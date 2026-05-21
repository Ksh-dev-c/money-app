money = []

from datetime import datetime
import json

try:
   with open("money.json","r") as f:
          money = json.load(f)
except:
  money = []

#リスト表示
def show_list(money,year,month):
  print("一覧を表示します")
  print(f"\n-------({year}年{month}月の記録)-------")

  filtered_money = []

  for k in money:
    record_month = k[1][:2] #05-12から05を取り出す

    if k[0] == year and record_month == f"{month:02}": #年月指定
      filtered_money.append(k)

  if len(filtered_money) == 0:
      print("まだ記録はありません\n")
  else:
    for i, k in enumerate(filtered_money):
      print(f"{i}: {k[1]} {k[2]} {k[3]}円")

  return filtered_money


#合計表示
def show_total(money,year,month):
  if len(money) == 0:
    print("まだ記録はありません\n")
  else:
    total = sum([k[3] for k in money if k[0] == year and int(k[1][:2]) == month])
    print(f"合計{total}円です\n")


#収入・支出追加
def add_money(money,come):

  if come == "income":
    print("収入を入力してください")
  else:
    print("支出を入力してください")

  year = datetime.now().year
  month = input_number("月：",1,12)
  day = input_number("日：",1,31)

  date = f"{month:02}-{day:02}"

  category = input("カテゴリー：")
  while True:
    try:
      amount = int(input("金額："))
      break
    except:
      print("注：数字のみを入力してください\n")

  if come == "outcome":
    amount = -amount
  
  money.append([year,date,category,amount])
  money.sort(key=lambda x:(x[0],x[1]))
  print("追加しました\n")


#リスト削除
def del_list(money,filtered_money):
  if len(filtered_money) == 0:
    print("消去する記録がありません\n")
  else:
    try:
      del_num = int(input("消去する記録を選択してください"))

      if 0 <= del_num < len(filtered_money):
        target = filtered_money[del_num]

        money.remove(target)

        print("削除しました")
        return True
      
      else:
        print("選択された番号がありません")
        return False

    except:
      print("正しい番号を入力してください")
      return False

#ファイルセーブ
def save_file(money):
  with open("money.json", "w") as f:
     json.dump(money, f, ensure_ascii=False, indent=2)

#今日の日付取得
def get_today():
  today = datetime.now().strftime("%Y-%m-%d")
  return today

#数字入力
def input_number(text_number,min_number,max_number):
    while True:
        try:
            number = int(input(text_number))

            if min_number <= number <= max_number:
                return number
            else:
                print("正しい数字を入力してください")
        except ValueError:
            print("正しい数字を入力してください")

#年月移動
def change_date(time,select_date):
  if time == "year":
    date = "年"
  else:
    date = "月"

  while True:
    choice = input("選択してください\n"
    f"a:{select_date - 1}{date} w:{select_date}{date} s:{select_date + 1}{date}")
  
    if choice == "a":
      select_date -= 1 
    elif choice == "w":
      return select_date
    elif choice == "s":
      select_date += 1
    else:
      print("正しいものを入力してください")

#編集機能
def edit_list(money,filtered_money):
  if len(filtered_money) == 0:
    print("記録がありません")
  else:
    print("編集するデータを選択してください")

    while True:
      try:
        edit_num = int(input())
        if 0 <= edit_num < len(filtered_money):
          target = filtered_money[edit_num]
          print(target)
          break
        else:
          print("正しい数字を入力してください")
      except ValueError:
        print("正しく数字を入力してください")

    print("どの部分を編集しますか？")
    while True:
      try:
        target_num = int(input("0:年\n1:月日\n2:カテゴリー\n3:金額"))
        break
      except ValueError:
        print("正しい数字を入力してください")

    if target_num == 3:
      while True:
        try:
          if 0 <= target_num <= 3:
            new_value = int(input(("新しい金額：")))
            break
        except ValueError:
          print("正しく数字を入力してください")

    else:
      new_value = input("新しい情報：")

    target[target_num] = new_value

    print("編集しました")
    print(target)


#本体
print(f"今日は{get_today()}です")

now_year = datetime.now().year #strftimeは文字列になる
now_month = datetime.now().month
show_list(money,now_year,now_month)

while True:

  print("1～5を選択してください\n")
  print("1:収入を追加")
  print("2:支出を追加")
  print("3:一覧表示")
  print("4:削除")
  print("5:編集")
  print("6:終了")

  choice = (input("\n選択してください："))
  print("")

  if choice == "1":
    add_money(money,"income")
    save_file(money)

  elif choice == "2":
    add_money(money,"outcome")
    save_file(money)

  elif choice == "3":
    choice_year = change_date("year",now_year)
    choice_month = change_date("month",now_month)
      
    show_list(money,choice_year,choice_month)
    show_total(money,choice_year,choice_month)

  elif choice == "4":
    choice_year = change_date("year",now_year)
    choice_month = change_date("month",now_month)

    filtered_money = show_list(money,choice_year,choice_month)

    result = del_list(money,filtered_money)

    if result: #Trueの省略
       show_list(money,choice_year,choice_month)
       save_file(money)
    else:
      continue
  
  elif choice == "5":
    choice_year = change_date("year",now_year)
    choice_month = change_date("month",now_month)

    filtered_money = show_list(money,choice_year,choice_month)

    edit_list(money,filtered_money)
    save_file(money)

  elif choice == "6":
    print("終了します")
    save_file(money)
    break

  else:
    print("表示された番号を選択してください\n")


