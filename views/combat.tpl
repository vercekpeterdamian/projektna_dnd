% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'><form action='/create-character/combat/' method='POST' style='margin: 0;'>
        <h1 class='element-title'>Combat </h1>
        <div class='box top-margin'>
            <h3 class='top-margin'>Insert required information about your combat abiliies.</h3>
            <label>Max HP:</label>
            <div class='box-field'><input name='max_hp' type='number' value="{{ 0 if uporabnik.nov_uporabnik else character.combat['max_hp'] }}"></div>
            <label>Inititive:</label>
            <div class='box-field'><input name='initiative' type='number' value="{{ 0 if uporabnik.nov_uporabnik else character.combat['initiative'] }}"></div>
            <label>Attack modifier:</label>
            <div class='box-field'><input name='attack_mod' type='number' value="{{ 0 if uporabnik.nov_uporabnik else character.combat['attack_mod'] }}"></div>
            <label>Armour class:</label>
            <div class='box-field'><input name='ac' type='number' value="{{ 0 if uporabnik.nov_uporabnik else character.combat['ac'] }}"></div>
            <label>Save DC:</label>
            <div class='box-field'><input name='save_dc' type='number' value="{{ 0 if uporabnik.nov_uporabnik else character.combat['save_dc'] }}"></div>
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