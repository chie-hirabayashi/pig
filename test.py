from datetime import datetime
from db_config import Day
from parts import list_day, list_number


# すべてのpigの辞書をリスト化
all_pig_l = []  # 空リスト用意(すべてのpigの辞書が入る)
for p in Day.select():
    pig_no = p.pig_no
    d = Day.get(Day.pig_no == pig_no)

    #  age算出
    add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
    today = (datetime.now()).strftime("%Y%m%d")
    age = int((int(today) - int(add_day) + 600) / 10000)

    # rotate算出
    number_l = list_number(pig_no)
    day_l = list_day(pig_no)
    day_time_l = []
    for n in range(2, 13):
        t_day = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
            day_l[n], "%Y/%m/%d"
        )
        day_time_l.append(t_day)
    idx = 10  # 初期値を設定 possibly unbound 回避
    for n in range(0, 10):  # 直近の出産日index取得
        if day_time_l[n].days < 0:
            idx = day_time_l.index(day_time_l[n])
            if idx == 0:  # pig_noが産子数(2)に入る防止
                idx = 1
            else:
                pass
            break
        else:
            idx = 10
    if day_time_l[(idx - 1)].days == 0:
        rotate = 0  # division by zero 回避
    else:
        rotate = 365 / day_time_l[(idx - 1)].days  # 回転数算出
        if rotate < 0:  # 過去1回しか出産していない場合rotateがマイナスになる防止
            rotate = 0
        else:
            pass
