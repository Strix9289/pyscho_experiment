import pandas as pd
import random
import numpy as np
from psychopy import core, event, gui, visual
#import psychopy.sound.backend_ptb as pss

komoji = ["a","c","e","g","m","n","o","r","s","u","v","w","x","z"] # 小文字
cap_moji =  ["d","f","h","k","l"] #大文字と同じ大きさ
desc_moji = ["g","p","q","y"] # 下に長い文字
spe_moji = ["i", "t"]


def random_double(a, b):
    n = random.randint(a, b)
    while True:
        m = random.randint(a, b)
        if n != m:
            break
    return n, m

def print_text(win, text, message):
    message.setText(text)
    message.draw()
    win.flip()

def print_one(win, text, message):
    message.setText(text)
    message.setHeight(0.5)
    message.draw()
    win.flip()

def print_set(win, text1, text2, information, information2):
    information.setText(text1)
    information2.setText(text2)
    # 文字の大きさ
    if text1 in komoji:
        information.setPos([-0.35, 0.08])
        information.setHeight(0.65)
    elif text1 in cap_moji:
        information.setPos([-0.35, 0])
        information.setHeight(0.5)
    elif text1 in desc_moji:
        information.setPos([-0.35, 0.10])
        information.setHeight(0.60)
    elif text1 in spe_moji:
        information.setPos([-0.35, 0.008])
        information.setHeight(0.57)
    elif text1 == 'j':
        information.setPos([-0.35, 0.06])
        information.setHeight(0.49)
    else:
        information.setPos([-0.35, 0])
        information.setHeight(0.50)
    # 文字の大きさ
    if text2 in komoji:
        information2.setPos([0.35, 0.08])
        information2.setHeight(0.65)
    elif text2 in cap_moji:
        information2.setPos([0.35, 0])
        information2.setHeight(0.5)
    elif text2 in desc_moji:
        information2.setPos([0.35, 0.10])
        information2.setHeight(0.60)
    elif text2 in spe_moji:
        information2.setPos([0.35, 0.008])
        information2.setHeight(0.57)
    elif text2 == 'j':
        information2.setPos([0.35, 0.06])
        information2.setHeight(0.49)
    else: # 大文字
        information2.setPos([0.35, 0])
        information2.setHeight(0.5)

    information.draw()
    information2.draw()
    win.flip()

def save(RTs, Intvls, Judge, Answer, Precision, f=False):
    flnm = gui.fileSaveDlg(prompt=u'出力ファイル名(*.csv)')
    print('file name = ', flnm)
    if f:
        df = pd.DataFrame({'RT' : RTs,
                            'Intervals' : Intvls})
    else:
        df = pd.DataFrame({'RT' : RTs,
                            'Intervals' : Intvls,
                            'Judge' : Judge,
                            'Answer': Answer,
                            'Precision':Precision})
    print(df)
    df.to_csv(f'{flnm}')
    print(flnm, ' was saved.')

def start(myWin, information, t, n_trials):
    #mySound = pss.SoundPTB(value = 2000, secs = 0.5, volume = 1.0)
    #mySound.play()
    print_text(myWin, f'{t}/{n_trials}', information) 
    core.wait(1)
    msg = 'zを押すとスタート\r\neを押すとストップ'
    print_text(myWin, msg, information) 

    while True:
        pressedList = event.getKeys(keyList=['z','e'])
        if len(pressedList) > 0:
            if pressedList[0] == 'e': # 中断
                myWin.close()
                core.quit()
            if pressedList[0] == 'z':  # 試行開始
                event.clearEvents()
                break

if __name__ == '__main__':
    myWin = visual.Window(color='black')
    information = visual.TextStim(myWin, text='', font='MS PGothic', color='white') # 文字の書式
    information2 = visual.TextStim(myWin, text='', font='MS PGothic', color='white') # 文字の書式
    print_set(myWin, 'I', 'i', information, information2)
    while True:
        pressedList = event.getKeys(keyList=['e'])
        if len(pressedList) > 0:
            if pressedList[0] == 'e': # 中断
                myWin.close()
                core.quit()
