<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="/static/dungeoneer.css">
	<link rel="icon" type="image/png" sizes="32x32" href="/static/icons/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="/static/icons/favicon-16x16.png">
	<title>
		Dungeoneer
	</title>
</head>
<body>
<nav>
	<div class='grid-main grid-element'>
		<div class='box col-1-2'>
			<a href="/">
				<img src='/static/main_logo.png' alt='Main logo' max-width='100%' height='100'>
			</a>
		</div>
		% if defined('uporabnik'):
		<div class='box col-3-2'>
    		<form method="POST" action="/signout/">
				<button>
    				Sign out
        		</button>
			</form>
		</div>
		% else:
		<div class='box col-3-2'>
			<div class='box'>
				<a href='/register/'>
					<button>
						Register
					</button>
				</a>
			</div>
			<div class='box'>
				<a href='/signin/'>
					<button>
						Sign in
					</button>
				</a>
			</div>
		</div>
		% end
	</div>
</nav>
{{!base}}
<footer>© 2021, Peter Damian Verček</footer>
</body>
</html>