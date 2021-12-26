import json

with open('data7.json', 'w+') as firm_data_j:
    with open('data7.txt', 'r', encoding='utf-8') as firm_data:
        profit_f = {line.split()[0]: int(line.split()[2]) for line in firm_data if int(line.split()[2]) > int(line.split()[3])}
        mid_p = round(sum(profit_f.values()) / len(profit_f))
        res_dict = [profit_f, {'средняя выручка': mid_p}]
        json.dump(res_dict, firm_data_j, ensure_ascii=False, indent=3)



