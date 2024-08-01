
import time 
# t = time.strftime('%H:%M:%S')
# print (t)

# hour = int(time.strftime('%H'))
# print (hour)
hour = int(input("Enter hour: "))



if hour >= 0 and hour < 12:
    print ("Good Morning")

elif hour>= 12 and hour < 17:
    print ("Good After Noon")



elif hour>= 17 and hour<= 23:
    print ("Good Night")

else:
    print ("Please Enter valid hour (0-23)")  



# import time

# hour = int(input("Enter hour: "))

# if 0 <= hour < 12:
#     print("Good Morning")
# elif 12 <= hour < 17:
#     print("Good Afternoon")
# elif 17 <= hour <= 23:
#     print("Good Evening")
# else:
#     print("Please enter a valid hour (0-23)")
