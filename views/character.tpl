% rebase('osnova.tpl')
% if character.name == '':
<h1>Welcome {{uporabnik.uporabnisko_ime}}!</h1>
<p>
    I'm Dungeoneer, your personal D&D character manager! 
    This is my first edition so I'm not the most capable, but I'd love to help you in your campaign.
    Before we even go any further you need to create your character!
</p>
<a href='/create_character/'>
    <button>
        Create your character
    </button>
</a>
% else:
<h1>AAAAAAAAAAAAAAAAAAAAA</h1>
% end