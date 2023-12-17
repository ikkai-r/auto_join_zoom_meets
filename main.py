import tkinter as tk
import tkinter.ttk as ttk
from tkinter import LEFT, BOTTOM, END

from tktimepicker import SpinTimePickerModern, constants


class AutoJoin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.style_window()
        self.create_widgets()

    def style_window(self):
        self.style = ttk.Style(self)
        self.tk.call('source', 'awthemes-10.4.0/awthemes-10.4.0/awdark.tcl')
        self.tk.call('::themeutils::setHighlightColor', 'awdark', '#E529EE')
        self.style.theme_use('awdark')
        self.geometry("700x400")
        self.title("auto join zoom meetings .ೃ࿐")
        self.iconbitmap("icon.ico")

    def create_widgets(self):
        self.topframe = ttk.Frame(self)
        self.zoom_label = ttk.Label(self.topframe, text="Zoom Link")
        self.zoom_entry = ttk.Entry(self.topframe)
        self.time_label = ttk.Label(self.topframe, text="Time")

        self.button = ttk.Button(self.topframe, text="Submit", command=self.on_button)
        self.topframe.pack(expand=True, fill="both")

        #zoom
        self.zoom_label.pack(side=LEFT)
        self.zoom_entry.pack(side=LEFT)

        #time
        self.time_label.pack(side=LEFT)
        self.time_picker = SpinTimePickerModern(self.topframe)
        self.time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        self.time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", hoverbg="#404040",
                                 clickedbg="#2e2d2d", hovercolor="#DEDBDD", clickedcolor="#ffffff",
                                 font=("Arial", 20, "bold"))
        self.time_picker.configure_separator(bg="#404040", fg="#ffffff")
        self.time_picker.pack(side=LEFT)

        #days
        self.days_label = ttk.Label(self.topframe, text="Days")
        self.days_label.pack(side=LEFT)
        self.list = tk.Listbox(self.topframe, selectmode="multiple")
        self.list.pack(expand="True")

        x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
             "Saturday"]

        for each_item in range(len(x)):
            self.list.insert(END, x[each_item])
            self.list.itemconfig(each_item)

        #button
        self.button.pack(side=LEFT)

    def get_time(self):
        time_picker = SpinTimePickerModern(self)
        time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", hoverbg="#404040",
                                 clickedbg="#2e2d2d", hovercolor="#DEDBDD", clickedcolor="#ffffff",
                                 font=("Inter", 20, "bold"))
        time_picker.configure_separator(bg="#404040", fg="#ffffff")
        time_picker.pack()

    def on_button(self):
     print(self.zoom_entry.get())


window = AutoJoin()
window.mainloop()
