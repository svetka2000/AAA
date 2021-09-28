import csv
from functools import reduce

def printhierarchyofcomands(data: list): #Вывести в понятном виде иерархию команд, 
    #т.е. департамент и все команды, которые входят в него
    departmentscommands=[]#list кортежей (департамент, команда) c повторами
    departments=[]#list департаментов c повторами
    curentcomand, commands_=[],[] #промежуточные листы
    commands=[]#list листов формата [департамент, [", ".join(команды)]]
    makedepartmentscommands(data, departmentscommands, departments)
    #делаем list кортежей (департамент, команда) c повторами
    #делаем list департаментов c повторами
    makecommands(departments, departmentscommands, commands, curentcomand)
    #формируем list листов формата [департамент, [", ".join(команды)]]
    for i in commands:#пробегаем по list листов формата [департамент, [", ".команды)]] и печатаем их
        department = i[0]
        commands_ = ", ".join(i[1])
        print(f'В департаменте {department} находятся команды: {commands_}.')


def makedepartmentscommands(data:list, departmentscommands:list, departments:list):
    for person in data[1:]: #пробегаем по данным, считывам данные людей
         departmentscommands.append((person[1], person[2])) #делаем list кортежей (департамент, команда)
         departments.append(person[1])#делаем list департаментов


def makecommands(departments: list, departmentscommands: list, commands: list, curentcomand: list):
    #формируем list листов формата [департамент, [", ".команды)]]
    for department in list(set(departments)):#пробегаем по уникальным департаментам
        for command in list(set(departmentscommands)):#пробегаем по list кортежей (департамент, команда)
            if command[0] == department: #если в кортеже (департамент, команда) департамент 
                #совпадает с тем, что мы пробегаем в цикле
                if not set(command[1]).issubset(set(curentcomand)):#если мы ещё не встречали такую команду
                    curentcomand.append(command[1])#добавляем команду в список соответствующих команд
        commands.append([department, curentcomand])#формируем list листов формата [департамент, [", ".команды)]]
        curentcomand=[]#обнуляем текующая команду, чтобы перейти к следующему департаменту


def makefreereport(data: list) -> list:#составляем отчёт
    departmentscommands=[]#list кортежей (департамент, команда) c повторами
    departments=[]#list департаментов c повторами
    currentnumber=0#счётчик для численности в департаменте
    currentcosts=[]#зарплаты в департаменте
    report=[]#list с отчётом
    makedepartmentscommands(data, departmentscommands, departments)
    #делаем list кортежей (департамент, команда) c повторами
    #делаем list департаментов c повторами
    for department in list(set(departments)):#бежим по департаментам
        for person in data:#смотрим базу людей
            if person[1]==department:
                currentnumber+=1#считаем людей в департаменте, где мы находимся
                currentcosts.append(int(person[5]))#записываем зарплату каждого в этом департаменте
        #вносим данные в отчёт
        report.append([department, #департамент
                    currentnumber, #численностьь сотрудников
                    min(currentcosts), #минимальная зарпалата
                    max(currentcosts), #максимальная зарплата
                    round(reduce(lambda x, y: x + y, currentcosts) /currentnumber, 3)
                    #средняя, округлённая до 3 знаков
                    ])
        currentnumber=0#переходим в следующий департамент
        currentcosts=[]
    return report


def printfreereport(data: list):#выводим отчёт в консоль
    report = makefreereport(data)#пишем отчёт
    for itemofreport in report:#пробегаем каждую строку отчёта
        department = itemofreport[0]
        numberempl = itemofreport[1]
        maxcost = itemofreport[2]
        mincost = itemofreport[3]
        average = itemofreport[4]
        print(f'Название: {department};\nЧисленность: {numberempl};\n' 
        f'"Вилка" зарплат: {mincost}-{maxcost};\nСредняя зарплата: {average};\n ')


REPORT_HEADER_FIELDS = (#заголовки для файла с отчётом
    'Департамент',
    'Численность департамента',
    '"Вилка" зарплат',
    'Средняя зарплата',
)

def savefreereport(data: list):#сохраняем отчёт в файлик
    report = makefreereport(data)#пишем отчёт
    with open('./report.csv', 'w') as f:#открываем файлик
        out_file = csv.writer(f, delimiter=';')#говорим, как будем писать в файлик
        out_file.writerow(REPORT_HEADER_FIELDS)#пишем заголовки 
        for department, numberempl, mincost, maxcost, average in report:#пишем в файлик отчёт
            out_file.writerow((
                department,
                numberempl,
                f'{mincost}-{maxcost}',
                average
            ))


def takedata() -> list: #функция открывает файл и считывает данные
    with open('Corp Summary.csv', newline='\n') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        data =[row for row in file] #данные -
        #кортежи формата ['ФИО полностью', 'Департамент', 'Отдел', 'Должность', 'Оценка', 'Оклад']
        return data


def consol(data: list):
    print(
        'Хотите?\n'
        '1) Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n'
        '2) Вывести сводный отчёт по департаментам: название, численность,' 
        '"вилка" зарплат в виде мин – макс, среднюю зарплату\n'
        '3) Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. '
        'При этом необязательно вызывать сначала команду из п.2)\n'
    )
    option = ''
    options = {'1)': 1, '2)': 2, '3)': 3, '0': 0}
    while option not in options:
        print('Выберите: {}, или {}, или {}, или 0, чтобы выйти'.format(*options))
        option = input()
    if options[option]==1:
        return printhierarchyofcomands(data)
    if options[option]==2:
        return printfreereport(data)
    if options[option]==3:
        return savefreereport(data)
    if options[option]==0:
        return 0


if __name__ == '__main__':
    data = takedata()
    while 1:
        if consol(data)==0:
            break

