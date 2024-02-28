first_string = input()
second_string = input()
result = 'Да, первая строка содержит все символы второй строки'
for i in second_string:
    if i in first_string:
        continue
    else:
        result = 'Нет, первая строка не содержит все символы второй строки'
        break
print(result)
