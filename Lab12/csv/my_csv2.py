line_counter = 0
data_header = []
employee = []
customer_FRANCE_only_list = []
customer = None
with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\Lab12\\customers.csv", "r") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer = data.split(",")
            # 프랑스는 콤마로 구분할 경우 10번째 인덱스가 국가 명이 아님. IndexError
            # USA는 제대로 돌아감
            if customer[10].upper().strip() == 'FRANCE':
                customer_FRANCE_only_list.append(customer)
        line_counter += 1

print("Header:", data_header)
for i in range(0, 10):
    print("Data:", customer_FRANCE_only_list[i])
print(len(customer_FRANCE_only_list))

with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\Lab12\\customer_FRANCE_only.csv", "w") as customer_FRANCE_only_csv:
    for customer in customer_FRANCE_only_list:
        customer_FRANCE_only_csv.write(", ".join(customer).strip('\n') + "\n")