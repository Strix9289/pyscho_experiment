import math
import numpy
import pandas as pd
import random
from psychopy import core, event, visual


# 文字を出力する関数
import function as f

# 課題用の文字セット

chr_set1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # 課題2
chr_set2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # 課題3


myWin = visual.Window(color='black', size=(800,600))
myClock = core.Clock() # 時計の用意

# 試行回数
n_trials = 50
RTs = numpy.zeros(n_trials) # 反応時間
Intvls = numpy.zeros(n_trials) # インターバル
Answer = numpy.zeros(n_trials) # 正しい答え
Judge = numpy.zeros(n_trials) # あなたの解答(1:正解, 0:不正解)
Precision = numpy.zeros(n_trials) # 正解か否か
message = visual.TextStim(myWin, text='', color='white') # 文字の書式
information = visual.TextStim(myWin, text='', font='MS PGothic', color='white') # 文字の書式
information2 = visual.TextStim(myWin, text='', font='MS PGothic', color='white') # 文字の書式

# ディレイの調整
latencies = []
for _ in range(n_trials):
    t = float(f'{random.uniform(1, 2):.4f}')
    latencies.append(t)

g_latencies = []

for i in range(40):
    numpy.random.shuffle(latencies)
    g_latencies = g_latencies + latencies

t = 1
pos_g_latencies = 0


# モード選択
flag = 0
while True:
    msg = """
    モード選択
    課題1 : 1
    課題2 : 2
    課題3 : 3
    課題4 : 4
    """
    f.print_text(myWin, msg, message)
    event.clearEvents()


    while True:
        pressedList = event.getKeys(keyList=['1','2','3','4'])
        if len(pressedList) > 0:
            if pressedList[0] == '1':  # 試行開始
                f.print_text(myWin, '課題1', message)
                core.wait(1)
                event.clearEvents()
                flag = 1
                break
            if pressedList[0] == '2':  # 試行開始
                f.print_text(myWin, '課題2', message)
                core.wait(1)
                event.clearEvents()
                flag = 2
                break
            if pressedList[0] == '3':  # 試行開始
                f.print_text(myWin, '課題3', message)
                core.wait(1)
                event.clearEvents()
                flag = 3
                break
            if pressedList[0] == '4':  # 試行開始
                f.print_text(myWin, '課題4', message)
                core.wait(1)
                event.clearEvents()
                flag = 4
                break
    break

# 課題1
if flag == 1:
    while True:
        f.start(myWin, message, t, n_trials)

        myWin.flip()
        t1 = myClock.getTime()
        flying = False

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:  # フライングの時の処理
                flying = True
                message.setText('Flying')
                message.draw()
                myWin.flip()
                core.wait(1)
                event.clearEvents()
                pos_g_latencies += 1
                break
            event.clearEvents()


            if myClock.getTime() > t1 + g_latencies[pos_g_latencies]:
                break

        if flying == True:
            continue

        f.print_one(myWin, 'A', information)
        event.clearEvents()

        t1 = myClock.getTime()  # 刺激提示時刻
        t2 = None

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:
                t2 = myClock.getTime()  # 反応時刻
                break
        event.clearEvents()

        myWin.flip()
        core.wait(1)

        RTs[t-1] = t2 - t1  # 反応時間
        Intvls[t-1] = g_latencies[pos_g_latencies]

        t += 1
        pos_g_latencies += 1

        if pos_g_latencies >= len(g_latencies):
            pos_g_latnecies = 0
        if t > n_trials:
            break

    # 反応時間の保存
    myWin.close()
    f.save(RTs, Intvls, Judge, Answer, Precision, True)
    core.quit()



# 課題2
if flag == 2:
    while True:
        f.start(myWin, message, t, n_trials)

        myWin.flip()
        t1 = myClock.getTime()
        flying = False

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:  # フライングの時の処理
                flying = True
                f.print_text(myWin, 'Flying', message)
                core.wait(1)
                event.clearEvents()
                pos_g_latencies += 1
                break
            event.clearEvents()

            if myClock.getTime() > t1 + g_latencies[pos_g_latencies]:
                break

        if flying == True:
            continue
        
        if random.random() < 0.5: # 0.5未満なら正解のセットを表示
            moji = random.choice(chr_set1)
            f.print_set(myWin, moji, moji, information, information2)
            ans = 'y'
            event.clearEvents()
        else:
            moji = random.sample(chr_set1, 2)
            f.print_set(myWin, moji[0], moji[1], information, information2)
            ans = 'u'
            event.clearEvents()
            

        t1 = myClock.getTime()  # 刺激提示時刻
        t2 = None

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:
                t2 = myClock.getTime()  # 反応時刻
                Judge[t-1] = 1 if pressedList[0] == 'y' else 0 # あなたの解答
                if pressedList[0] == ans: # 正答率
                    Precision[t-1] = 1
                else:
                    Precision[t-1] = 0

                break
        event.clearEvents()
        myWin.flip()
        core.wait(1)

        RTs[t-1] = t2 - t1  # 反応時間
        Intvls[t-1] = g_latencies[pos_g_latencies] # インターバル
        Answer[t-1] = 1 if ans=='y' else 0 # 正解

        t += 1
        pos_g_latencies += 1

        if pos_g_latencies >= len(g_latencies):
            pos_g_latnecies = 0
        if t > n_trials:
            break

    # 反応時間の保存
    myWin.close()
    f.save(RTs, Intvls, Judge ,Answer, Precision)
    core.quit()

