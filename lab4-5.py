dictionary = {}

inf = ['Фамилия призывника ', 'Имя призывника ', 'Отчество призывника ', 'Год рождения призывника ', 'Заболевание призывника ']
numbers = ['№1','№2','№3','№4','№5']

for i in range(5):
    for j in range(5):
        dictionary[inf[j] + numbers[i]] = input()

for key, value in dictionary.items():
    print(key, ":", value)