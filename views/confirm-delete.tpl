% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'>
        <h1 class='element-title'>Confirm you wish to delete this entry</h1>
        <div class='grid-2x1'>
            <div class='box'>
                <a href='/'><button>No</button></a>
            </div>
            <div class='box'>
                <form action='/{{slovar}}-entry-delete/{{id}}/' method='POST'><input type='submit' value='Yes'></form>
            </div>
        </div>
    </div>
    % if slovar == 'wallet':
    <div class='grid-element col-2-2'>
        <h2>{{character.wallet[id][0]}}</h2>
        <div class='grid-2x1'>
            <div class='box'>DATE: <div class='box-field'>{{character.wallet[id][1]}}</div></div>
            <div class='box'>AMOUNT: <div class='box-field'>{{character.wallet[id][2]}}</div></div>
        </div>
        <div class='box-field'>
            {{character.wallet[id][3]}}
        </div>
    </div>
    % else:
    <div class='grid-element col-2-2'>
        <h2>{{character.diary[id][0]}}</h2>
        <div class='grid-2x1'>
            <div class='box'>DATE: <div class='box-field'>{{character.diary[id][1]}}</div></div>
        </div>
        <div class='box-field'>
            {{character.diary[id][2]}}
        </div>
    </div>
    % end
</div>