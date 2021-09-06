% rebase('osnova.tpl')
% if character.name == '':
<h1>Welcome {{uporabnik.uporabnisko_ime}}!</h1>
<p>
    I'm Dungeoneer, your personal D&D character manager! 
    This is my first edition so I'm not the most capable, but I'd love to help you in your campaign.
    Before we even go any further you need to create your character!
</p>
<a href='/create-character/'>
    <button>
        Create your character
    </button>
</a>
% else:
<div>
    <h1>
        Your character's sheet.
    </h1>
    <div>
        <div>
            <h2>About</h2>
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
    <div>
        <div>
            <h2>
                Abilities
            </h2>
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
    <div>
        <div>
            <h2>
                Skills
            </h2>
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
<div>
    <div>
        <h1>
            Wallet
        </h1>
        <h2>
            Current ballance: {{character.financno_stanje}}
        </h2>
    </div>
    <div>
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
        <div>
            % for wallet_entry in character.wallet[::-1]:
            <button class='accordion'>{{wallet_entry[0]}} date: {{wallet_entry[1]}} amount: {{wallet_entry[2]}}</button>
            % if not wallet_entry == '':
            <div class='panel'>
                {{wallet_entry[3]}}
            </div><br>
            % else:
            <br>
            % end
        </div>
    </div>
</div>
% end