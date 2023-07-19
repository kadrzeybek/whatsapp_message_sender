import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:
    # sending message to receiver
    pywhatkit.sendwhatmsg("+90**********","test1",11,45)
    print("Successfully Sent!")

except:
    print("An Unexpected Error!")