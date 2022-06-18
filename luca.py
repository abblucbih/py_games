

input("master key")

def add(text):
    with open("file.txt", "a") as add:
        add.write(text + "\n")
        

def view():
    with open("file.txt", "r") as file:
     for x in file:
            print(x)


while True:
    mode = input("what do u wish to do? ( view | add | q)  ")

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        text = input("what do u wish to add? ")
        add(text)
    
    else: 
        print("invalid")
        continue
    

  
    
