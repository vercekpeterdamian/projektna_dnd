% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'><form action='/create-character/skills/' method='POST' style='margin: 0;'>
        <h1 class='element-title'>Skill proficiencies</h1>
        <div class='box'>
            <h3 class='top-margin'>Check the boxes assigned to the skills you're proficient in.</h3>
            % for x in range(18):
            <div class='box-field'>
                % if SKILLS_SLOVAR[x][0] in character.skill_prof_list:
                <input name={{SKILLS_SLOVAR[x][0]}} type='checkbox' checked>
                <label>{{SKILLS_SLOVAR[x][1]}}</label><br>
                % else:
                <input name={{SKILLS_SLOVAR[x][0]}} type='checkbox'>
                <label>{{SKILLS_SLOVAR[x][1]}}</label><br>
                % end
            </div>
            % end
        </div>
        <div class='box top-margin'>
            % if uporabnik.nov_uporabnik:
            <input type='submit' value='Continue'>
            % else:
            <input type='submit' value='Change'>
            % end
        </div>
    </form></div>
</div>