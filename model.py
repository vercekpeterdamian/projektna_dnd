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
    def __init__(self, name, race, subrace, dclass, dsubclass, background):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.dclass = dclass
        self.dsubclass = dsubclass
        self.background = background

    def set_proficiency_bonus(self, prof_bonus):
        self.prof_bonus = prof_bonus

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

    def set_skills(self, proficiency_list):
        for skill in SKILLS_DEX:
            self.skill = self.dex_modifier
            if skill in proficiency_list:
                self.skill += self.prof_bonus
        for skill in SKILLS_WIS:
            self.skill = self.wis_modifier
            if skill in proficiency_list:
                self.skill += self.prof_bonus
        for skill in SKILLS_INTL:
            self.skill = self.int_modifier
            if skill in proficiency_list:
                self.skill += self.prof_bonus
        for skill in SKILLS_CHA:
            self.skill = self.cha_modifier
            if skill in proficiency_list:
                self.skill += self.prof_bonus
        for skill in SKILLS_STRG:
            self.skill = self.strg_modifier
            if skill in proficiency_list:
                self.skill += self.prof_bonus
        
    def set_saving_profs(self, saving_profs_list):
        self.save_strg = self.strg_modifier
        self.save_dex = self.dex_modifier
        self.save_con = self.con_modifier
        self.save_intl = self.intl_modifier
        self.save_wis = self.intl_modifier
        self.save_cha = self.cha_modifier
        
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

    def set_allies_and_organizations(self, description, name, logo):
        self.aao_name = name
        self.aao_description = description
        self.aao_logo = logo
    
    def set_additional_features_and_traits(self, description):
        self.aft = description

    def set_treasure(self, treasure):
        self.treasure = treasure
