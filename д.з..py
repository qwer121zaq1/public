money = float(input("Введите сумму"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#  % = (money x %ставка) / 100
TKB = round((money * (per_cent['ТКБ'])/100), 2)
SKB = round((money * (per_cent['СКБ'])/100), 2)
VTB = round((money * (per_cent['ВТБ'])/100), 2)
SBER = round((money * (per_cent['СБЕР'])/100), 2)

deposit = [TKB, SKB, VTB, SBER]
deposit_list = list(deposit)
print(deposit)
print("Максимальное значение", max(deposit_list))
