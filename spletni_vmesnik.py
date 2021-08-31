import bottle
import model

CHARACTERS = {}

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('homepage.tpl')

@bottle.post('/create_character/')
def character_creation_post():
    ch_name = bottle.request.forms['ch_name']
    if ch_name not in CHARACTERS.keys():
        return bottle.template('/create_character_info/', ch_name=ch_name)
    else:
        return bottle.template('/')

@bottle.get('/create_character_info/')
def character_creation_info_post():
    return bottle.template('create_character')

@bottle.post('/cci-post/')
def cci_post():
    CHARACTERS[-1].race = bottle.request.forms['ch_race']
    CHARACTERS[-1].subrace = bottle.request.forms['ch_subrace']
    CHARACTERS[-1].dclass = bottle.request.forms['ch_class']
    CHARACTERS[-1].dsubclass = bottle.request.forms['ch_subclass']
    CHARACTERS[-1].background = bottle.request.forms['ch_background']
    bottle.redirect('/')

bottle.run(debug=True, reloader=True)