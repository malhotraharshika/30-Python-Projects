import pywhatkit

mobile = input("Enter Mobile No of Receiver: ")
message = input("Enter Message you wanna send: ")

pywhatkit.sendwhatmsg_instantly(mobile, message, wait_time=15) 

