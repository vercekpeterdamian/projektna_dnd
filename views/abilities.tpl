% rebase('osnova.tpl')
<form action='/create-character/abilities/' method='POST'>
    <div>
        <div>
            <div>
                <p>
                    Insert the level of your character.
                </p>
            </div>
            <div>
                <label>Level:</label>
                <input name="level" type="number" placeholder="level" value="1">
            </div>
        </div>
        <div>
            <div>
                <p>
                    Insert your ability stats and check the boxes next to those in which you have saving proficiency. 
                </p>
            </div>
            <div>
                <label>Strength:</label>
                <input name="strength" type="number" placeholder="str" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['strg'] }}"><input name="strg" type="checkbox"><br>
                <label>Dexterity:</label>
                <input name="dexterity" type="number" placeholder="dex" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['dex'] }}"><input name="dex" type="checkbox"><br>
                <label>Constitution:</label>
                <input name="constituion" type="number" placeholder="con" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['con'] }}"><input name="con" type="checkbox"><br>
                <label>Inteligence:</label>
                <input name="inteligence" type="number" placeholder="int" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['intl'] }}"><input name="intl" type="checkbox"><br>
                <label>Wisdom:</label>
                <input name="wisdom" type="number" placeholder="wis" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['wis'] }}"><input name="wis" type="checkbox"><br>
                <label>Charisma:</label>
                <input name="charisma" type="number" placeholder="cha" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['cha'] }}"><input name="cha" type="checkbox"><br>
            </div>
        </div>
        % if uporabnik.nov_uporabnik:
        <div>
            <input type='submit' value='Continue'>
        </div>
        % else:
        <div>
            <input type='submit' value='Change'>
        </div>
        % end
    </div>
</form>