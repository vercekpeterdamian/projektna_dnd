<html>
    <head>
    	<title>
			Dungeoneer
		</title>
		<style>
			.accordion {
				background-color: aquamarine;
				padding: 5px;
			}

			.active, .accordion:hover {
				background-color: mediumaquamarine;
			}

			.panel {
				padding: 0;
				background-color: mediumpurple;
			}
		</style>
    </head>
    <body>
		<nav>
    		<div>
        		<a href='/register/'>
          			<button>
        				Register!!!
	      			</button>
    	    	</a>
        		<form method="POST" action="/signout/">
        			<button>
        				Sign out!!!
            		</button>
    			</form>
    		</div>
		</nav>
    	{{!base}}
    	<footer>© 2021, Peter Damian Verček</footer>
    </body>
</html>