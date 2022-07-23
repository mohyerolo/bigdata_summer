def exchange(m, c):
    global country_list
    global unit
    global rate

    if c in country_list:
        i = country_list.index(c);
        print("%d원은 %.2f%s입니다" %(m, (m / rate[i]), unit[i]))
    else: print("해당 국가 정보가 없습니다")
    
country_list = ['미국', '중국', '유럽', '일본', '영국']
unit = ['달러', '위안', '유로', '엔', '파운드']
rate = [1270.50, 189.44, 1345.21, 975.36, 1571.67]

money1 = int(input("환전 금액(원)을 입력하세요: "))
country = input("국가를 입력하세요: " )
exchange(money1, country)