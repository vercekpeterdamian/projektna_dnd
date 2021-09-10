% rebase('osnova.tpl')
<form action='/create-character/about/' method='POST'>
    <div>
        <div>
            <p>
                Insert basic information about your character.
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