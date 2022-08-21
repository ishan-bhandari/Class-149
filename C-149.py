from tkinter import *
import random

root=Tk()

root.title("Luck friend wheel")
root.geometry("500x500")


list1 = ["James" , "Isabella" , "Sophia" , "Oliver" , "Peter"]
print(list1)

def random_numbers():
    random_no = random.randint(0, 4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("your luckey friend is: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="who is your lucky Friend? ", command = random_numbers)
btn1.place(relx= 0.5,rely = 0.5,anchor = CENTER )

root.mainloop()