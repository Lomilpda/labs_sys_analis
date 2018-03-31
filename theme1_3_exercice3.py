import random
#buy = int(input("Цена покупки"))
#sell = int(input("Цена продажи"))
#remain = int(input("Цена продажи остатков"))
buy = 390   #вариант 14, Соляника
sell = 700
remain = 150
quantity_list = [[100, 0.2], [150, 0.25], [200, 0.3], [250, 0.15], [300, 0.1]]  #Это была плохая идея
total_buy_list = []
total_sell_list = []
remain_sell_list = []
possibility_remain_list = []
balance_list = []
remain_quantity_list = []    #список кол-ва непроданных сразу товаров
i = 0
while i < len(quantity_list):     #заполняем массивы, которые будем обрабатывать
    buy_summ = buy*quantity_list[i][0]
    total_buy_list.append(buy_summ)
    sell_summ = sell*quantity_list[i][0]*quantity_list[i][1]
    total_sell_list.append(sell_summ)
    possibility_remain = 1-quantity_list[i][1]      #если не продали сразу, значит продадим потом (с)
    possibility_remain_list.append(possibility_remain)
    remain_summ = remain*quantity_list[i][0]*possibility_remain_list[i]
    remain_sell_list.append(remain_summ)
    remain_quantity = quantity_list[i][0]-sell_summ/sell    #кол-во остатков
    remain_quantity_list.append(remain_quantity)
    """
    <1C mode on>
    БАЛАНС = ЦЕНА_ПРОДАЖИ*КОЛ-ВО*ВЕРОЯТНОСТЬ_ПРОДАЖИ+
    +ЦЕНА_ПРОДАЖИ_ОСТАТКОВ*КОЛ-ВО*(1-ВЕРОЯТНОСТЬ_ПРОДАЖИ)-ЦЕНА_ПОКУПКИ*КОЛ-ВО
    </1C mode off>
    """
    formule_principal = (remain_sell_list[i]+total_sell_list[i]-total_buy_list[i])  #см. расшифроку ф-лы выше
    balance_list.append(formule_principal)
    if formule_principal == max(balance_list):
        optimal_quantity = quantity_list[i][0]     #записываем оптимальное кол-во товара
        remain_quantity_year = remain_quantity_list[i]
        index = i
    print("При закупке ", quantity_list[i][0], " ед. товара")
    print("Затраты на покупку ", total_buy_list[i])
    print("Выручка за продажу ", total_sell_list[i])
    print("Выручка за продажу остатков ", remain_sell_list[i])
    print("Итоговый баланс ", balance_list[i], "\n")
    i += 1
print("Наибольшая прибыль ", max(balance_list), "при закупке", optimal_quantity, "ед. товара",
      "Запас, шт:"+" ", remain_quantity_year)
def second_year(remain_quantity_year):  #вычисление решения по закупке на 2-ой год
    if remain_quantity_year == 0:
        optimal_next_year = optimal_quantity
    elif remain_quantity_year > 0:
        try:
            optimal_next_year = random.randrange(index)
        except ValueError:      #если index = 0
            optimal_next_year = 0
    else:
        optimal_next_year = random.randrange(index, 5)
    return optimal_next_year
prognos_quantity =  quantity_list[second_year(remain_quantity_year)]
print("Оптимальное кол-во товара для закупки на следующий год:"+"",
      prognos_quantity[0],
      "шт")
input()

