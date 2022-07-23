stock = {'커피': 15, '펜': 3, '종이컵': 20, '우유': 5, '콜라': 7, '라면': 20}
print("판매 전 재고:", stock)

product = input("판매할 물건을 입력하시오: ")
if product in stock.keys():
    stock[product] -= 1
print("판매 후 재고:", stock)