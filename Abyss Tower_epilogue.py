#関数

def nl(): #改行
    print("-------------------------------------------------------------------")



#システム
result = "" #判断結果の取得
tower_level = 30


#プレイヤーステータス
pl_name = ""
pl_hp = 300
pl_attck = 30
pl_armor = 30

#エネミーステータス
em_hp = 300
em_attck = 30
em_armor = 30


#タイトル
nl()
print("Abyss Tower")
nl()

#名前取得
print("名前を入力してください")
pl_name = str(input())
print(pl_name + " ですか？※yes or no")
result = str(input())

if result == "no":
  print("名前を入力してください※最後です")
  pl_name = str(input())
  print("ようこそ" + pl_name)

elif result == "yes":
  print("ようこそ" + pl_name)

else:
  print("不明な選択肢です")
  print("名前を入力してください※最後です")
  pl_name = str(input())
  print("ようこそ " + pl_name)

#ゲーム説明
nl()
result = ""
print("ゲーム説明を受けますか？※yes or no")
result = str(input())

if result == "yes":
  print("ゲーム概要を説明します")
  nl()
  print("プレイヤーは1階ごとに2回以上のイベントをクリアしながら")
  print("このゲームではタワーの最上階を目指します")
  print("基本的なイベントとして")
  print()
  print("戦闘",end="・")
  print("探索")
  print()
  print("の二つがあります")
  print("探索ではアイテムゲットや能力値アップのイベントが基本です")
  print("戦闘に関してですが")
  print("プレイヤーは")
  print()
  print("HP(体力)")
  print("ATTACK(攻撃力)")
  print("ARMOR(装甲)")
  print()
  print("の3つのステータスを持っています。")
  print("このゲームの戦闘におけるダメージ量は")
  print()
  print("ATTACK x 0.5 ~ ATTACK")
  print()
  print("の中からランダムな数字になります。")
  print("※例として初期値は30なので15~30のダメージになります")
  print("また全ての敵と自分は装甲値を持っており、実際のダメージは")
  print()
  print("ATTACK x 0.5 ~ ATTACK - ARMOR/2")
  print()
  print("になります。")
  print("※例として自分が30のダメージを受けたとしても、初期値で30あるため")
  print("  15ダメージしか受けないことになります")

  #タワーの説明
  nl()
  print("タワーの説明をします")
  print("このゲームは自身でタワーの最上階を決めることができ")
  print("5階ごとにイベントの数が増え、敵が強くなります")
  print("探索で能力値をあげ、敵を倒しつつ最上階を目指しましょう")
  nl()

else:
  print("ゲーム概要をスキップします")

print("それでは今回の階数を入力してください※半角です")
tower_level = int(input())
print("階数は " + str(tower_level) + "階 でいいですね？ yes or no")
result = str(input())

if result == "no":
  print("では正しい階数を入力してください")
  tower_level = int(input())
  print("最上階の" + str(tower_level) + "階を目指して頑張ってください")
else:
  print("最上階の" + str(tower_level) + "階を目指して頑張ってください")

