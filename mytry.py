# ----------------- threadtest
# from threading import Thread
# from time import time
# def execute_slowly(glacial,plodding,leaden):
#     sleep(2)
#     print(glacial, plodding, leaden,sep = '')


# t = Thread(target=execute_slowly, args=(1, 2, 3))
# t.start()
# print(11111)
# sleep(4)
# print(22222)
# --------------------
# from datetime import datetime
# def convert2ampm(time24:str)->str:
#     return datetime.strptime(time24,'%H:%M').strftime('%I:%M%P')
# print(convert2ampm('19:00'))
showtb = [i for i in range(10,1,-2)]
print(showtb)