import tkinter as tk
import wikipedia
from tkinter import messagebox


class Search_class(object):
    def __init__(self, mainframe):
        self.mainframe = mainframe

        def search_data(*args):
            try:
                if len(search.get()) <= 0:
                    messagebox.showerror('Error', 'Please fill the Search entry.\nTry again please')
                else:
                    search_value = search.get()
                    wikipedia.set_lang("en")
                    content = wikipedia.summary(search_value)
                    data.insert('insert', '\t' + content + '\n\n')
                    keyword_fun()
            except:
                messagebox.showinfo('Warning',
                                    'Search results is not found.\nTry again please or otherwise info to Developer.')

        def keyword_fun():
            keyword_list = wikipedia.search(search.get())
            myself = 'Myself David. I am a Programmer as well as a Cyber Security crime resolver.\n\nListed below are the keywords for your results. Try once, thank you for using my application.\n'
            words = ''
            for i in keyword_list:
                words += i + '\n'
            keywords.insert('insert', myself + words)

        search = tk.Entry(self.mainframe, width=38, fg='blue', bg='powder blue', font=('Helvetical', 15, ''))
        search.place(x=160, y=30)
        search_btn = tk.Button(self.mainframe, command=search_data, text='Search', width=15,
                               font=('Helvetical', 12, ''), bg='violet')
        search_btn.place(x=600, y=26)
        search.bind('<Return>', search_data)
        frame = tk.LabelFrame(self.mainframe, text=' Orismós ', font=('Times', 17, 'bold'), width=800, height=400,
                              bd=5)  # Greek language
        frame.place(x=50, y=70)
        data = tk.Text(frame, width=98, height=22)
        data.place(y=8)

        keywords = tk.Text(self.mainframe, width=98, height=6)
        keywords.place(x=54, y=480)


def run():
    root = tk.Tk()
    root.title('Search Engine')
    root.geometry('900x600+240+25')
    Search_class(root)
    root.resizable(False, False)
    root.mainloop()

def developer():
	return 'David Boga'

def gmail():
	return 'spoter49@gmail.com'


if __name__ == '__main__':
    run()

# 8748008340
