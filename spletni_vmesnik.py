import bottle
from model import Uporabnik
from datetime import date

PISKOTEK_UPORABNISKO_IME = 'User_cookies'
SKRIVNOST = 'moja macka Mufi'

def shrani_stanje(uporabnik):
    uporabnik.v_datoteko()


def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie(
        PISKOTEK_UPORABNISKO_IME, secret=SKRIVNOST
    )
    if uporabnisko_ime:
        return podatki_uporabnika(uporabnisko_ime)
    else:
        bottle.redirect('/signin/')


def podatki_uporabnika(uporabnisko_ime):
    return Uporabnik.iz_datoteke(uporabnisko_ime)


@bottle.get('/')
def osnovni_zaslon():
    bottle.redirect('/character/')


@bottle.get('/register/')
def registracija_get():
    return bottle.template('register.tpl', napaka=None)


@bottle.post('/register/')
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('username')
    geslo_v_cistopisu = bottle.request.forms.getunicode('password')
    if not uporabnisko_ime:
        return bottle.template('register.tpl', napaka='Enter a username!')
    try:
        Uporabnik.registracija(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path='/', secret=SKRIVNOST
        )
        bottle.redirect('/')
    except ValueError as e:
        return bottle.template('register.tpl', napaka=e.args[0])


@bottle.get('/signin/')
def prijava_get():
    return bottle.template('signin.tpl', napaka=None)


@bottle.post('/signin/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('username')
    geslo_v_cistopisu = bottle.request.forms.getunicode('password')
    if not uporabnisko_ime:
        return bottle.template('signin.tpl', napaka='Enter your username!')
    try:
        Uporabnik.prijava(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path='/', secret=SKRIVNOST
        )
        bottle.redirect('/')
    except ValueError as e:
        return bottle.template('signin.tpl', napaka=e.args[0])


@bottle.post('/signout/')
def odjava():
    bottle.response.delete_cookie(PISKOTEK_UPORABNISKO_IME, path='/')
    bottle.redirect('/')

@bottle.get('/character/')
def character_homepage():
    uporabnik = trenutni_uporabnik()
    return bottle.template('character.tpl', character=uporabnik.character, uporabnik=uporabnik)

@bottle.get('/create-character/')
def create_character_get():
    return bottle.template('create-character.tpl')

@bottle.post('/create-character/')
def create_character_post():

bottle.run(debug=True, reloader=True)