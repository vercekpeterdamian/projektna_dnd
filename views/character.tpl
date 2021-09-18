% rebase('osnova.tpl')
% if uporabnik.nov_uporabnik:
<h1>Welcome {{uporabnik.uporabnisko_ime}}!</h1>
<p>
    I'm Dungeoneer, your personal D&D character manager! 
    This is my first edition so I'm not the most capable, but I'd love to help you in your campaign.
    Before we go any further you need to create your character!
</p>
<a href='/create-character/about/'>
    <input type='submit' value='Create your character'>
</a>
% else:
<div class='grid-container'>
    <div class='col-1-1 grid-element'>
        <div>
            <h1>
                Your character's sheet.
            </h1>
        <div>
        <div>
            <div>
                <h2>About</h2><br>
                <a href='/create-character/about/'><button>Edit</button></a>
            </div>
            <div>
                <table border="1">
                    <tr>
                        <td>
                            Name
                        </td>
                        <td>
                            {{character.name}}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Race
                        </td>
                        <td>
                            {{character.race}}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Subrace
                        </td>
                        <td>
                            {{character.subrace}}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Class
                        </td>
                        <td>
                            {{character.dclass}}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Subclass
                        </td>
                        <td>
                            {{character.dsubclass}}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Background
                        </td>
                        <td>
                            {{character.background}}
                        </td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    <div class='col-1-1 grid-element'>
        <div>
            <div>
                <h2>
                    Abilities
                </h2><br>
                <a href='/create-character/abilities/'><button>Edit</button></a>
            </div>
            <div>
                <table border="1">
                    <tr>
                        <td>
                            Ability
                        </td>
                        <td>

                        </td>
                        <td>
                            Ability mod
                        </td>
                        <td>
                            Saving mods
                        </td>
                    </tr>
                    % for x in range(6):
                    <tr>
                        <td>
                            {{ABILITIES_SLOVAR[x][1]}}
                        </td>
                        <td>
                            {{character.abilities[ABILITIES_SLOVAR[x][0]]}}
                        </td>
                        <td>
                            {{character.abilities_mods[ABILITIES_SLOVAR[x][0]]}}
                        </td>
                        <td>
                            {{character.saving_mods[ABILITIES_SLOVAR[x][0]]}}
                        </td>
                    </tr>
                    % end
                </table>
            </div>
        </div>
    </div>
    <div class='col-3-2 grid-element'>
        <div>
            <div>
                <h2>
                    Skills
                </h2><br>
                <a href='/create-character/skills/'><button>Edit</button></a>
            </div>
            <div>
                <table border="1">
                    <tr>
                        <td>
                            Skill
                        </td>
                        <td>
                            Skill modifier
                        </td>
                    </tr>
                    % for x in range(18):
                    <tr>
                        <td>
                            {{SKILLS_SLOVAR[x][1]}}
                        </td>
                        <td>
                            {{character.skills[SKILLS_SLOVAR[x][0]]}}
                        </td>
                    </tr>
                    % end
                </table>
            </div>
        </div>
    </div>
    <div class='col-2-2 grid-element'>
        <h1>
            Wallet
        </h1>
        <h2>
            Current ballance: {{character.financno_stanje}}
        </h2>
        <div>
            <h2>
                New wallet entry
            </h2>
        </div>
        <div>
            <form action='/wallet-entry/' method='POST'>
                <label>Title:</label>
                <input name='naslov' type='text'><br>
                <label>Amount</label>
                <input name='znesek' type='number' vlaue='0'><br>
                <label>Description</label><br>
                <textarea name='opis' rows='3', cols='50'></textarea><br><br>
                <button>
                    Make an entry!
                </button>
            </form>
        </div>
    </div>
    <div class='col-1-4 grid-element'>
        <div>
            % for id in wallet_ids:
                <div>
                    <div>
                        {{character.wallet[id][0]}}     DATE: {{character.wallet[id][1]}}     AMOUNT: {{character.wallet[id][2]}}
                    </div>
                    <div>
                        <form action='/confirm-delete/wallet/{{id}}/' method='GET'>
                            <button>Delete entry</button>
                        </form>
                    </div>
                </div>
                % if not character.wallet[id][3] == '':
                <div>
                    {{character.wallet[id][3]}}
                </div><br>
                % else:
                <br>
                % end
            % end
        </div>
    </div>
    <div class='col-2-2 grid-element'>
        <h1>
            Diary
        </h1>
        <div>
            <h2>
                New diary entry
            </h2>
        </div>
        <div>
            <form action='/diary-entry/' method='POST'>
                <label>Title:</label>
                <input name='naslov' type='text'><br>
                <label>Content</label><br>
                <textarea name='vsebina' rows='3', cols='50'></textarea><br><br>
                <button>
                    Make an entry!
                </button>
            </form>
        </div>
    </div>
    <div class='col-1-4 grid-element'>
        <div>
            % for id in diary_ids:
            <div>
                <div>
                    {{character.diary[id][0]}}     DATE: {{character.diary[id][1]}}
                </div>
                <div>
                    <form action='/confirm-delete/diary/{{id}}/' method='GET'>
                        <button>Delete entry</button>
                    </form>
                </div>
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
</div>
% end