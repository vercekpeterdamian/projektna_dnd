% rebase('osnova.tpl')
<form method="POST">
    <div>
        <label >Username</label>
        <div>
            <input class="input" name="username" type="text" placeholder="username">
            <span>
                <i></i>
            </span>
        </div>
        % if napaka:
        <p>{{ napaka }}</p>
        % end
    </div>
    <div>
        <label>Password</label>
        <div>
            <input class="input" name="password" type="password" placeholder="password">
            <span>
                <i></i>
            </span>
        </div>
    </div>
    <div>
        <div>
            <button>Sign in</button>
        </div>
    </div>
</form>