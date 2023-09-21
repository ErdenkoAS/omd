# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print("Утка-маляр 🦆 взяла зонтик и пошла в бар. Там она встретила другую утку. "
          "Предложить другой утке сыграть в игру? 🎲")
    options = {'да': True, 'нет': False}
    option = ''
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print("Утки-маляры 🦆🦆 сыграли в игру и прекрасно провели время вместе!")
    else:
        print("Утка-маляр 🦆 продолжила выпивать одна и размышлять о своей жизни.")


def step2_no_umbrella():
    print("Утка-маляр 🦆 пошла в бар без зонтика. Внезапно начался дождь. "
          "Попросить у прохожего одолжить зонтик? ☂️")
    options = {'да': True, 'нет': False}
    option = ''
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print("Утка-маляр 🦆 попросила зонтик у прохожего и благодаря этому добралась до бара сухой.")
        print("В баре она встретила своих друзей, и они вместе хорошо провели время!")
    else:
        print("Утка-маляр 🦆 промокла и заболела. На следующий день она решила остаться дома и выздоравливать.")

if __name__ == '__main__':
    step1()

