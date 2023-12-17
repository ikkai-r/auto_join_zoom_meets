import tkinter as tk
import tkinter.ttk as ttk
from tkinter import LEFT, BOTTOM

from tktimepicker import SpinTimePickerModern, constants


class AutoJoin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.style_window()
        self.create_widgets()
        self.get_time()

    def get_time(self):
        self.botframe = ttk.Frame(self)
        self.botframe.pack(side=BOTTOM, expand=True, fill="both")
        time_picker = SpinTimePickerModern(self.botframe)
        time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", hoverbg="#404040",
                                 clickedbg="#2e2d2d", hovercolor="#DEDBDD", clickedcolor="#ffffff",
                                 font=("Inter", 20, "bold"))
        time_picker.configure_separator(bg="#404040", fg="#ffffff")
        time_picker.pack()

    def style_window(self):
        self.style = ttk.Style(self)
        self.tk.call('source', 'awthemes-10.4.0/awthemes-10.4.0/awdark.tcl')
        self.tk.call('::themeutils::setHighlightColor', 'awdark', '#E529EE')
        self.style.theme_use('awdark')
        self.geometry("500x200")
        self.title("auto join zoom meetings .ೃ࿐")
        self.iconbitmap("icon.ico")

    def create_widgets(self):
        self.topframe = ttk.Frame(self)
        self.entry = ttk.Entry(self.topframe)
        self.label = ttk.Label(self.topframe, text="Zoom Link")
        # self.button = ttk.Button(self.topframe, text="Get", command=self.on_button)
        self.topframe.pack(expand=True, fill="both")
        self.label.pack(side=LEFT)
        self.entry.pack(side=LEFT)
        self.button.pack(side=LEFT)

    # def on_button(self):
    # print(self.entry.get())


window = AutoJoin()
window.mainloop()
