my_d = {'Ana':{'mq':[10], 'ps':[10,10]},
        'Bob':{'ps':[7,8], 'mq':[8]},
        'Eric':{'mq':[3], 'ps':[0]} }

def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]
    
    return sum(all_data)/len(all_data)

print(get_average(my_d, "mq"))