import json
import hashlib
import random

def modifier(xx):
    return xx // 2 - 5

ABILITIES = ['strg', 'dex', 'con', 'intl', 'wis', 'cha']
SKILLS = ['acrobatics', 'animal_handling', 'arcana', 'atheltics', 'deception', 'history', 'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 'stealth', 'survival']
SKILLS_DEX = ['acrobatics', 'sleight_of_hand', 'stealth']
SKILLS_WIS = ['animal_handling', 'insight', 'medicine', 'perception', 'survival']
SKILLS_INTL = ['arcana', 'history', 'investigation', 'nature', 'religion']
SKILLS_CHA = ['deception', 'intimidation', 'performance', 'persuasion']
SKILLS_STRG = ['athletics']


class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, character):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.character = character

    @staticmethod
    def prijava(uporabnisko_ime, geslo_v_cistopisu):
        uporabnik = Uporabnik.iz_datoteke(uporabnisko_ime)
        if uporabnik is None:
            raise ValueError('This user does not exist')
        elif uporabnik.prevri_geslo(geslo_v_cistopisu):
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
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'character': self.character.prepare_to_save(),
        }

    def v_datoteko(self):
        with open(
            Uporabnik.ime_uporabnikove_datoteke(self.uporabnisko_ime), 'w'
        ) as datoteka:
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
        character = Character.load_character(slovar['character'])
        return Uporabnik(uporabnisko_ime, zasifrirano_geslo, character)

    @staticmethod
    def iz_datoteke(uporabnisko_ime):
        try:
            with open(Uporabnik.ime_uporabnikove_datoteke(uporabnisko_ime)) as datoteka:
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
        self.diary = []
        self.wallet = []

    def add_diary(self, naslov, datum, vsebina):
        self.diary.append((naslov, datum, vsebina))

    def add_transaction(self, naslov, datum, znesek, opis=''):
        self.wallet.append((naslov, datum, int(znesek), opis))
        self.izracunaj_financno_stanje()

    def izracunaj_financno_stanje(self):
        skupaj = 0
        for transakcija in self.wallet:
            skupaj += transakcija[2]
        self.financno_stanje = skupaj

    def set_level(self, lvl):
        self.lvl = lvl
        self.prof_bonus = (lvl - 1) // 4 + 2

    def set_ability_stats(self, strg, dex, con, intl, wis, cha):
        self.strg = strg
        self.strg_modifier = modifier(strg)
        self.dex = dex
        self.dex_modifier = modifier(dex)
        self.con = con
        self.con_modifier = modifier(con)
        self.intl = intl
        self.intl_modifier = modifier(intl)
        self.wis = wis
        self.wis_modifier = modifier(wis)
        self.cha = cha
        self.cha_modifier = modifier(cha)

    def set_skill_proficiencies(self, proficiency_list):
        self.skill_prof_list = proficiency_list

    def set_skills(self):
        self.skills = {}
        for skill in SKILLS_DEX:
            self.skills[skill] = self.dex_modifier
            if skill in self.skill_prof_list:
                self.skills[skill] += self.prof_bonus
        for skill in SKILLS_WIS:
            self.skills[skill] = self.wis_modifier
            if skill in self.skill_prof_list:
                self.skills[skill] += self.prof_bonus
        for skill in SKILLS_INTL:
            self.skills[skill] = self.intl_modifier
            if skill in self.skill_prof_list:
                self.skills[skill] += self.prof_bonus
        for skill in SKILLS_CHA:
            self.skills[skill] = self.cha_modifier
            if skill in self.skill_prof_list:
                self.skills[skill] += self.prof_bonus
        for skill in SKILLS_STRG:
            self.skills[skill] = self.strg_modifier
            if skill in self.skill_prof_list:
                self.skills[skill] += self.prof_bonus

    def set_saving_proficiencies(self, save_proficiencies_list):
        self.saving_profs_list = save_proficiencies_list

    def set_saving(self):
        self.save_strg = self.strg_modifier + int('strg' in self.saving_profs_list) * self.prof_bonus
        self.save_dex = self.dex_modifier + int('dex' in self.saving_profs_list) * self.prof_bonus
        self.save_con = self.con_modifier + int('con' in self.saving_profs_list) * self.prof_bonus
        self.save_intl = self.intl_modifier + int('intl' in self.saving_profs_list) * self.prof_bonus
        self.save_wis = self.intl_modifier + int('wis' in self.saving_profs_list) * self.prof_bonus
        self.save_cha = self.cha_modifier + int('cha' in self.saving_profs_list) * self.prof_bonus

    def change_level(self, lvl):
        self.lvl = lvl
        self.prof_bonus = (lvl - 1) // 4 + 2
        self.set_skills()
        self.set_saving()

    def change_ability_stats(self, strg, dex, con, intl, wis, cha):
        self.set_ability_stats(self, strg, dex, con, intl, wis, cha)
        self.set_skills()
        self.set_saving()

    def set_character_appearance(self, age, height, weight, eyes, complexion, hair):
        self.age = age
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.complexion = complexion
        self.hair = hair

    def set_about(self, text):
        self.about = text

    def prepare_to_save(self):
        return {
            'about': {
                'character_basic': (self.name, self.race, self.subrace, self.dclass, self.dsubclass, self.background),
                'level': self.lvl,
                'abilities': (self.strg, self.dex, self.con, self.intl, self.wis, self.cha),
                'skill_proficiencies': self.skill_prof_list,
                'saving_proficiencies': self.saving_profs_list,
                'character_appearance': (self.age, self.height, self.weight, self.eyes, self.complexion, self.hair)
            },
            'wallet': self.wallet,
            'diary': self.diary
        }
                


    @classmethod
    def load_character(cls, ch_slovar):
        name, race, subrace, dclass, dsubclass, background = ch_slovar['about']['character_basic']
        character = Character(name, race, subrace, dclass, dsubclass, background)
        character.build_character(ch_slovar['about'])
        character.wallet = ch_slovar['wallet']
        character.diary = ch_slovar['diary']
        return character

    def build_character(self, ch_slovar_about):
        self.set_level(ch_slovar_about['level'])
        strg, dex, con, intl, wis, cha = ch_slovar_about['abilities']
        self.set_ability_stats(strg, dex, con, intl, wis, cha)
        self.set_skill_proficiencies(ch_slovar_about['skill_proficiencies'])
        self.set_skills()
        self.set_saving_proficiencies(ch_slovar_about['saving_proficiencies'])
        self.set_saving()
        age, height, weight, eyes, complexion, hair = ch_slovar_about['character_appearance']
        self.set_character_appearance(age, height, weight, eyes, complexion, hair)


    def save_character(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.prepare_to_save(), datoteka, ensure_ascii=False, indent=4)

    @classmethod
    def load_character_from_file(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            ch_slovar = json.load(datoteka)
        return cls.load_character(ch_slovar)