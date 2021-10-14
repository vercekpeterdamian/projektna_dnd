% rebase('osnova.tpl')
% if uporabnik.nov_uporabnik:
<div class='grid-center-element'>
    <div class='grid-element col-2-2'>
        <h1 class='element-title'>Welcome {{uporabnik.uporabnisko_ime}}!</h1>
        <div class='box'>
            <p>
                I'm Dungeoneer, your personal D&D character manager! 
                This is my first edition so I'm not the most capable, but I'd love to help you in your campaign.
                Before we go any further you need to create your character!
            </p>
            <a href='/create-character/about/'>
                <input type='submit' value='Create your character'>
            </a>
        </div>
    </div>
</div>
% else:
<div class='grid-main'>
    <div class='col-1-4'>
        <div class='grid-element'>
            <h1 class='element-title'>About</h1>
            <div class='grid-3x2_abt'>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Name:</h3>
                    <div class='box-field'>
                        {{character.name}}
                    </div>
                </div>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Race:</h3>
                    <div class='box-field'>
                        {{character.race}}
                    </div>
                </div>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Subrace:</h3>
                    <div class='box-field'>
                        {{character.subrace}}
                    </div>
                </div>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Class:</h3>
                    <div class='box-field'>
                        {{character.dclass}}
                    </div>
                </div>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Subclass:</h3>
                    <div class='box-field'>
                        {{character.dsubclass}}
                    </div>
                </div>
                <div class='box' style='padding-top: 0;'>
                    <h3 class='top-margin'>Background:</h3>
                    <div class='box-field'>
                        {{character.background}}
                    </div>
                </div>
            </div>
            <a href='/create-character/about/'><button>Edit</button></a>
        </div>
    </div>
    <div class='col-1-4 flex-container'>
        <div class='grid-element'>
            <h1 class='element-title'>
                Abilities
            </h1>
            <div class='grid-3x2'>
                % for x in range(6):
                <div class='box'>
                    <h3 class='element-title'>{{ABILITIES_SLOVAR[x][2]}}</h3>
                    <div class='box-field ability-no'>
                        {{character.abilities[ABILITIES_SLOVAR[x][0]]}}
                    </div>
                    <table class='ability-mods'>
                        <tr>
                            <td>{{character.abilities_mods[ABILITIES_SLOVAR[x][0]]}}</td>
                            <td>{{character.saving_mods[ABILITIES_SLOVAR[x][0]]}}</td>
                        </tr>
                    </table>
                </div>
                % end
            </div>
            <a href='/create-character/abilities/'><button>Edit</button></a>
        </div>
        <div class='grid-element'>
            <h1 class='element-title'>
                Skills
            </h1>
            <div class='box grid-2x9' style='padding: 10px;'>
                % for x in range(9):
                <div class='box-field'>
                    <div style='float: left;'>{{SKILLS_SLOVAR[x][1]}}</div>
                    <div style='float:right; margin-left: 5px;'>{{character.skills[SKILLS_SLOVAR[x][0]]}}</div>
                </div>
                <div class='box-field'>
                    <div style='float: left;'>{{SKILLS_SLOVAR[x+9][1]}}</div>
                    <div style='float:right; margin-left: 5px;'>{{character.skills[SKILLS_SLOVAR[x+9][0]]}}</div>
                </div>
                % end
            </div>
            <a href='/create-character/skills/'><button>Edit</button></a>                
        </div>
        <div class='grid-element'>
            <h1 class='element-title'>
                Combat
            </h1>
            <div class='grid-3x2_cmb'>
                % for x in range(6):
                <div class='box'>
                    <h3 class='element-title'>{{ COMBAT_SLOVAR[x][1] }}</h3>
                    <div class='box-field ability-no'>
                        {{ character.combat[COMBAT_SLOVAR[x][0]] }}
                    </div>
                </div>
                % end
            </div>
            <div class='box col-1-3' style="margin-top: 10px;"><form action='/combat/change-hp/' method='POST' style='margin: 0;'>
                <div class='grid-3x2_abt'>
                    <div class='col-1-2'>
                        <h3 style="margin: 0;">+/- HP</h3>
                    </div>
                    <div>
                        <button>Change</button>
                    </div>
                    <div>
                        <input name='change' type='number' value="0" style="width: 8ch;">
                    </div>
                    <div class='col-2-2'>
                        <input name='plusminus' type="radio" value="Taken">
                        <label>Taken</label>
                        <input name='plusminus' type='radio' value="Restored">
                        <label>Restored</label>
                    </div>
                </div>
            </form></div>
            <a href='/create-character/combat/'><button>Edit</button></a>  
        </div>
    </div>
    <div class='col-2-2 grid-element'>
        <h1 class='element-title'>
            Wallet
        </h1>
        <h2 style='margin: 10px 0'>
            Current ballance: {{character.financno_stanje}}
        </h2>
        <div class='box'>
            <h2 class='entry-title'>
                New wallet entry
            </h2>
            <form action='/wallet-entry/' method='POST'>
                <label>Title:</label>
                <input name='naslov' type='text'><br>
                <label>Amount:</label>
                <input name='znesek' type='number' vlaue='0'><br>
                <label>Description:</label><br>
                <textarea name='opis' rows='3' style="width: 100%;"></textarea><br><br>
                <button>
                    Make an entry!
                </button>
            </form>
        </div>
    </div>
    <div class='col-1-4 flex-container'>
        % for id in wallet_ids:
        <div class='grid-element' style='max-width: 400px;'>
            <h2 class='entry-title'>{{character.wallet[id][0]}}</h2>
            <div class='grid-3x1'>
                <div class='box'>DATE: <div class='box-field'>{{character.wallet[id][1]}}</div></div>
                <div class='box'>AMOUNT: <div class='box-field'>{{character.wallet[id][2]}}</div></div>
                <div class='box' style='padding: 17px;'>
                    <form action='/confirm-delete/wallet/{{id}}/' method='GET' style='margin: 0;'>
                        <button>Delete entry</button>
                    </form>
                </div>
            </div>
            <div class='box-field'>
                {{character.wallet[id][3]}}
            </div>
        </div>
        % end
    </div>
    <div class='col-2-2 grid-element'>
        <h1 class='element-title'>
            Diary
        </h1>
        <div class='box'>
            <h2>
                New diary entry
            </h2>
            <form action='/diary-entry/' method='POST'>
                <label>Title:</label>
                <input name='naslov' type='text'><br>
                <label>Content:</label><br>
                <textarea name='vsebina' rows='3' style="width: 100%;"></textarea><br><br>
                <button>
                    Make an entry!
                </button>
            </form>
        </div>
    </div>
    <div class='col-1-4 flex-container'>
        % for id in diary_ids:
        <div class='grid-element' style='max-width: 400px;'>
            <h2 class='entry-title'>{{character.diary[id][0]}}</h2>
            <div class='grid-2x1'>
                <div class='box'>DATE: <div class='box-field'>{{character.diary[id][1]}}</div></div>
                <div class='box' style='padding: 17px;'>
                    <form action='/confirm-delete/diary/{{id}}/' method='GET' style='margin: 0;'>
                        <button>Delete entry</button>
                    </form>
                </div>
            </div>
            <div class='box-field'>
                {{character.diary[id][2]}}
            </div>
        </div>    
        % end
    </div>
</div>
% end