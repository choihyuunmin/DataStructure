coin_list = [1000, 500, 100, 10]

def get_coin_min_value(value, coin_list):
    total_coin_count = 0
    result = list()
    coin_list.sort(reverse=True)
    
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        result.append([coin, coin_num])
        
    return total_coin_count, result


print(get_coin_min_value(4720, coin_list))



#-------------------------------------------------------------------------------------------------------


data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def greedy_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    result = list()
    
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            result.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            result.append([data[0], data[1], fraction])
            break
    
    return total_value, result


print(greedy_value(data_list, 30))