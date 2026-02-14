from tkinter import *

expression = "" # it will store whatever we  type

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("Simple Calculator")
    gui.geometry("270x200")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 14), justify="right")
    expression_field.grid(columnspan=4, ipadx=8, ipady=5, padx=10, pady=10)

    equation.set('Enter expression')

    button1 = Button(gui, text=' 1 ', fg='black', bg='orange', command=lambda: press(1), height=2, width=6)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='orange', command=lambda: press(2), height=2, width=6)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='orange', command=lambda: press(3), height=2, width=6)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='orange', command=lambda: press(4), height=2, width=6)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='orange', command=lambda: press(5), height=2, width=6)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='orange', command=lambda: press(6), height=2, width=6)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='orange', command=lambda: press(7), height=2, width=6)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='orange', command=lambda: press(8), height=2, width=6)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='orange', command=lambda: press(9), height=2, width=6)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='orange', command=lambda: press(0), height=2, width=6)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='orange', command=lambda: press("+"), height=2, width=6)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='orange', command=lambda: press("-"), height=2, width=6)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='orange', command=lambda: press("*"), height=2, width=6)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='orange', command=lambda: press("/"), height=2, width=6)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='orange', command=equalpress, height=2, width=6)
    equal.grid(row=5, column=2)

    clear_button = Button(gui, text='Clear', fg='black', bg='orange', command=clear, height=2, width=6)
    clear_button.grid(row=5, column=1)

    decimal = Button(gui, text='.', fg='black', bg='orange', command=lambda: press("."), height=2, width=6)
    decimal.grid(row=5, column=3)

    gui.mainloop()