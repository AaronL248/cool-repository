# from pyautogui import *
# import time
# time.sleep(3)
# for i in range(1, 40):
#     typewrite('pebis')
#     press('Enter')
dic = {1:2, 3:4, 1:6}
print((1,2,3) in (1,2,3,4))

class MyError(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise MyError('test')
except MyError as e:
    print(e, 'doesnt work')