money = []

from datetime import datetime
import json

try:
   with open("money.json","r") as f:
          money = json.load(f)
except:
  money = []

this_year = datetime.now().year

#リスト表示
def show_list(money):
  print("一覧を表示します")
  print(f"\n-------({this_year}年の記録)-------")
  if len(money) == 0:
      print("まだ記録はありません\n")
  else:
    for i, k in enumerate(money):
      if k[0] == this_year:
        print(f"{i}: {k[1]} {k[2]} {k[3]}円")
      else:
        continue


#収入追加
def add_income(money):
  print("収入を入力してください")

  year = datetime.now().year
  month = input_number("月：",1,12)
  day = input_number("日：",1,31)

  date = f"{month:02}-{day:02}"

  category = input("カテゴリー：")
  while True:
    try:
      income = int(input("金額："))
      break
    except:
      print("注：数字のみを入力してください\n")

  money.append([year,date,category,income])

  money.sort(key=lambda x:(x[0],x[1]))
  print("追加しました\n")

#支出追加
def add_outcome(money):
  print("支出を入力してください")
  year = datetime.now().year
  month = input_number("月：",1,12)
  day = input_number("日：",1,31)

  date = f"{month.zfill(2)}-{day.zfill(2)}"

  category = input("カテゴリー：")
  while True:
    try:
      outcome = int(input("金額："))
      break
    except:
      print("数字のみを入力してください")

  money.append([year,date,category,-outcome])

  money.sort(key = lambda x:(x[0],x[1]))
  print("追加しました\n")

#合計表示
def show_total(money):
  if len(money) == 0:
    print("まだ記録はありません\n")
  else:
    total = sum([k[3] for k in money if k[0] == this_year])
    print(f"合計{total}円です\n")

#リスト削除
def del_list(money):
  if len(money) == 0:
    print("消去する記録がありません\n")
  else:
    try:
      del_num = int(input("消去する記録を選択してください"))
      if 0 <= del_num < len(money):
        del money[del_num]
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
     json.dump(money,f)

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
        except:
            print("正しい数字を入力してください")


#本体
print(f"今日は{get_today()}です")
show_list(money)

while True:

  print("1～5を選択してください\n")
  print("1:収入を追加")
  print("2:支出を追加")
  print("3:一覧表示")
  print("4:削除")
  print("5:終了")

  choice = (input("\n選択してください："))
  print("")

  if choice == "1":
    add_income(money)
    save_file(money)

  elif choice == "2":
    add_outcome(money)
    save_file(money)

  elif choice == "3":
    show_list(money)
    show_total(money)

  elif choice == "4":
    show_list(money)
    result = del_list(money)
    if result:
       show_list(money)
       save_file(money)
    else:
      continue

  elif choice == "5":
    print("終了します")
    save_file(money)
    break

  else:
    print("表示された番号を選択してください\n")


