from datetime import datetime
from db_config import Day
from db_config import Number
from dateutil import relativedelta

# for d in Day.select():
# print(d.pig_no, d.born_day1, d.pub_datetime)

# for n in Number.select():
# print(type(n.pub_datetime))

# d = Day.get(Day.pig_no == "10-28")
# print(d.pig_no)


""" リスト作成 """


def list_number(pig_no):  # numberリスト
    number = Number.get(Number.pig_no == pig_no)
    List = [
        f"{number.pig_no}",
        f"{number.born_num1}",
        f"{number.born_num2}",
        f"{number.born_num3}",
        f"{number.born_num4}",
        f"{number.born_num5}",
        f"{number.born_num6}",
        f"{number.born_num7}",
        f"{number.born_num8}",
        f"{number.born_num9}",
        f"{number.born_num10}",
        f"{number.born_num11}",
        f"{number.born_num12}",
        f"{number.delete_day}",
        f"{number.pub_datetime}",
    ]

    return List


def list_day(pig_no):  # dayリスト
    day = Day.get(Day.pig_no == pig_no)
    List = [
        f"{day.pig_no}",
        f"{day.add_day}",
        f"{day.born_day1}",
        f"{day.born_day2}",
        f"{day.born_day3}",
        f"{day.born_day4}",
        f"{day.born_day5}",
        f"{day.born_day6}",
        f"{day.born_day7}",
        f"{day.born_day8}",
        f"{day.born_day9}",
        f"{day.born_day10}",
        f"{day.born_day11}",
        f"{day.born_day12}",
        f"{day.delete_day}",
        f"{day.pub_datetime}",
    ]

    return List


# リスト作成コード
# pig_no = "10-28"
# List = list_number(pig_no)  # numberのリスト作成
# List = list_day(pig_no)  # dayのリスト作成
# print(List)


""" Aコマンドで使用 """


def create(new_no, new_day):
    Day.create(
        pig_no=new_no,
        add_day=new_day,
        born_day1="1900/1/1",
        born_day2="1900/1/1",
        born_day3="1900/1/1",
        born_day4="1900/1/1",
        born_day5="1900/1/1",
        born_day6="1900/1/1",
        born_day7="1900/1/1",
        born_day8="1900/1/1",
        born_day9="1900/1/1",
        born_day10="1900/1/1",
        born_day11="1900/1/1",
        born_day12="1900/1/1",
        delete_day="3000/1/1",
    )
    Number.create(
        pig_no=new_no,
        born_num1=0,
        born_num2=0,
        born_num3=0,
        born_num4=0,
        born_num5=0,
        born_num6=0,
        born_num7=0,
        born_num8=0,
        born_num9=0,
        born_num10=0,
        born_num11=0,
        born_num12=0,
        delete_day="3000/1/1",
    )


# 新data登録コード
# new_no = "99-99"
# new_day = "2022/7/7"
# create(new_no, new_day)

""" Rコマンドで使用 """


def in_born_data1(pig_no, new_day, new_num):  # born1用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day1 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num1 = new_num
    number.save()


def in_born_data2(pig_no, new_day, new_num):  # born2用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day2 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num2 = new_num
    number.save()


def in_born_data3(pig_no, new_day, new_num):  # born3用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day3 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num3 = new_num
    number.save()


def in_born_data4(pig_no, new_day, new_num):  # born4用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day4 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num4 = new_num
    number.save()


def in_born_data5(pig_no, new_day, new_num):  # born5用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day5 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num5 = new_num
    number.save()


def in_born_data6(pig_no, new_day, new_num):  # born6用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day6 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num6 = new_num
    number.save()


def in_born_data7(pig_no, new_day, new_num):  # born7用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day7 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num7 = new_num
    number.save()


def in_born_data8(pig_no, new_day, new_num):  # born8用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day8 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num8 = new_num
    number.save()


def in_born_data9(pig_no, new_day, new_num):  # born9用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day9 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num9 = new_num
    number.save()


def in_born_data10(pig_no, new_day, new_num):  # born10用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day10 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num10 = new_num
    number.save()


def in_born_data11(pig_no, new_day, new_num):  # born11用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day11 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num11 = new_num
    number.save()


def in_born_data12(pig_no, new_day, new_num):  # born12用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day12 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num12 = new_num
    number.save()


# 出産情報登録コード
# pig_no = "99-99"
# new_day = "2022/8/8"
# new_num = 8

