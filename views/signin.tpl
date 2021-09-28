% rebase('osnova.tpl')
<div class='grid-center-element'>
    <div class='grid-element col-2-2'>
        <h1 class='element-title'>
            Sign in
        </h1>
        <div class='box'><form method="POST">
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
                <button>Sign in</button>
            </div>
        </form></div>
    </div>
</div>