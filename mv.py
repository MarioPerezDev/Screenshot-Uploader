import re
from robobrowser import RoboBrowser

browser = RoboBrowser(parser="lxml")
config = configparser.ConfigParser()

def login():
    browser.open("https://www.mediavida.com/login")
    login_form = browser.get_form(id='login_form')
    config.read('auth.ini')
    mv_username=config.get('mediavida', 'username')
    mv_password=config.get('mediavida', 'password')

    login_form["name"] = 'mv_username'
    login_form["password"] = 'mv_password'
    browser.submit_form(login_form)
    return browser

def postScreenshot(cuerpo):
    config.read('auth.ini')
    mv_thread=config.get('mediavida', 'screenshotsThreadURL')
    browser.open(mv_thread)
    post_form = browser.get_form(id='postear')
    post_form["cuerpo"] = "[spoiler=Nuevas Capturas]"+ cuerpo+ "[/spoiler]"
    browser.submit_form(post_form)
