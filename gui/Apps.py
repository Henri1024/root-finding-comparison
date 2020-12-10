from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

from logics import comparator


class Gui():
    def __init__(self):
        root = Tk()

        root.title('Apps')
        root.configure(background="white")
        root.resizable(width=0, height=0)

        title_frame = Frame(root, bg="#ffffff")
        title_frame.pack()

        self.menu_frame = Frame(root, bg="#ffffff")
        self.menu_frame.pack()

        # Label

        some_title = Label(title_frame, text="Biseksi, Regulfasi, Secant",
                           font=("times new roman", 20), bg="white")
        some_title.grid(row=0, column=0, pady=20, padx=30,)

        mylabel = Label(self.menu_frame, text="Choose the method :",
                        font=("times new romaan", 10), bg="white")
        mylabel.grid(row=0, column=0, padx=10, pady=20, sticky="w")

        function_label = Label(self.menu_frame, text="Function :", bg="white")
        function_label.grid(row=1, column=0, padx=10, sticky="w")

        self.Xi_value_label = Label(
            self.menu_frame, text="Xi Value :", bg="white")
        self.Xi_value_label.grid(row=2, column=0, padx=10, sticky="w")

        self.Xu_value_label = Label(
            self.menu_frame, text="Xu Value :", bg="white")
        self.Xu_value_label.grid(row=3, column=0, padx=10, sticky="w")

        self.Err_value_label = Label(
            self.menu_frame, text="Expected Error Rate :", bg="white")
        self.Err_value_label.grid(row=4, column=0, padx=10, sticky="w")

        # Text Box

        self.function_value = Entry(self.menu_frame, width=25,  borderwidth=2)
        self.function_value.grid(row=1, column=1, padx=20, pady=10)

        self.Xi_value = Entry(self.menu_frame, width=25, borderwidth=2)
        self.Xi_value.grid(row=2, column=1, padx=20, pady=10)

        self.Xu_value = Entry(self.menu_frame, width=25, borderwidth=2)
        self.Xu_value.grid(row=3, column=1, padx=20, pady=10)

        self.Err_value = Entry(self.menu_frame, width=25, borderwidth=2)
        self.Err_value.grid(row=4, column=1, padx=20, pady=10)

        # drop down box

        self.clicked = StringVar()
        self.clicked.set("Biseksi")

        self.drop = OptionMenu(self.menu_frame, self.clicked, "Biseksi",
                          "Regulfasi", "Secant")
        self.drop.grid(row=0, column=1)

        # Button
        run_img = PhotoImage(file='./gui/run.png')
        run_button = Button(self.menu_frame, image=run_img,
                            command=self.computeOne, borderwidth=0, bg="#ffffff")
        run_button.grid(row=5, column=0, pady=20)

        compare_img = PhotoImage(file='./gui/compare.png')
        compare_button = Button(self.menu_frame, image=compare_img,
                                command=self.compare_clicked, borderwidth=0, bg="#ffffff")
        compare_button.grid(row=5, column=1, pady=20)

        info_img = PhotoImage(file='./gui/info.png')
        info_button = Button(title_frame, image=info_img, command=self.popup,
                             borderwidth=0, bg="#ffffff", height=25, width=25)
        info_button.grid(row=0, column=1, padx=10, pady=20)

        root.mainloop()

    # Function
    def confirm(self):
        mylabel = Label(self.menu_frame, text=self.clicked.get())
        mylabel.grid(row=5, column=1)

    def submit(self):
        self.Xi_value.delete(0, END)
        self.Xu_value.delete(0, END)
        self.Err_value.delete(0, END)

    def Info(self):
        mylabel = Label(
            self.menu_frame, text="Andri Kuwito, Dharmawan, Henri, Jourdan", bg="white")
        mylabel.grid(row=2, column=1)

    def popup(self):
        messagebox.showinfo(
            "Info", "Kelompok : \nAndri Kuwito (535180062),\nSteven Dharmawan (535180075),\nHenri (535180074),\nJourdan Stanley (535180097)")

    def compare_clicked(self):
        fx = self.function_value.get()
        xi = self.Xi_value.get()
        xu = self.Xu_value.get()
        es = self.Err_value.get()

        try:
            comparator.compare(fx, float(xi), float(xu), float(es))
        except:
            messagebox.showinfo(
            "Warning", "Nilai f(Xi) * f(Xu) tidak < 0 or invalid function")

    def computeOne(self):
        fx = self.function_value.get()
        xi = float(self.Xi_value.get())
        xu = float(self.Xu_value.get())
        es = float(self.Err_value.get())

        # if self.clicked.get() == 'Biseksi':
        #     print('biseksi')
        # elif self.clicked.get() == 'Regulfasi':
        #     print('Regulfasi')
        # elif self.clicked.get() == 'Secant':
        #     print('Secant')

        try:
            comparator.compute(self.clicked.get(),fx,xi,xu,es)
        except:
            messagebox.showinfo(
            "Warning", "Nilai f(Xi) * f(Xu) tidak < 0 or invalid function")

        
        

