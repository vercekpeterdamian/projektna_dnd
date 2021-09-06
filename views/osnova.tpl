<html>
    <head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>
			Dungeoneer
		</title>
		<style>
			body {
				background-image: url('ozadje.jpg');
			}
			h1, h2 {
				font-family: Georgia, 'Times New Roman', Times, serif;
				color: mediumvioletred;
			}
			.entry_title {
				font-family: Georgia, 'Times New Roman', Times, serif;
				color: navajowhite;
				background-color: black;
				padding: 1px;
			}
			.entry_content {
				background-color: bisque;
			}
			.levo {
				float: left;
				border: 2px blue
			}
			.desno {
				float: bottom right;
				border: 2px blue
			}
		</style>
    </head>
    <body>
		<nav>
    		<div>
				% if defined('uporabnik'):
        			<form method="POST" action="/signout/">
        				<button>
        					Sign out!!!
            			</button>
					</form>
				% else:
					<a href='/register/'>
						<button>
						  Register!!!
						</button>
				 	</a>
					<a href='/signin/'>
						<button>
							Sign in!!!
						</button>
					</a>
				% end
    		</div>
		</nav>
    	{{!base}}
    	<footer>© 2021, Peter Damian Verček</footer>
    </body>
</html>