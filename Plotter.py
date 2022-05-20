import numpy as np
from matplotlib.figure import Figure
from Validator import Validator
import tkinter.messagebox as ms
from Formatter import Formatter
import Gui


class Plotter:
    def __init__(self):
        self.validator = Validator()
        self.equation_format = "The Equation Must be in X format"

    def __plot(self, min_value, max_value, equation):
        min_value = int(min_value)
        max_value = int(max_value)
        x = np.linspace(min_value, max_value, 100)
        try:
            y = eval(equation)
        except SyntaxError:
            return self.equation_format
        figure = Figure(figsize=(8, 4))
        plt = figure.add_subplot(111)
        plt.plot(x, y, '#004467')
        return figure

    def plot_function(self, min_value, max_value, equation, canvas, root):
        equation = Formatter.reformat_equation(equation.get())
        min_value = min_value.get()
        max_value = max_value.get()
        try:
            status = self.validator.validate(equation, min_value, max_value)
            if type(status) == bool:
                figure = self.__plot(min_value, max_value, equation)
                Gui.Gui.update_graph(figure, canvas, root)
            else:
                ms.showerror("Invalid Input", status)
        except:
            status = self.equation_format
            ms.showerror("Invalid Input", status)
