# -*- coding: utf-8 -*-
want_worldcity = ['北京', '山海', '厦门', '大理', '重庆']

print("wulx想去的城市", want_worldcity)
city1 = sorted(want_worldcity)
print("使用sorted方法后打印的顺序：", city1)
city2 = sorted(want_worldcity, reverse=True)
print("列表翻转打印：", city2)
want_worldcity.reverse()
print("使用reverse方法后的排序：", want_worldcity)
want_worldcity.sort()
print("使用sort方法后的排序：",want_worldcity)
print(want_worldcity)
want_worldcity.sort(reverse=True)
print("使用reverse方法进行反向排序后的顺序",want_worldcity)
