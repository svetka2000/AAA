def step3_umbrella_change():
    print(
        'Кайф!\n'
        'Жизнь утки-маляра заиграла новыми красками🤪')
    return 0
    
def step3_umbrella_no_change():
    print('Ну и правильно, в зонтик больше жидкостей поместится🥳')
    return 0

def step3_no_umbrella_beer():
    print('Лучшее решение найдено! Cheers!😊')
    return 0

def step3_no_umbrella_no_beer():
    print('Ну что ж... No woman, no cry...🤓')
    return 0

def step2_umbrella():
    print(
        'А зачем это ей зонтик, она же не сахарная!\n'
        'Обменять в баре у сахарной утки зонтик на кисточку для красок?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_umbrella_change()
    return step3_umbrella_no_change()

def step2_no_umbrella():
    print('Лучше пива?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_no_umbrella_beer()
    return step3_no_umbrella_no_beer()

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

if __name__ == '__main__':
    step1()