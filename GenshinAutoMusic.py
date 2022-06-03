from  pyautogui import press
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from time import sleep

defaultBpm=180

def playAccordingToStave(stave):
    bitTime = 60 / currentBpm
    halfMark = False
    inBracket = False
    notesInBracket = []

    def breakAferPlay():
        nonlocal halfMark
        if halfMark:
            sleep(bitTime / 2)
            halfMark = False
        else:
            sleep(bitTime)

    for note in stave:
        if inBracket:
            if note == ')':
                inBracket = False
                press(notesInBracket, _pause = False)
                breakAferPlay()
                notesInBracket = []
            elif note == ']':
                inBracket = False
                for n in notesInBracket:
                    press(n, _pause = False)
                    sleep(0.04)
                breakAferPlay()
                notesInBracket = []
            elif note.isalpha():
                notesInBracket.append(note)
        else:
            if note == '(' or note == '[':
                inBracket = True
            elif note == ' ':
                sleep(bitTime)
            elif note == '+':
                sleep(bitTime / 2)
            elif note == '-':
                halfMark = True
            elif note.isalpha():
                press(note, _pause = False)
                breakAferPlay()

def showInfoBeforePlay(currentBpm):
    print('当前节拍：', currentBpm)
    print('3秒准备')
    sleep(3)
    print('\n开始演奏~\n')

window = Tk()
window.withdraw()
txtTypeFilter = [('琴谱txt', '.txt')]

while True:
    try:
        input('\n按Enter开始选择琴谱\n')
        dir = askopenfilename(initialdir = './琴谱', title = '选择琴谱', filetypes = txtTypeFilter)
        if dir == '':
            print('\n您已取消本次选择\n')
            continue
        with open(dir, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    if line[0:4] == 'bpm=':
                        currentBpm = int(line[4:])
                        showInfoBeforePlay(currentBpm)
                        continue
                    else:
                        currentBpm = defaultBpm
                        showInfoBeforePlay(currentBpm)
                if line == '':
                    continue
                playAccordingToStave(line.lower().replace('0', ' ').replace('\n', ''))
        print('\n演奏完成！\n')
    except KeyboardInterrupt:
        print('\n播放终止')
    except Exception as e:
        print('\n播放失败，\n错误信息：%s'%e)
    finally:
        print('\n----------')