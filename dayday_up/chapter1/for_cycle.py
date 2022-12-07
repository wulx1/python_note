# -*- coding: utf-8 -*-
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"{fruit},i like it！")
print("i really like fruits!")

animals = ["dog", "cat", "bride"]
for animal in animals:
    print(f'{animal.title()}想成一只好的宠物！')
print("他们都是特别可爱的动物啊！")




def danshen():
    print("现在有优质男士吴龙兴，请问你选择他吗")
    str = input("现在有两个选择1是愿意，2是不愿意，请问你的选择是：")
    print("1.愿意")
    print("2.不愿意")
    if str == '1':
        print("恭喜你，你们在一起了！")
        cp.append("wulx&zzj")
    else:
        print("你虽然不愿意，但是他愿意！恭喜你们在一起了！哦耶")
        cp.append("wulx&zzj")


def not_marry():
    print("请再次确认是已婚男士/女士")
    print("不要欺骗自己，你是未婚的！请选择其他选择")

def marry():
    pass

def marry_marry():
    pass

def show_cp():
    print("当前的cp如下：")
    print(cp)

def over():
    if in_input == '6':
        exit()


if __name__ == '__main__':
    cp = []
    while True:
        print("---------欢迎来到恋爱系统-----------！")
        print("1.单身")
        print("2.未婚")
        print("3.已婚")
        print("4.不婚主义")
        print("5.查看当前的cp")
        print("6.退出系统！")
        in_input = input("请输入你的选择：")
        if in_input == '1':
            danshen()
        if in_input == '2':
            not_marry()
        if in_input == 3:
            pass
        if in_input == 4:
            pass
        if in_input == '5':
            show_cp()
