from time import perf_counter
from  pyautogui import press
from time import sleep

sleep(3)
notesInBracket=['a', 'd', 'g']
start = perf_counter()
press(notesInBracket, _pause = False)
sleep(1)
end = perf_counter()
print('用时 %.3f' % (end - start))
input()