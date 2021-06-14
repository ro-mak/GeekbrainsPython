firm_file = open("task7.txt")
result_list = []
firm_dict = dict()
profit_dict = dict()
for line in firm_file:
    firm_info = line.split()
    firm_name = firm_info[0]
    firm_gain = int(firm_info[2])
    firm_loss = int(firm_info[3])
    firm_profit = firm_gain - firm_loss
    firm_dict[firm_name] = firm_profit
total_profit = 0
profited_firms_count = 0
for firm_profit_str in firm_dict.values():
    firm_profit_int = int(firm_profit_str)
    if firm_profit_int > 0:
        profited_firms_count += 1
        total_profit += firm_profit_int
profit_dict["average_profit"] = total_profit / profited_firms_count
result_list.append(firm_dict)
result_list.append(profit_dict)
print(result_list)
