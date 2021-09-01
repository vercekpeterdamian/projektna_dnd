import json

def modifier(xx):
    return xx // 2 - 5

ABILITIES = ['strg', 'dex', 'con', 'intl', 'wis', 'cha']
SKILLS = ['acrobatics', 'animal_handling', 'arcana', 'atheltics', 'deception', 'history', 'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 'stealth', 'survival']
SKILLS_DEX = ['acrobatics', 'sleight_of_hand', 'stealth']
SKILLS_WIS = ['animal_handling', 'insight', 'medicine', 'perception', 'survival']
SKILLS_INTL = ['arcana', 'history', 'investigation', 'nature', 'religion']
SKILLS_CHA = ['deception', 'intimidation', 'performance', 'persuasion']
SKILLS_STRG = ['athletics']

class Character:
    def __init__(self, name='', race='', subrace='', dclass='', dsubclass='', background=''):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.dclass = dclass
        self.dsubclass = dsubclass
        self.background = background

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
                'character_basic': (self.name, self.race, self.subrace, self.dclass, self.dsubclass, self.background),
                'level': self.lvl,
                'abilities': (self.strg, self.dex, self.con, self.intl, self.wis, self.cha),
                'skill_proficiencies': self.skill_prof_list,
                'saving_proficiencies': self.saving_profs_list,
                'character_appearance': (self.age, self.height, self.weight, self.eyes, self.complexion, self.hair)
                }

    @classmethod
    def load_character(cls, ch_slovar):
        name, race, subrace, dclass, dsubclass, background = ch_slovar['character_basic']
        character = Character(name, race, subrace, dclass, dsubclass, background)
        character.build_character(ch_slovar)
        return character

    def build_character(self, ch_slovar):
        self.set_level(ch_slovar['level'])
        strg, dex, con, intl, wis, cha = ch_slovar['abilities']
        self.set_ability_stats(strg, dex, con, intl, wis, cha)
        self.set_skill_proficiencies(ch_slovar['skill_proficiencies'])
        self.set_skills()
        self.set_saving_proficiencies(ch_slovar['saving_proficiencies'])
        self.set_saving()
        age, height, weight, eyes, complexion, hair = ch_slovar['character_appearance']
        self.set_character_appearance(age, height, weight, eyes, complexion, hair)


    def save_character(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.prepare_to_save(), datoteka, ensure_ascii=False, indent=4)

    @classmethod
    def load_character_from_file(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            ch_slovar = json.load(datoteka)
        return cls.load_character(ch_slovar)

class Diary:
    def __init__(self, zaporedni, datum):
        self.zaporedni = zaporedni
        self.datum = datum
        self.vsebina = ''

    def spremeni_vsebino(self, zaporedni, datum, vsebina):
        self.zaporedni = zaporedni
        self.datum = datum
        self.vsebina += vsebina 