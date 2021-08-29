import model

slovar_sposobnosti = {1: 'acrobatics', 2: 'animal_handling', 3: 'arcana', 4: 'athetics', 5: 'deception', 6: 'history', 7: 'insight', 8: 'intimidation', 9: 'investigation', 10: 'medicine', 11: 'nature', 12: 'perception', 13: 'performance', 14: 'persuasion', 15: 'religion', 16: 'sleight_of_hand', 17: 'stealth', 18: 'survival'}
slovar_lastnosti = {1: 'strength', 2: 'dexterity', 3: 'constitution', 4: 'inteligence', 5: 'wisdom', 6: 'charisma'}
space = ' '

def izpis_junaka_osnova(hero):
    input(
        30 * '=' + '\n' +
        f'JUNAK {hero.name}\n' +
        f'Rasa    | {hero.race}\n' +
        f'Podrasa | {hero.subrace}\n' +
        f'Ceh     | {hero.dclass}\n' +
        f'Podceh  | {hero.dsubclass}\n' +
        f'Ozadje  | {hero.background}\n' +
        30 * '=' + '\n' +
        'Za vrnitev na domač zaslon pritisni "enter"'
    )
    return homescreen(hero)

def homescreen(hero):
    print(
        30 * '=' + '\n' +
        f'Dobrodošel {hero.name}!\n' +
        '1> Pokaži osnovne lastnosti\n' +
        '2> Pokaži lastnosti\n' +
        '3> Pokaži sposobnosti\n' +
        30 * '=' +'\n'
    )
    while True:
        inp = input('> ')
        if inp == '1':
            return izpis_junaka_osnova(hero)
        elif inp == '2':
            return izpis_junaka_lastnosti(hero)
        elif inp == '3':
            return izpis_junaka_sposobnosti(hero)
        else:
            print('Prosim odgovori z "1", "2" ali "3"\n>')

def izpis_junaka_lastnosti(hero):
    input(
        30 *  '=' + '\n'
        f'Strength      | {hero.strg} | mod: {hero.strg_modifier} | save mod: {hero.save_strg} |\n' +
        f'Dexterity     | {hero.dex} | mod: {hero.dex_modifier} | save mod: {hero.save_dex} |\n' +
        f'Constitution  | {hero.con} | mod: {hero.con_modifier} | save mod: {hero.save_con} |\n' +
        f'Inteligence   | {hero.intl} | mod: {hero.intl_modifier} | save mod: {hero.save_intl} |\n' +
        f'Wisdom        | {hero.wis} | mod: {hero.wis_modifier} | save mod: {hero.save_wis} |\n' +
        f'Charisma      | {hero.cha} | mod: {hero.cha_modifier} | save mod: {hero.save_cha} |\n' +
        30 * '=' + '\n' +
        'Za vrnitev na domač zaslon pritisni "enter"'
    )
    return homescreen(hero)

def izpis_junaka_sposobnosti(hero):
    return izpis_junaka_osnova(hero)



def zagon():
    print('Pozdravljen v Dungeoneeru! Za začetek ustvarimo tvojega junaka.')
    name = input('Vnesi ime:\n> ')
    race = input('Vnesi raso:\n> ')
    subrace = input('Vnesi podraso:\n> ')
    dclass = input('Vnesi ceh:\n> ')
    dsubclass = input('Vnesi podceh:\n> ')
    background = input('Vnesi ozadje:\n> ')
    hero = model.Character(name, race, subrace, dclass, dsubclass, background)
    print(f'Super, {hero.name} je že na dobri poti.')
    lvl = input(f'Kateri level je {hero.name}?\n> ')
    hero.set_level(int(lvl))
    print('Sedaj vnesi junakove lastnosti (1-20).')
    strg = input('Vnesi moč:\n> ')
    dex = input('Vnesi hitrost:\n> ')
    con = input('Vnesi telesno utrjenost:\n> ')
    intl = input('Vnesi inteligenco:\n> ')
    wis = input('Vnesi modrost:\n> ')
    cha = input('vnesi karizmo:\n> ')
    hero.set_ability_stats(int(strg), int(dex), int(con), int(intl), int(wis), int(cha))
    print('V dani tabeli izberi številke ki pripadajo sposobnostim v katerih si vešč:')
    for x in range(1, 19):
        print(f'|{x}| {slovar_sposobnosti[x] + (18 - len(slovar_sposobnosti[x])) * space} |')
    ima_kaj_za_dodat = True
    sposob = set()
    while ima_kaj_za_dodat:
        skill = int(input('Vnesi število:\n> '))
        sposob.add(slovar_sposobnosti[skill])
        inp = input('Imaš še kaj za dodat?\na) Da.\nb) Ne\n> ')
        if 'a' in inp.lower() or 'd' in inp.lower() or 'y' in inp.lower:
            continue
        else:
            ima_kaj_za_dodat = False
            continue
    hero.set_skills(sposob)
    print('Skoraj si že na koncu, dodaj le še veščost v obrambnih metih.')
    print('V dani tabeli izberi številki:')
    for x in range(1, 7):
        print(f'|{x}| {slovar_lastnosti[x] + (10 -  len(slovar_lastnosti[x])) * space} |')
    ima_kaj_za_dodat = True
    last = set()
    while ima_kaj_za_dodat:
        ability = int(input('Vnesi Število:\n> '))
        last.add(slovar_lastnosti[ability])
        inp = input('Imaš še kaj za dodat?\na) Da.\nb) Ne\n> ')
        if 'a' in inp.lower() or 'd' in inp.lower() or 'y' in inp.lower:
            continue
        else:
            ima_kaj_za_dodat = False
            continue
    print('Super, osnova tvojega junaka je dokončana!')
    return homescreen(hero)





    




