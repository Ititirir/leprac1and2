import time 

print("Wait...")
time.sleep(1.0)

while True:
    try: 
        x = int(input("Enter a whole number/integer: "))
        break
    except:
        print("Did I say whole number? I think so. Try again.")
        
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
    
print("Transitioning...")
time.sleep(1.0)

while True:
    password = input("Enter password: ")
    
    
    if len(password) >= 8:
        print("Password accepted!")
        break 
    else:
        print('"Too short!"')
        
time.sleep(2.0)
print("Bye!")




