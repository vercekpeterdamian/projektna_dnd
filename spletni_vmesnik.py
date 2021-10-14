import bottle
from model import Uporabnik, kljuci_v_seznam
from datetime import date

PISKOTEK_UPORABNISKO_IME = 'User_cookies'
SKRIVNOST = 'moja macka Mufi'
SKILLS_SLOVAR = {0: ('acrobatics', 'Acrobatics'), 1: ('animal_handling', 'Animal handling'), 2: ('arcana', 'Arcana'), 3: ('athletics', 'Athletics'), 4: ('deception', 'Deception'), 5: ('history', 'History'), 6: ('insight', 'Insight'), 7: ('intimidation', 'Intimidation'), 8: ('investigation', 'Investigation'), 9: ('medicine', 'Medicine'), 10: ('nature', 'Nature'), 11: ('perception', 'Perception'), 12: ('performance', 'Performance'), 13: ('persuasion', 'Persuasion'), 14: ('religion', 'Religion'), 15: ('sleight_of_hand', 'Sleight of hand'), 16: ('stealth', 'Stealth'), 17: ('survival', 'Survival')}
ABILITIES_SLOVAR = {0: ('strg', 'Strength', 'STR'), 1: ('dex', 'Dexterity', 'DEX'), 2: ('con', 'Constitution', 'CON'), 3: ('intl', 'Intelligent', 'INT'), 4: ('wis', 'Wisdom', 'WIS'), 5: ('cha', 'Charisma', 'CHA')}
COMBAT_SLOVAR = {0: ('current_hp', 'HP'), 1: ('max_hp', 'Max. HP'), 2: ('initiative', 'Init.'), 3: ('attack_mod', 'Atk MOD'), 4: ('ac', 'AC'), 5: ('save_dc', 'Save DC')}

def shrani_stanje(uporabnik): ##
    uporabnik.v_datoteko()


def trenutni_uporabnik(): ##
    uporabnisko_ime = bottle.request.get_cookie(
        PISKOTEK_UPORABNISKO_IME, secret=SKRIVNOST
    )
    if uporabnisko_ime:
        return podatki_uporabnika(uporabnisko_ime)
    else:
        bottle.redirect('/signin/')


def podatki_uporabnika(uporabnisko_ime): ##
    return Uporabnik.iz_datoteke(uporabnisko_ime)


@bottle.get('/static/<ime_dat:path>') ##
def server_static(ime_dat):
    pot = 'staticne_datoteke'
    return bottle.static_file(ime_dat, root=pot)


@bottle.get('/') ##
def osnovni_zaslon():
    bottle.redirect('/character/')


@bottle.get('/register/') ##
def registracija_get():
    return bottle.template('register.tpl', napaka=None)


@bottle.post('/register/') ##
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('username')
    geslo_v_cistopisu = bottle.request.forms.getunicode('password')
    if not uporabnisko_ime:
        return bottle.template('register.tpl', napaka='Enter a username!')
    try:
        Uporabnik.registracija(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path='/', secret=SKRIVNOST
        )
        bottle.redirect('/')
    except ValueError as e:
        return bottle.template('register.tpl', napaka=e.args[0])


@bottle.get('/signin/') ##
def prijava_get():
    return bottle.template('signin.tpl', napaka=None)


@bottle.post('/signin/') ##
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('username')
    geslo_v_cistopisu = bottle.request.forms.getunicode('password')
    if not uporabnisko_ime:
        return bottle.template('signin.tpl', napaka='Enter your username!')
    try:
        Uporabnik.prijava(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path='/', secret=SKRIVNOST
        )
        bottle.redirect('/')
    except ValueError as e:
        return bottle.template('signin.tpl', napaka=e.args[0])


@bottle.post('/signout/') ##
def odjava():
    bottle.response.delete_cookie(PISKOTEK_UPORABNISKO_IME, path='/')
    bottle.redirect('/')


@bottle.get('/character/')
def character_homepage():
    uporabnik = trenutni_uporabnik()
    wallet_ids = kljuci_v_seznam(uporabnik.character.wallet, 0)
    wallet_ids.sort(reverse=True)
    diary_ids = kljuci_v_seznam(uporabnik.character.diary, 0)
    diary_ids.sort(reverse=True)
    return bottle.template(
        'character.tpl',
        character=uporabnik.character,
        uporabnik=uporabnik,
        ABILITIES_SLOVAR=ABILITIES_SLOVAR,
        SKILLS_SLOVAR=SKILLS_SLOVAR,
        COMBAT_SLOVAR=COMBAT_SLOVAR,
        diary_ids=diary_ids,
        wallet_ids=wallet_ids
    )


@bottle.get('/create-character/')
def create_character_get():
    return bottle.template(
        'create-character.tpl', 
        SKILLS_SLOVAR = SKILLS_SLOVAR
    )


@bottle.get('/create-character/about/')
def create_character_about_get():
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        'about.tpl', 
        uporabnik=uporabnik,
        character=uporabnik.character
    )


