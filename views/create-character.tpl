% rebase('osnova.tpl')
<h1>Character creation!</h1>
<p>
    If you don't know how to create a character you can find help
    most of it <a href='https://www.instructables.com/Creating-a-DD-5e-Character-for-Beginners/'>here</a>.
    And <a href='http://dnd5e.wikidot.com/'>this</a> is a website where all the races, classes and more is gathered.
</p>
<form method='POST'>
    <div>
        <div>
            <p>
                Insert your character's about information.
            </p>
        </div>
        <div>
            <label>Name:</label>
            <input name="ch_name" type="text" placeholder="name"><br>
            <label>Race:</label>
            <input name="ch_race" type="text" placeholder="race"><br>
            <label>Subrace:</label>
            <input name="ch_subrace" type="text" placeholder="subrace"><br>
            <label>Class:</label>
            <input name="ch_class" type="text" placeholder="class"><br>
            <label>Subclass:</label>
            <input name="ch_subclass" type="text" placeholder="subclass"><br>
            <label>Background:</label>
            <input name="ch_background" type="text" placeholder="background"><br>
        </div>
    </div>
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
            <input name="strength" type="number" placeholder="str" value="10"><input name="strg" type="checkbox"><br>
            <label>Dexterity:</label>
            <input name="dexterity" type="number" placeholder="dex" value="10"><input name="dex" type="checkbox"><br>
            <label>Constitution:</label>
            <input name="constituion" type="number" placeholder="con" value="10"><input name="con" type="checkbox"><br>
            <label>Inteligence:</label>
            <input name="inteligence" type="number" placeholder="int" value="10"><input name="intl" type="checkbox"><br>
            <label>Wisdom:</label>
            <input name="wisdom" type="number" placeholder="wis" value="10"><input name="wis" type="checkbox"><br>
            <label>Charisma:</label>
            <input name="charisma" type="number" placeholder="cha" value="10"><input name="cha" type="checkbox"><br>
        </div>
    </div>
    <div>
        <div>
            <p>
                Check the boxes assigned to the skills you're proficient in.
            </p>
        </div>
        <div>
            % for x in range(18):
            <input name={{SKILLS_SLOVAR[x][0]}} type='checkbox'>
            <label>{{SKILLS_SLOVAR[x][1]}}</label><br>
            % end
        </div>
    </div>
    <div>
        <button>
            Create!
        </button>
    </div>
</form>