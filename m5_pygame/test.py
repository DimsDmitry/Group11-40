from time import time as telephon


start = telephon()
for i in range(1000):
    print(i)

stop = telephon()


print('Прошло времени:', stop-start)