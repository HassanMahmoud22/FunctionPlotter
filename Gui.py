from functools import partial
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Plotter import Plotter


class Gui:

    def __init__(self):
        self.plotter = Plotter()
        self.root = Tk()
        self.figure = Figure(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.equation = ""
        self.min_value = ""
        self.max_value = ""

    def set_window(self):
        title = 'Function Plotter'
        self.root.title(title)
        self.root.geometry("800x600+500+200")
        self.root.resizable(False, False)
        self.root.config(bg="#afb7bb")

    def set_initial_values(self):
        self.equation = StringVar(self.root, "5*x^3 + 2*x")
        self.min_value = StringVar(self.root, "0")
        self.max_value = StringVar(self.root, "10")

    def set_graph(self):
        self.figure.add_subplot(111)
        self.canvas.get_tk_widget().place(x=0, y=200)
        self.canvas.draw()

    @staticmethod
    def update_graph(figure, canvas, root):
        canvas.close_event()
        canvas = FigureCanvasTkAgg(figure, master=root)
        canvas.get_tk_widget().place(x=0, y=200)
        canvas.draw()

    def set_inputs_block(self):
        # equation lapel and input field

        Label(self.root, text="Equation of X: ", bg="#afb7bb", fg="#004467", font=('Comic Sans MS bold', 10)) \
            .place(x=20, y=20)
        Entry(self.root, textvariable=self.equation, bg="#FFF", fg="#004467", width=35,
              font=('Comic Sans MS bold', 10)).place(x=175, y=20)

        # Minimum Value of X lapel and input field
        Label(self.root, text="Minimum Value of X: ", bg="#afb7bb", fg="#004467", font=('Comic Sans MS bold', 10)) \
            .place(x=20, y=60)
        Entry(self.root, textvariable=self.min_value, bg="#FFF", fg="#004467", width=35,
              font=('Comic Sans MS bold', 10)).place(x=175, y=60)

        # Maximum Value of X lapel and input field
        Label(self.root, text="Maximum Value of X: ", bg="#afb7bb", fg="#004467", font=('Comic Sans MS bold', 10)) \
            .place(x=20, y=100)
        Entry(self.root, textvariable=self.max_value, bg="#FFF", fg="#004467", width=35,
              font=('Comic Sans MS bold', 10)).place(x=175, y=100)

        # Draw Function Button
        Button(self.root, text="Draw Function", bg="#004467", fg="#e4e7e8", width=50, font=('Comic Sans MS bold', 13),
               command=partial(self.plotter.plot_function, self.min_value, self.max_value, self.equation, self.canvas,
                               self.root)) \
            .place(x=135, y=150)

    def build_ui(self):
        self.set_window()
        self.set_initial_values()
        self.set_inputs_block()
        self.set_graph()
        self.root.mainloop()
