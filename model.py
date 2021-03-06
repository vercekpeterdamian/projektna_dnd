import json
import hashlib
import random

def modifier(xx):
    return int(xx) // 2 - 5

def kljuci_v_seznam(slovar, izjema):
    kljuci = slovar.keys()
    seznam = []
    for kljuc in kljuci:
        if kljuc == izjema:
            continue
        else:
            seznam.append(kljuc)
    return seznam


ABILITIES = ['strg', 'dex', 'con', 'intl', 'wis', 'cha']
SKILLS = ['acrobatics', 'animal_handling', 'arcana', 'atheltics', 'deception', 'history', 'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 'stealth', 'survival']
SKILLS_SLOVAR = {'strg': ['athletics'], 'dex': ['acrobatics', 'sleight_of_hand', 'stealth'], 'con': [], 'intl': ['arcana', 'history', 'investigation', 'nature', 'religion'], 'wis': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'], 'cha': ['deception', 'intimidation', 'performance', 'persuasion']}
COMBAT = ['current_hp', 'max_hp', 'initiative', 'attack_mod', 'ac', 'save_dc']

class Uporabnik: ##
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, character, nov_uporabnik=1):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.character = character
        self.nov_uporabnik = nov_uporabnik

    @staticmethod
    def prijava(uporabnisko_ime, geslo_v_cistopisu):
        uporabnik = Uporabnik.iz_datoteke(uporabnisko_ime)
        if uporabnik is None:
            raise ValueError('This user does not exist')
        elif uporabnik.preveri_geslo(geslo_v_cistopisu):
            return uporabnik
        else:
            raise ValueError('The password is incorrect')

    @staticmethod
    def registracija(uporabnisko_ime, geslo_v_cistopisu):
        if Uporabnik.iz_datoteke(uporabnisko_ime) is not None:
            raise ValueError('This username is already occupied')
        else:
            zasifrirano_geslo = Uporabnik._zasifriraj_geslo(geslo_v_cistopisu)
            uporabnik = Uporabnik(uporabnisko_ime, zasifrirano_geslo, Character())
            uporabnik.v_datoteko()
            return uporabnik

    def _zasifriraj_geslo(geslo_v_cistopisu, sol=None):
        if sol is None:
            sol = str(random.getrandbits(32))
        posoljeno_geslo = sol + geslo_v_cistopisu
        h = hashlib.blake2b()
        h.update(posoljeno_geslo.encode(encoding='utf-8'))
        return f'{sol}${h.hexdigest()}'

    def v_slovar(self):
        return {
            'nov_uporabnik': self.nov_uporabnik,
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'character': self.character.prepare_to_save()
        }

    def v_datoteko(self):
        with open(Uporabnik.ime_uporabnikove_datoteke(self.uporabnisko_ime), 'w', encoding='utf8') as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)

    def preveri_geslo(self, geslo_v_cistopisu):
        sol, _ = self.zasifrirano_geslo.split('$')
        return self.zasifrirano_geslo == Uporabnik._zasifriraj_geslo(geslo_v_cistopisu, sol)

    @staticmethod
    def ime_uporabnikove_datoteke(uporabnisko_ime):
        return f'{uporabnisko_ime}.json'

    @staticmethod
    def iz_slovarja(slovar):
        uporabnisko_ime = slovar['uporabnisko_ime']
        zasifrirano_geslo = slovar['zasifrirano_geslo']
        character = Character.load_character(slovar['character'], slovar['nov_uporabnik'])
        nov_uporabnik = slovar['nov_uporabnik']
        return Uporabnik(uporabnisko_ime, zasifrirano_geslo, character, nov_uporabnik)

    @staticmethod
    def iz_datoteke(uporabnisko_ime):
        try:
            with open(Uporabnik.ime_uporabnikove_datoteke(uporabnisko_ime), encoding='utf8') as datoteka:
                slovar = json.load(datoteka)
                return Uporabnik.iz_slovarja(slovar)
        except FileNotFoundError:
            return None


