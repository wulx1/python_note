# -*- coding: utf-8 -*-



list1 = ((x,y)for x in range(1,6) for y in 'abcde'[x-1])
print(list1)
list2 = []
for i in list1:
    list2.append(i)
print(list2)
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)




if __name__ == '__main__':
    print("hello world!")