import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# def normalize_phone(phone_number):
#     normalized = []
#     for index,char in enumerate(phone_number):
#         if char.isdigit() or char == '+' :
#             normalized.insert(index,char)
#     if normalized[0] != '+':
#         normalized.insert(0,'+')
#     if normalized[1] != '3':
#         normalized.insert(1,'3')
#     if normalized[2] != '8':
#         normalized.insert(2,'8')
#     if normalized[3] != '0':
#         normalized.insert(3,'0')  
#     return  ''.join(normalized)

# def normalize_phone(phone_number):
#     normalized = ''
#     pattern = r'[0-9]+'
#     res = re.findall(pattern, phone_number, re.IGNORECASE )
#     sliced = ''.join(res)[::-1][0:9:][::-1]
#     normalized = '+380' + sliced
#     return  normalized

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_number.startswith('+380'):
        return cleaned_number
    if cleaned_number.startswith('380'):
        return f'+{cleaned_number}'
    if not cleaned_number.startswith('+'):
        return f'+38{cleaned_number}'
    return cleaned_number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)