# in_born_data1(pig_no, new_day, new_num)  # born1入力
# in_born_data2(pig_no, new_day, new_num)  # born2入力
# in_born_data3(pig_no, new_day, new_num)  # born3入力
# in_born_data4(pig_no, new_day, new_num)  # born4入力
# in_born_data5(pig_no, new_day, new_num)  # born5入力
# in_born_data6(pig_no, new_day, new_num)  # born6入力
# in_born_data7(pig_no, new_day, new_num)  # born7入力
# in_born_data8(pig_no, new_day, new_num)  # born8入力
# in_born_data9(pig_no, new_day, new_num)  # born9入力
# in_born_data10(pig_no, new_day, new_num)  # born10入力
# in_born_data11(pig_no, new_day, new_num)  # born11入力
# in_born_data12(pig_no, new_day, new_num)  # born12入力


""" Fコマンドで使用 """


"""
def pig_info(pig_no, number_l, day_l):
    day_time_l = []
    for n in range(2, 13):
        t_day = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
            day_l[n], "%Y/%m/%d"
        )
        day_time_l.append(t_day)

    idx = 10  # 初期値を設定 possibly unbound 回避
    for n in range(0, 10):
        if day_time_l[n].days < 0:
            idx = day_time_l.index(day_time_l[n])
            break
        else:
            idx = 10

    if day_time_l[(idx - 1)].days == 0:
        rotate = 0  # division by zero 回避
    else:
        rotate = 365 / day_time_l[(idx - 1)].days  # 回転数算出

    print(
        f"NO.{pig_no}",
        f"出産日:{day_l[idx+2]}",
        f"出産頭数:{number_l[idx+1]}匹",
        f"回転数:{round(rotate, 2)}回",
    )
"""


def pig_info(pig_no, number_l, day_l):
    day_time_l = []
    for n in range(2, 13):
        t_day = datetime.strptime(
            day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
            day_l[n], "%Y/%m/%d"
        )
        day_time_l.append(t_day)

    idx = 10  # 初期値を設定 possibly unbound 回避
    for n in range(0, 10):
        if day_time_l[n].days < 0:
            idx = day_time_l.index(day_time_l[n])
            break
        else:
            idx = 10

    if day_time_l[(idx - 1)].days == 0:
        rotate = 0  # division by zero 回避
    else:
        rotate = 365 / day_time_l[(idx - 1)].days  # 回転数算出

    print(
        f"NO.{pig_no}",
        f"出産日:{day_l[idx+2]}",
        f"出産頭数:{number_l[idx+1]}匹",
        f"回転数:{round(rotate, 2)}回",
    )


# 最近の出産情報表示コード
pig_no = "28-10"
number_l = list_number(pig_no)
day_l = list_day(pig_no)
pig_info(pig_no, number_l, day_l)


# pig_no = "99-99"
# li = list_day(pig_no)
# tstr = li[2]
# tdatetime = datetime.strptime(tstr, "%Y/%m/%d")
# print(tdatetime)
# print(type(tdatetime))

# index 3...day4-day3
# 回転数はday3-day2...[idx-1]
# 出産日はday4...List[5]...[idx+2]
# 出産頭数はnum4...List[4]...[idx+1]
# tdatetime = datetime.strptime(tstr, "%Y-%m-%d %H:%M:%S")

# 以下をインライン化
# time_l = []
# for n in range(2, 13):
# t_day = datetime.strptime(List[n], "%Y-%m-%d")
# time_l.append(t_day)

# print(time_l)
# day_timne_l = []
# for n in range(10):
# day_time = time_l[n+1] - time_l[n]
# day_timne_l.append(day_time)


""" 全削除用 """


def delete_alldays():  # 全day削除
    for day in Day.select():
        day.delete_instance()


def delete_allnums():  # 全number削除
    for num in Number.select():
        num.delete_instance()


# delete_alldays()  # 削除キー
# delete_allnums()  # 削除キー


""" C,Dコマンドで使用 """


def delete(pig_no):  # 単純削除機能
    number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    number.delete_instance()
    day.delete_instance()


# pig_no = "99-99"
# delete(pig_no)


""" Dコマンドで使用 """


def delete_day_set(pig_no):  # 時限爆弾設置
    number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    delete_day = datetime.now() + relativedelta.relativedelta(years=1)
    number.delete_day = delete_day
    number.save()
    day.delete_day = delete_day
    day.save()


# pig_no = "99-99"
# delete_day_set(pig_no)


"""

tstr = List[2]
tdatetime = datetime.datetime.strptime(tstr, "%Y-%m-%d %H:%M:%S")
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdate)
print(type(tdate))

oneday = "1900/01/01"
oneday_time1 = datetime.datetime.strptime(oneday, "%Y/%m/%d")
print(oneday_time1)

oneday = "2022-7-1"
oneday_time2 = datetime.datetime.strptime(oneday, "%Y-%m-%d")
print(oneday_time2)

day = oneday_time1 - oneday_time2
print(day.days)
print(type(day.days))

i = 365 / day.days
print(i)

list = []
for user in Users.select():  # すべてのユーザーのName,Ageを表示
    list.append(f"Name: {user.user_name} Age: {user.user_age}")
print(list)

"""