% rebase('osnova.tpl')
<div>
    <h1>
        Sign in
    </h1>
</div>
<div>
    <form method="POST">
        <div>
            <label >Username</label>
            <div>
                <input class="input" name="username" type="text" placeholder="username">
            </div>
            % if napaka:
            <p>{{ napaka }}</p>
            % end
        </div>
        <div>
            <label>Password</label>
            <div>
                <input class="input" name="password" type="password" placeholder="password">
            </div>
        </div>
        <div>
            <div>
                <button>Sign in</button>
            </div>
        </div>
        <div>

        </div>
    </form>
</div>