@bottle.post('/create-character/about/')
def create_character_about_post():
    uporabnik = trenutni_uporabnik()
    ch_name = bottle.request.forms.getunicode('ch_name')
    uporabnik.character.name = ch_name
    ch_race = bottle.request.forms.getunicode('ch_race')
    uporabnik.character.race = ch_race
    ch_subrace = bottle.request.forms.getunicode('ch_subrace')
    uporabnik.character.subrace = ch_subrace
    ch_class = bottle.request.forms.getunicode('ch_class')
    uporabnik.character.dclass = ch_class
    ch_subclass = bottle.request.forms.getunicode('ch_subclass')
    uporabnik.character.dsubclass = ch_subclass
    ch_background = bottle.request.forms.getunicode('ch_background')
    uporabnik.character.background = ch_background
    shrani_stanje(uporabnik)
    if uporabnik.nov_uporabnik:
        bottle.redirect('/create-character/abilities/')
    else:
        bottle.redirect('/')


@bottle.get('/create-character/abilities/')
def create_character_abilities_get():
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        'abilities.tpl', 
        uporabnik=uporabnik, 
        character=uporabnik.character, 
        ABILITIES_SLOVAR=ABILITIES_SLOVAR
    )


@bottle.post('/create-character/abilities/')
def create_character_abilities_post():
    uporabnik = trenutni_uporabnik()
    lvl = bottle.request.forms['level']
    uporabnik.character.set_level(int(lvl))
    strg = bottle.request.forms['strength']
    dex = bottle.request.forms['dexterity']
    con = bottle.request.forms['constituion']
    intl = bottle.request.forms['inteligence']
    wis = bottle.request.forms['wisdom']
    cha = bottle.request.forms['charisma']
    uporabnik.character.set_ability_stats(strg, dex, con, intl, wis, cha)
    saving_profs = []
    for x in range(6):
        if ABILITIES_SLOVAR[x][0] in bottle.request.forms.keys():
            saving_profs.append(ABILITIES_SLOVAR[x][0])
    uporabnik.character.set_saving_proficiencies(saving_profs)
    shrani_stanje(uporabnik)
    if uporabnik.nov_uporabnik:
        bottle.redirect('/create-character/skills/')
    else:
        bottle.redirect('/')


@bottle.get('/create-character/skills/')
def create_character_skills_get():
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        'skills.tpl', 
        uporabnik=uporabnik, 
        character=uporabnik.character, 
        SKILLS_SLOVAR=SKILLS_SLOVAR
    )

    
@bottle.post('/create-character/skills/')
def create_character_skills_post():
    uporabnik = trenutni_uporabnik()
    skill_profs = []
    for x in range(18):
        if SKILLS_SLOVAR[x][0] in bottle.request.forms.keys():
            skill_profs.append(SKILLS_SLOVAR[x][0])
    uporabnik.character.set_skill_proficiencies(skill_profs)
    shrani_stanje(uporabnik)
    if uporabnik.nov_uporabnik:
        bottle.redirect('/create-character/combat/')
    else:
        bottle.redirect('/')


@bottle.get('/create-character/combat/')
def create_character_combat_get():
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        'combat.tpl',
        uporabnik=uporabnik,
        character=uporabnik.character
    )


@bottle.post('/create-character/combat/')
def create_character_combat_post():
    uporabnik = trenutni_uporabnik()
    for x in range(6):
        if x == 0:
            cmb = COMBAT_SLOVAR[x][0]
            num = bottle.request.forms['max_hp']
            uporabnik.character.combat[cmb] = int(num)
        else:
            cmb = COMBAT_SLOVAR[x][0]
            num = bottle.request.forms[cmb]
            uporabnik.character.combat[cmb] = int(num)
    uporabnik.nov_uporabnik = 0
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.post('/combat/change-hp/')
def change_hp():
    uporabnik = trenutni_uporabnik()
    num = bottle.request.forms['change']
    predznak = 1
    if bottle.request.forms['plusminus'] == 'Taken':
        predznak = -1
    uporabnik.character.combat['current_hp'] += predznak * int(num)
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.post('/wallet-entry/')
def wallet_entry_post():
    uporabnik = trenutni_uporabnik()
    naslov = bottle.request.forms.getunicode('naslov')
    datum = date.today().strftime("%Y-%m-%d")
    znesek = bottle.request.forms.getunicode('znesek')
    if 'opis' not in bottle.request.forms.keys():
        opis = ''
    else:
        opis = bottle.request.forms.getunicode('opis')
    uporabnik.character.add_transaction(naslov, datum, znesek, opis)
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.post('/wallet-entry-delete/<trans_id:int>/')
def delete_wallet_entry(trans_id):
    uporabnik = trenutni_uporabnik()
    uporabnik.character.wallet.pop(trans_id)
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.post('/diary-entry/')
def diary_entry_post():
    uporabnik = trenutni_uporabnik()
    naslov = bottle.request.forms.getunicode('naslov')
    datum = date.today().strftime('%Y-%m-%d')
    if 'vsebina' not in bottle.request.forms.keys():
        vsebina = ''
    else:
        vsebina = bottle.request.forms.getunicode('vsebina')
    uporabnik.character.add_diary(naslov, datum, vsebina)
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.post('/diary-entry-delete/<diary_id:int>/')
def delete_diary_entry(diary_id):
    uporabnik = trenutni_uporabnik()
    uporabnik.character.diary.pop(diary_id)
    shrani_stanje(uporabnik)
    bottle.redirect('/')


@bottle.get('/confirm-delete/<slovar>/<id:int>/')
def confirm_delete(slovar, id):
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        'confirm-delete.tpl',
        uporabnik=uporabnik,
        character=uporabnik.character,
        slovar=slovar,
        id=id
    )


bottle.run(debug=True, reloader=True)