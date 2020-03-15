import heapq
import random
import time

tab = [1, 2, 7, 5, 9, 2, 4, 1, 1, 4, 5, 3, 1000000000, 1000000000]


def random_generator(liczba: int):
    lista = []
    g = 0
    for i in range(liczba):
        lista.append(i)
        g += 1
        random.shuffle(lista)

    return lista


def insert_sort(unsorted_tab):
    sorted_tab = [0]

    for unsorted_num in unsorted_tab:
        for index, sorted_num in enumerate(sorted_tab):
            if unsorted_num > sorted_num:
                sorted_tab.insert(index, unsorted_num)
                break
    sorted_tab = sorted_tab[::-1]
    return sorted_tab[1:]


# print(insert_sort(tab))


def insert_sort_2(source):
    sorted_table = []
    wstaw = 0

    for wstawiony in source:
        for index, y in enumerate(sorted_table):
            if wstawiony < y:
                wstaw = index
                break
            elif index == len(sorted_table) - 1:
                wstaw = index + 1

        sorted_table.insert(wstaw, wstawiony)
    return sorted_table




def one_list_sort(source):
    for i in range(len(source)):
        for j in range(i):
            if source[i] < source[j]:
                source.insert(j, source.pop(i))

    return source


def one_list_sort_enumerate(source):
    for index, i in enumerate(source):
        for index1, j in enumerate(source):
            if i < j:
                indeks = index1
                source.insert(index1, source.pop(index))
                break
    return source


def min_max_sort(source):
    for iterator in range(len(source)):
        maksi = int()
        for iterowana in source[:(len(source) - iterator)]:
            if iterowana > maksi:
                maksi = iterowana
        source.remove(maksi)
        source.insert(len(source) - iterator, maksi)
    return source


def min_max_sort_2(source):
    for iterator in range(len(source)):
        maksi = source[0]
        for iterowana in source[:(len(source) - iterator)]:
            if iterowana > maksi:
                maksi = iterowana
        source.remove(maksi)
        source.insert(len(source) - iterator, maksi)
    return source

def quick_sort(source):
    tab_small = []
    tab_big = []
    pivot_tab = []
    if len(source) <= 1:
        return source
    else:
        pivot = source[len(source) // 2]
        source.pop(len(source) // 2)
        pivot_tab.append(pivot)
    for i in source:
        if i < pivot:
            tab_small.append(i)
        else:
            tab_big.append(i)

    return quick_sort(tab_small) + pivot_tab + quick_sort(tab_big)


def heap_sort(lista):
    heapq.heapify(lista)
    lista_sorted=[heapq.heappop(lista) for i in range(len(lista))]
    return lista_sorted



lista = random_generator(100)
lista1=lista

start = time.time()
min_max_sort(lista1)
end = time.time()
print(f'min max sort {end - start}')

random.shuffle(lista)

start = time.time()
one_list_sort_enumerate(lista)
end = time.time()
print(f'one list sort enumerate  {end - start}')

random.shuffle(lista)

start = time.time()
one_list_sort(lista)
end = time.time()
print(f'one list sort{end - start}')

random.shuffle(lista)

start = time.time()
insert_sort(lista)
end = time.time()
print(f'insert sort {end - start}')

random.shuffle(lista)

start = time.time()
insert_sort_2(lista)
end = time.time()
print(f'insert sort 2 {end - start}')

random.shuffle(lista)

start = time.time()
quick_sort(lista)
end = time.time()
print(f'quick sort  {end - start}')


random.shuffle(lista)
start = time.time()
heap_sort(lista)
end = time.time()
print(f'heap sort {end - start}')


random.shuffle(lista)
start = time.time()
lista.sort()
end = time.time()
print(f'quick sort builtin {end - start}')
