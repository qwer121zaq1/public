price_big = 1390
price_middle = 990
price_smal = 0
sum_all = 0

ppl = int(input('введите количество билетов: '))
number_of_ppl = [i for i in range(ppl)]
for age_id in number_of_ppl:
    age = int(input('введите возраст слушателя: '))
    if age < 18:
        print('вход свободный')
        sum_all += price_smal
    elif 18 <= age <= 25:
        print('цена билета: ', price_middle)
        sum_all += price_middle
    else:
        print('цена билета: ', price_big)
        sum_all += price_big
if len(number_of_ppl) > 3:
    print('группа больше 3х человек скидка 10%')
    sum_all -= sum_all * 0.1
print('ваш заказ составил: ', sum_all)