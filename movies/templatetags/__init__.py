from typing import Iterator


def examp(func):
    value = {}
    def wrapp(a):
        
        if a not in value:
            
            value[a] = func(a)
        return value[a]
    return wrapp

@examp
def print_a(a):
    print('Func work')
    return(a * a)

print(print_a(4))

print(print_a(4))
print(print_a(5))
print(print_a(5))

iterator = {x if x%2 else 0 for x in range(5)}
print(iterator)


aaa = [1,2,3,4,5,6]

aaa = map(lambda x: x * 2 if x % 2 else x, aaa)
print(list(aaa))


list = [3,8,9,5,6,7,1,2]

def buble_sort(arr):
    for item1 in range(len(arr) - 1):
        for item in range(0, len(arr) -item1 - 1):
            if arr[item] > arr[item + 1]:
                template = arr[item]
                arr[item] = arr[item + 1]
                arr[item + 1] = template
    return arr

list = buble_sort(list)
print(list)


def binar_searct(arr,item):
    if item > arr[len(arr) // 2]:
        print('>')
        return binar_searct(arr[len(arr) // 2:], item)

    elif item < arr[len(arr) // 2]:
        print('<')
        return binar_searct(arr[:len(arr) // 2], item)

    elif item ==  arr[len(arr) // 2]:
        print('=')
        return item

print(binar_searct(list,5))
