import pandas as pd
import random
import numpy as np
from psychopy import core, event, gui
#import psychopy.sound.backend_ptb as pss


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

def print_set(win, text1, text2, information, information2, f):
    information.setText(text1)
    information2.setText(text2)
    information.setPos([-0.35, 0])
    information2.setPos([0.35, 0])
    if f == 0:  # 両方が同じ文字の大きさの時
        information.setHeight(0.5)
        information2.setHeight(0.5)
    elif f == 1: # 左の文字が大文字の時
        information.setHeight(0.5)
        information2.setHeight(0.6)
    else:       # 右の文字が大文字の時
        information.setHeight(0.6)
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
    msg = 'zを押すとスタート'
    print_text(myWin, msg, information) 

    while True:
        pressedList = event.getKeys(keyList=['z'])
        if len(pressedList) > 0:
            if pressedList[0] == 'z':  # 試行開始
                event.clearEvents()
                break

if __name__ == '__main__':
    # myWin = visual.Window(color='black')
    # information = visual.TextStim(myWin, text='', color='white') # 文字の書式
    # information2 = visual.TextStim(myWin, text='',height=0.8, color='white') # 文字の書式
    # print_set(myWin, 'A', 'B', information, information2)
    # core.wait(2)
    # myWin.close()
    # core.quit()
    print(random_double(0,25))
