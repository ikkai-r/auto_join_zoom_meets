import tkinter as tk
import tkinter.ttk as ttk
from tkinter import W
import openpyxl as op

class AutoJoin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.dataframe = op.load_workbook("zoom_meets.xlsx")

        self.style_window()
        self.create_widgets()
        self.display_scheduled()

    def style_window(self):
        self.style = ttk.Style(self)
        self.tk.call('source', 'awthemes-10.4.0/awthemes-10.4.0/awdark.tcl')
        self.tk.call('::themeutils::setHighlightColor', 'awdark', '#E529EE')
        self.style.theme_use('awdark')
        self.geometry("700x400")
        self.title("auto join zoom meetings .ೃ࿐")
        self.iconbitmap("icon.ico")

    def create_widgets(self):
        topframe = ttk.Frame(self)

        df1 = self.dataframe.active

        for row in range(0, df1.max_row):
            for col in df1.iter_cols(1, df1.max_column):
                print(col[row].value)

        # button
        pass
    def on_button(self):
        # get the info for the zoom and put in zoom entries
        pass


    def display_scheduled(self):
        pass


window = AutoJoin()
window.mainloop()
