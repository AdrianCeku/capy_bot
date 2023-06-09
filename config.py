import random

db_host = "localhost"
db_username = "capybot"
db_password = "capybot"
db_name = "capybot"


def capytime():
    if random.randrange(0, 100) > 98:
        return random.choice(contents['rarecapybaras'])
    return random.choice(contents['capybaras'])


contents = {
    'capybaras': (
        'https://media.tenor.com/5iFCl5T2WTkAAAAd/capybara-capybara-eating.gif',
        'https://media.tenor.com/HiIDwBWm28oAAAAd/cappy.gif',
        'https://media.tenor.com/e1Dz6IwQ-VEAAAAd/chifast-capy.gif',
        'https://media.tenor.com/cGV_IH4FefkAAAAd/capybara-haircut.gif',
        'https://media.tenor.com/yrclV_1mAgQAAAAC/capybara-capybara-ok-i-pull-up.gif',
        'https://media.tenor.com/B4JWdMKGfQQAAAAS/capybara-meme.gif',
        'https://media.tenor.com/K3uxrqffdCAAAAAC/capybara-orange.gif',
        'https://media.tenor.com/M8NEtEBrrIkAAAAC/capybara-infested-chat-capybara.gif',
        'https://media.tenor.com/hX9renH-K_YAAAAC/capibara.gif',
        'https://media.tenor.com/1kZ2j73pGDUAAAAd/capybara-ok-he-pull-up.gif',
        'https://media.tenor.com/JN3qS44yAZsAAAAS/capybara.gif',
    ),

    'rarecapybaras': (
        'https://media.tenor.com/jtF14XYTQmIAAAAd/capybara-capybara-ok-i-pull-up.gif',
    ),

    'games': (
        'Roblox',
        'Fortnite',
        'Among Us',
        'Minecraft',
        'Hello Kitty Online',
        'Microsoft Store',
        'Epic Games',
        'Orc Massage'
    )
}

messages = {
    'hello': 'hello',
    'chromosom': 'mehr als du, du hs',
    'capytime': capytime,
    'capybara': capytime,
    'ich liebe fortnite': 'für fortnite',
    'will jemand roblox spielen?': '...',
    'sullivan': '❤️🤤🥵🤤❤️ SULLIVAN 💗🍆🍆🍆💗 oh sulley 💕💕💕',
    'cbt': "Ich liebe CapyBaraTherapy 😍😍",
}
