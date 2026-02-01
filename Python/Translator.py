from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
root['bg'] = 'light blue'
root.title('Real-time Translator')

Label(root, text="Language Translator", font="Arial 20 bold").pack()

Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

languages = [
    'english', 'french', 'german', 'spanish', 'hindi',
    'italian', 'japanese', 'korean', 'chinese', 'arabic',
    'russian', 'portuguese', 'dutch', 'greek', 'turkish',
    'polish', 'swedish', 'thai', 'vietnamese', 'urdu',
    'indonesian', 'hebrew', 'romanian', 'hungarian', 'czech'
]

dest_lang = ttk.Combobox(root, values=languages, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')

def Translate():
    try:
        translation = GoogleTranslator(
            source='auto',
            target=dest_lang.get()
        ).translate(Input_text.get())

        Output_text.delete(1.0, END)
        Output_text.insert(END, translation)

    except Exception as e:
        Output_text.delete(1.0, END)
        Output_text.insert(END, "Error: Please select a valid language.")

trans_btn = Button(
    root,
    text='Translate',
    font='arial 12 bold',
    pady=5,
    command=Translate,
    bg='orange',
    activebackground='green'
)
trans_btn.place(x=445, y=180)

root.mainloop()
