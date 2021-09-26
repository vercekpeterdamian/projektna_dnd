<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="/static/dungeoneer.css">
	<title>
		Dungeoneer
	</title>
</head>
<body>
<nav>
	<div>
		<img src='/static/main_logo.png' alt='Main logo' width='400' height='100'>
	</div>
	<div>
		% if defined('uporabnik'):
    	<form method="POST" action="/signout/">
			<button>
    			Sign out
        	</button>
		</form>
		% else:
		<a href='/register/'>
			<button>
				Register
			</button>
		</a>
		<a href='/signin/'>
			<button>
				Sign in
			</button>
		</a>
		% end
	</div>
</nav>
{{!base}}
<!--<footer>© 2021, Peter Damian Verček</footer>-->
</body>
</html>