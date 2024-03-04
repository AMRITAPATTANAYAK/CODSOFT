import string
from tkinter import *
import random


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    
    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())
    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
        
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
        
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
    
    # password=random.sample(all,password_length)
    # passwordField.insert(0,password)


root=Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('Arial',15,'bold')

passwordLabel=Label(root,text='Password Generator', font=('times new roman',20,'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

weakRadioButton=Radiobutton(root,  text='Weak', value=1, variable=choice, font=Font)
weakRadioButton.grid(pady=5)

mediumRadioButton=Radiobutton(root,  text='Medium', value=2, variable=choice, font=Font)
mediumRadioButton.grid(pady=5)

strongRadioButton=Radiobutton(root,  text='Strong', value=3, variable=choice, font=Font)
strongRadioButton.grid(pady=5)

lengthLabel=Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root, from_=5, to=18, width=5, font=Font)
length_Box.grid(pady=5)

passwordField=Entry(root, width=25, bd=2, font=Font)
passwordField.grid(pady=5)

generateButton=Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)


root.mainloop()