class Character:
    def __init__(self, name='', race='', subrace='', dclass='', dsubclass='', background=''):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.dclass = dclass
        self.dsubclass = dsubclass
        self.background = background
        self.abilities_are = False
        self.lvl = 0
        self.saving_profs_list = []
        self.skill_prof_list = []
        self.diary = {0: 1}
        self.wallet = {0: 1}
        self.combat = {}

    def add_diary(self, naslov, datum, vsebina):
        self.diary[self.diary[0]] = [naslov, datum, vsebina]
        self.diary[0] += 1

    def add_transaction(self, naslov, datum, znesek, opis=''):
        self.wallet[self.wallet[0]] = [naslov, datum, int(znesek), opis]
        self.wallet[0] += 1
        self.izracunaj_financno_stanje()

    def izracunaj_financno_stanje(self):
        id_lista_transakcij = kljuci_v_seznam(self.wallet, 0)
        skupaj = 0
        for transakcija_id in id_lista_transakcij:
            skupaj += self.wallet[transakcija_id][2]
        self.financno_stanje = skupaj

    def set_level(self, lvl):
        self.lvl = lvl
        self.prof_bonus = (lvl - 1) // 4 + 2

    def set_ability_stats(self, strg, dex, con, intl, wis, cha):
        self.abilities = {}
        self.abilities_mods = {}
        self.abilities['strg'] = strg
        self.abilities_mods['strg'] = modifier(strg)
        self.abilities['dex'] = dex
        self.abilities_mods['dex'] = modifier(dex)
        self.abilities['con'] = con
        self.abilities_mods['con'] = modifier(con)
        self.abilities['intl'] = intl
        self.abilities_mods['intl'] = modifier(intl)
        self.abilities['wis'] = wis
        self.abilities_mods['wis'] = modifier(wis)
        self.abilities['cha'] = cha
        self.abilities_mods['cha'] = modifier(cha)
        self.abilities_are = True

    def set_skill_proficiencies(self, proficiency_list):
        self.skill_prof_list = proficiency_list

    def set_skills(self):
        self.skills = {}
        for ability in ABILITIES:
            for skill in SKILLS_SLOVAR[ability]:
                self.skills[skill] = self.abilities_mods[ability]
                if skill in self.skill_prof_list:
                    self.skills[skill] += self.prof_bonus

    def set_saving_proficiencies(self, save_proficiencies_list):
        self.saving_profs_list = save_proficiencies_list

    def set_saving(self):
        self.saving_mods = {}
        for ability in ABILITIES:
            self.saving_mods[ability] = self.abilities_mods[ability] + int(ability in self.saving_profs_list) * self.prof_bonus

    def change_level(self, lvl):
        self.lvl = lvl
        self.prof_bonus = (lvl - 1) // 4 + 2
        self.set_skills()
        self.set_saving()

    def change_ability_stats(self, strg, dex, con, intl, wis, cha):
        self.set_ability_stats(self, strg, dex, con, intl, wis, cha)
        self.set_skills()
        self.set_saving()

    def set_combat(self, combat_slovar):
        for cmb in COMBAT:
            self.combat[cmb] = combat_slovar[cmb]

    def prepare_to_save(self): ##
        if not self.abilities_are:
            self.set_ability_stats(0, 0, 0, 0, 0, 0)
        return {
            'about': {
                'character_basic': [self.name, self.race, self.subrace, self.dclass, self.dsubclass, self.background],
                'level': self.lvl,
                'abilities': [self.abilities['strg'], self.abilities['dex'], self.abilities['con'], self.abilities['intl'], self.abilities['wis'], self.abilities['cha']],
                'skill_proficiencies': self.skill_prof_list,
                'saving_proficiencies': self.saving_profs_list,
                'combat' : {cmb: self.combat.get(cmb, 0) for cmb in COMBAT}
            },
            'wallet': [
                {
                    'kljuc': kljuc,
                    'transakcija': self.wallet[kljuc]
                } for kljuc in self.wallet.keys()
            ],
            'diary': [
                {
                    'kljuc': kljuc,
                    'dnevnik': self.diary[kljuc]
                } for kljuc in self.diary.keys()
            ]
        }
                


    @classmethod ##
    def load_character(cls, ch_slovar, nov_uporabnik):
        name, race, subrace, dclass, dsubclass, background = ch_slovar['about']['character_basic']
        character = Character(name, race, subrace, dclass, dsubclass, background)
        character.build_character(ch_slovar['about'])
        if not nov_uporabnik:
            character.nalozi_denarnico_in_dnevnik(ch_slovar)
        character.izracunaj_financno_stanje()
        return character

    def build_character(self, ch_slovar_about):
        self.set_level(ch_slovar_about['level'])
        strg, dex, con, intl, wis, cha = ch_slovar_about['abilities']
        self.set_ability_stats(strg, dex, con, intl, wis, cha)
        self.set_skill_proficiencies(ch_slovar_about['skill_proficiencies'])
        self.set_skills()
        self.set_saving_proficiencies(ch_slovar_about['saving_proficiencies'])
        self.set_saving()
        self.set_combat(ch_slovar_about['combat'])


    def nalozi_denarnico_in_dnevnik(self, ch_slovar):
        for transakcija in ch_slovar['wallet']:
            if transakcija['kljuc'] == 0:
                self.wallet[0] = transakcija['transakcija']
            else:
                kljuc = transakcija['kljuc']
                naslov, datum, znesek, opis = transakcija['transakcija']
                self.wallet[kljuc] = [naslov, datum, int(znesek), opis]
        for vnos in ch_slovar['diary']:
            if vnos['kljuc'] == 0:
                self.diary[0] = vnos['dnevnik']
            else:
                kljuc = vnos['kljuc']
                naslov, datum, vsebina = vnos['dnevnik']
                self.diary[kljuc] = [naslov, datum, vsebina]


    def save_character(self, ime_datoteke): ##
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.prepare_to_save(), datoteka, ensure_ascii=False, indent=4)

    @classmethod ##
    def load_character_from_file(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            ch_slovar = json.load(datoteka)
        return cls.load_character(ch_slovar)