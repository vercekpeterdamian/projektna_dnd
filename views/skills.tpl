% rebase('osnova.tpl')
<form action='/create-character/skills/' method='POST'>
    <div>
        <div>
            <div>
                <p>
                    Check the boxes assigned to the skills you're proficient in.
                </p>
            </div>
            <div>
                % for x in range(18):
                    % if SKILLS_SLOVAR[x][0] in character.skill_prof_list:
                    <input name={{SKILLS_SLOVAR[x][0]}} type='checkbox' checked>
                    <label>{{SKILLS_SLOVAR[x][1]}}</label><br>
                    % else:
                    <input name={{SKILLS_SLOVAR[x][0]}} type='checkbox'>
                    <label>{{SKILLS_SLOVAR[x][1]}}</label><br>
                    % end
                % end
            </div>
        </div>
        % if uporabnik.nov_uporabnik:
        <div>
            <input type='submit' value='Create!'>
        </div>
        % else:
        <div>
            <input type='submit' value='Change'>
        </div>
        % end
    </div>
</form>