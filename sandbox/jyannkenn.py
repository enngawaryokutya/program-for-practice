import random


"""#確率計算用
def percent():
    count1 = test_pc.count(1)
    count2 = test_pc.count(2)
    count3 = test_pc.count(3)

    total = count1+count2+count3
    
    rate1 = count1/total
    rate2 = count2/total
    rate3 = count3/total
    print(f"1が出る割合は{rate1}\n2が出る割合は{rate2}\n3が出る割合は{rate3}")

test_pc = []
count = 0

while count <= 10000:

    test_pc.append(random.randrange(1,4))
    count += 1

print(test_pc)
percent()"""
GTP = {1:"グー",2:"チョキ",3:"パー"}

def jyannkenn():
    while True:
        pc = random.randrange(1,4)
        user = int(input("グーなら1、チョキなら2、パーなら3を入力:"))
        if pc == user:
            print(f"あなた：{GTP.get(user)} vs PC:{GTP.get(pc)}")
            print("あいこでしょ！")
        elif pc == 1 and user == 3 or pc == 2 and user == 1 or pc == 3 and user == 2:
            print(f"あなた：{GTP.get(user)} vs PC:{GTP.get(pc)}")
            print("あなたの勝ち！")
            break
        else:
            print(f"あなた：{GTP.get(user)} vs PC:{GTP.get(pc)}")
            print("あなたの負け！")
            break
    
        
jyannkenn()