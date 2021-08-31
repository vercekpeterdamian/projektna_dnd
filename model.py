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
        self.coplexion = complexion
        self.hair = hair

    def set_appearance_description(self, description):
        self.appearance_description = description

    def set_backstory(self, backstory):
        self.backstory = backstory

    def set_allies_and_organizations(self, description, name):
        self.aao_name = name
        self.aao_description = description
    
    def set_additional_features_and_traits(self, description):
        self.aft = description

    def set_treasure(self, treasure):
        self.treasure = treasure

class Wallet:
    def __init__(self, lastnik):
        self.lastnik = lastnik
        self.stanje = 0

    def posodobi_stanje(self, znesek):
        self.stanje += znesek

    #def zabeleži_transakcijo(self, znesek, namen, opombe):
    #    #### DODAJ .JSON REŠITEV ####
    #    pass

#class Diary:
#    def __init__(self, zaporedni, datum):
#        self.zaporedni = zaporedni
#        self.datum = datum
#        self.vsebina = ''
#
#    def dodaj_vsebino(self, vsebina):
#        self.vsebina += vsebina