# 課題3
if flag == 3:
    while True:
        f.start(myWin, message, t, n_trials)

        myWin.flip()
        t1 = myClock.getTime()
        flying = False

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:  # フライングの時の処理
                flying = True
                f.print_text(myWin, 'Flying', message)
                core.wait(1)
                event.clearEvents()
                pos_g_latencies += 1
                break
            event.clearEvents()

            if myClock.getTime() > t1 + g_latencies[pos_g_latencies]:
                break

        if flying == True:
            continue
        
        if random.random() < 0.5: # 0.5未満なら正解のセットを表示
            num = random.randint(0, 25)
            if random.random() < 0.5:
                f.print_set(myWin, chr_set1[num], chr_set2[num], information, information2)
            else:
                f.print_set(myWin, chr_set2[num], chr_set1[num], information, information2)
            ans = 'y'
            event.clearEvents()
        else:
            num1, num2 = f.random_double(0,25)
            if random.random() < 0.5:
                f.print_set(myWin, chr_set1[num1], chr_set2[num2], information, information2)
            else:
                f.print_set(myWin, chr_set2[num1], chr_set1[num2], information, information2)
            ans = 'u'
            event.clearEvents()
            

        t1 = myClock.getTime()  # 刺激提示時刻
        t2 = None

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:
                t2 = myClock.getTime()  # 反応時刻
                Judge[t-1] = 1 if pressedList[0] == 'y' else 0 # あなたの解答
                if pressedList[0] == ans: # 正解なら1
                    Precision[t-1] = 1
                else:
                    Precision[t-1] = 0

                break
        event.clearEvents()
        myWin.flip()
        core.wait(1)

        RTs[t-1] = t2 - t1  # 反応時間
        Intvls[t-1] = g_latencies[pos_g_latencies]
        Answer[t-1] = 1 if ans=='y' else 0

        t += 1
        pos_g_latencies += 1

        if pos_g_latencies >= len(g_latencies):
            pos_g_latnecies = 0
        if t > n_trials:
            break

    # 反応時間の保存
    myWin.close()
    f.save(RTs, Intvls, Judge, Answer, Precision)
    core.quit()

# 課題4
if flag == 4:
    while True:
        f.start(myWin, message, t, n_trials)

        myWin.flip()
        t1 = myClock.getTime()
        flying = False

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:  # フライングの時の処理
                flying = True
                f.print_text(myWin, 'Flying', message)
                core.wait(1)
                event.clearEvents()
                pos_g_latencies += 1
                break
            event.clearEvents()

            if myClock.getTime() > t1 + g_latencies[pos_g_latencies]:
                break

        if flying == True:
            continue
        
        if random.random() < 0.5: # 0.5未満なら同じカテゴリの2つを表示
            num1, num2 = f.random_double(0,25)
            if random.random() < 0.5: # 大文字の組み合わせ
                f.print_set(myWin, chr_set1[num1], chr_set1[num2], information, information2)
            else: # 小文字の組み合わせ
                f.print_set(myWin, chr_set2[num1], chr_set2[num2], information, information2)
            ans = 'y'
            event.clearEvents()
        else: # 大文字と小文字の組み合わせ
            num1, num2 = f.random_double(0,25)
            if random.random() < 0.5: # 右：大文字　左：小文字
                f.print_set(myWin, chr_set1[num1], chr_set2[num2], information, information2)
            else: # 右：小文字　左：大文字
                f.print_set(myWin, chr_set2[num1], chr_set1[num2], information, information2)
            ans = 'u'
            event.clearEvents()
            

        t1 = myClock.getTime()  # 刺激提示時刻
        t2 = None

        while True:
            pressedList = event.getKeys()
            if len(pressedList) > 0:
                t2 = myClock.getTime()  # 反応時刻
                Judge[t-1] = 1 if pressedList[0] == 'y' else 0 # あなたの解答
                if pressedList[0] == ans: # 正解なら1
                    Precision[t-1] = 1
                else:
                    Precision[t-1] = 0

                break
        event.clearEvents()
        myWin.flip()
        core.wait(1)

        RTs[t-1] = t2 - t1  # 反応時間
        Intvls[t-1] = g_latencies[pos_g_latencies]
        Answer[t-1] = 1 if ans=='y' else 0

        t += 1
        pos_g_latencies += 1

        if pos_g_latencies >= len(g_latencies):
            pos_g_latnecies = 0
        if t > n_trials:
            break

    # 反応時間の保存
    myWin.close()
    f.save(RTs, Intvls, Judge, Answer, Precision)
    core.quit()