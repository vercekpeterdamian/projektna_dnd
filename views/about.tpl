% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'><form action='/create-character/about/' method='POST' style='margin: 0;'>
        <h1 class='element-title'>About</h1>
        <div class='box'>
            <h3 class='top-margin'>Insert basic information about your character.</h3>
            <label>Name:</label>
            <div class='box-field'><input name="ch_name" type="text" placeholder="name"></div>
            <label>Race:</label>
            <div class='box-field'><input name="ch_race" type="text" placeholder="race"></div>
            <label>Subrace:</label>
            <div class='box-field'><input name="ch_subrace" type="text" placeholder="subrace"></div>
            <label>Class:</label>
            <div class='box-field'><input name="ch_class" type="text" placeholder="class"></div>
            <label>Subclass:</label>
            <div class='box-field'><input name="ch_subclass" type="text" placeholder="subclass"></div>
            <label>Background:</label>
            <div class='box-field'><input name="ch_background" type="text" placeholder="background"></div>
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