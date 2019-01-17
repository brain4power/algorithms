from collections import defaultdict


bd = defaultdict(list)
count = int(input('Введите количество предприятий от 1 и более: '))
for i in range(count):
    company_name = input(f'Введите {i + 1} наименование компании:')
    for j in range(4):
        profit = int(input(f'Введите доход {j + 1} квартала: '))
        bd[company_name].append(profit)

total_profit = sum(list(map(sum, bd.values())))

avg_profit_year = total_profit / len(bd)

less_avg = []
more_avg = []
for element in bd:
    if sum(bd[element]) > avg_profit_year:
        more_avg.append(element)
    if sum(bd[element]) < avg_profit_year:
        less_avg.append(element)

if more_avg:
    print('Предприятия, чья прибыль выше либо равна средней: ')
    for each in more_avg:
        print(each)
if less_avg:
    print('Предприятия, чья прибыль ниже средней: ')
    for each in less_avg:
        print(each)
