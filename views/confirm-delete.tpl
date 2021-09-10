% rebase('osnova.tpl')
<div>
    <div>
        <h1>Confirm you wish to delete this entry</h1>
        <a href='/'><button>No</button></a>
        <form action='/{{slovar}}-entry-delete/{{id}}/' method='POST'><input type='submit' value='Yes'></form>
    </div>
    <div>
    % if slovar == 'wallet':
        <div>
            {{character.wallet[id][0]}}     DATE: {{character.wallet[id][1]}}     AMOUNT: {{character.wallet[id][2]}}
        </div>
        % if not character.wallet[id][3] == '':
        <div>
            {{character.wallet[id][3]}}
        </div><br>
        % else:
        <br>
        % end
    % else:
        <div>
            {{character.diary[id][0]}}     DATE: {{character.diary[id][1]}}
        </div>
        % if not character.diary[id][2] == '':
        <div>
            {{character.diary[id][2]}}
        </div><br>
        % else:
        <br>
        % end
    % end
    </div>
</div>