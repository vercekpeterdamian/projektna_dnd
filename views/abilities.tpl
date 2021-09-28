% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'><form action='/create-character/abilities/' method='POST' style='margin: 0;'>
        <h1 class='element-title'>Abilities</h1>
        <div class='box'>
            <h3 class='top-margin'>Insert the level of your character.</h3>
            <div class='box-field'>
                <input name="level" type="number" placeholder="level" value="{{ 1 if uporabnik.nov_uporabnik else character.lvl }}">
            </div>
        </div>
        <div class='box top-margin'>
            <h3 class='top-margin'>Insert your ability stats and check the boxes next to those in which you have saving proficiency.</h3>
            <label>Strength:</label>
            <div class='box-field'><input name="strength" type="number" placeholder="str" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['strg'] }}"><input name="strg" type="checkbox"></div>
            <label>Dexterity:</label>
            <div class='box-field'><input name="dexterity" type="number" placeholder="dex" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['dex'] }}"><input name="dex" type="checkbox"></div>
            <label>Constitution:</label>
            <div class='box-field'><input name="constituion" type="number" placeholder="con" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['con'] }}"><input name="con" type="checkbox"></div>
            <label>Inteligence:</label>
            <div class='box-field'><input name="inteligence" type="number" placeholder="int" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['intl'] }}"><input name="intl" type="checkbox"></div>
            <label>Wisdom:</label>
            <div class='box-field'><input name="wisdom" type="number" placeholder="wis" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['wis'] }}"><input name="wis" type="checkbox"></div>
            <label>Charisma:</label>
            <div class='box-field'><input name="charisma" type="number" placeholder="cha" value="{{ 10 if uporabnik.nov_uporabnik else character.abilities['cha'] }}"><input name="cha" type="checkbox"></div>
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