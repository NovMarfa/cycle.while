
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len (my_list):          # № индексов не вылезали за длину строки
    if my_list [num] > 0:
        print (my_list [num])
    elif my_list [num] < 0:
        break
    val = my_list[num]              # прописываем в основном цикле while
    num += 1

