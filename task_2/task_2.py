import random
# def get_numbers_ticket(min, max, quantity):
#     winners_list = []
#     if min <= 0:
#         print('Minimal number value  must be more than 0 ')
#         return 
#     if max > 1000:
#         print('Maximum number value  must be less than 1000 ')
#         return 
#     for i in range(0,quantity):
#         random_winner = random.randint(min,max)
#         if random_winner in winners_list:
#             random_winner = random.randint(min,max)
#         winners_list.insert(i,random_winner)  
#     return winners_list 
# result = get_numbers_ticket(1,1000,5)
# print(result)

def get_numbers_ticket(min, max, quantity):
    winners_list = []
    if min <= 0:
        print('Minimal number value  must be more than 0 ')
        return 
    if max > 1000:
        print('Maximum number value  must be less than 1000 ')
        return
    try:
        winners_list = random.sample(range(min, max), quantity)
    except ValueError:
        print('Sample size exceeded population size.')
        return
    return winners_list 
   
result = get_numbers_ticket(10, 11, 6)
print(result)
