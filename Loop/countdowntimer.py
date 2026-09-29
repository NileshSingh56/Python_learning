count=int(input("Enter the number of seconds for countdown: "))
import time
for i in range(count,0,-1):
    print (i)
    time.sleep(1)


print("Woohoo! Happy New Year.....")