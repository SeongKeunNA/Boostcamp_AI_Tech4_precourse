line_count = 0
data_header = []
customer_list = []

with open ('customers.csv') as customer_data:
    while True:
        data = customer_data.readline()
        if not data: break
        if line_count == 0:
            data_header = data.split(',')
        else:
            customer_list.append(data.split(','))
        line_count += 1
print('Header : \t', data_header)
for i in range(10):
    print("Data", i,":\t\t", customer_list[i])
print(len(customer_list))