from pprint import pprint
cook_book = {}
with open('name.txt', encoding='utf-8') as f:
    file = f.read().split('\n\n')
    #print(file)
name_list = ['ingredient_name', 'quantity', 'measure']
for elem in file:
    l = elem.split('\n')
    cook_book[l[0]] = []
    for i in range(2,len(l)):
        ing = l[i].split(' | ')
        ing[1] = int(ing[1])
        cook_book[l[0]].append(dict(zip(name_list,ing)))
        #print(ing)
pprint(cook_book)

# Задача № 2

def get_shop_list_by_dishes(dishes, person_count):
    dict = {}

    for dish in dishes:
        for i in range(len(cook_book[dish])):
            ing = cook_book[dish][i]['ingredient_name']
            if ing not in dict.keys():
                dict[ing] = {}
                dict[ing]['measure'] = cook_book[dish][i]['measure']
                dict[ing]['quantity'] = cook_book[dish][i]['quantity']* person_count
            else:

                dict[ing]['quantity'] += cook_book[dish][i]['quantity'] * person_count

    pprint(dict)

print('----------------------------')
get_shop_list_by_dishes(['Омлет','Фахитос'], 2)
print('----------------------------')

# Задача № 3
a = ['1.txt', '2.txt', '3.txt']
l = []
for i in a:
    with open(i, encoding='utf-8') as f:
        list = [i]
        file = f.read().split('\n')
        list.append(str(len(file)))
        list.extend(file)
        l.append(list)
        l.sort(key=len)

#print(l)


with open('4.txt', 'a', encoding='utf-8') as f:
    for i in l:
        for j in i:
          f.write(j)
          f.write('\n')







