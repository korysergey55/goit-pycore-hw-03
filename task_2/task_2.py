import random

def get_numbers_ticket(min, max, quantity):
    winners_list = []
    if min <= 0:
        print('Minimal number value  must be more than 0 ')
    if max > 1000:
        print('Maximum number value  must be less than 1000 ')
        return winners_list
    for i in range(0,quantity):
        random_winner = random.randint(min,max)
        if random_winner in winners_list:
            random_winner = random.randint(min,max)
        winners_list.insert(i,random_winner)  
    return winners_list 
result = get_numbers_ticket(1,100,5)
print(result)

l = [1,2,3,4,5,6,7,8,9]
slice_l = l[0:5]
print(slice_l)