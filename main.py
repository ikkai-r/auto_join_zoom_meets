import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, W

from tktimepicker import SpinTimePickerModern, constants


class AutoJoin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.list = None
        self.time_picker = None
        self.button = None
        self.zoom_name_entry = None
        self.zoom_entry = None
        self.meetings = []

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
        zoom_label = ttk.Label(topframe, text="Zoom Link")
        self.zoom_entry = ttk.Entry(topframe, width=40)
        zoom_name_label = ttk.Label(topframe, text="Meeting Name")
        self.zoom_name_entry = ttk.Entry(topframe)
        time_label = ttk.Label(topframe, text="Time")
        self.button = ttk.Button(topframe, text="Submit", command=self.on_button)
        topframe.pack(expand=True, fill="both")

        # time
        self.time_picker = SpinTimePickerModern(topframe)
        self.time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        self.time_picker.configureAll(bg="#404040", height=1, fg="#ffffff", hoverbg="#404040",
                                      clickedbg="#2e2d2d", hovercolor="#DEDBDD", clickedcolor="#ffffff",
                                      font=("Arial", 20, "bold"), padx=10, pady=5)
        self.time_picker.configure_separator(bg="#404040", fg="#ffffff")

        # days
        days_label = ttk.Label(topframe, text="Days")
        self.list = tk.Listbox(topframe, selectmode="multiple")

        x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
             "Saturday"]

        for each_item in range(len(x)):
            self.list.insert(END, x[each_item])
            self.list.itemconfig(each_item)

        # labels
        zoom_name_label.grid(row=0, column=0, sticky=W, pady=10, padx=10)
        zoom_label.grid(row=1, column=0, sticky=W, pady=10, padx=10)
        time_label.grid(row=2, column=0, sticky=W, pady=10, padx=10)
        days_label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        # entries
        self.zoom_name_entry.grid(row=0, column=1, sticky=W, pady=10, padx=10)
        self.zoom_entry.grid(row=1, column=1, sticky=W, pady=10, padx=10)
        self.time_picker.grid(row=2, column=1, sticky=W, pady=10, padx=5)
        self.list.grid(row=3, column=1, sticky=W, padx=10)

        # button
        self.button.grid(row=4, column=1, sticky=W, pady=10, padx=10)

    def on_button(self):
        # get the info for the zoom and put in zoom entries
        index_selected = self.list.curselection()
        days_selected = []
        for index in index_selected:
            days_selected.append(self.list.get(index))

        time_pick = self.time_picker.time()

        new_zoom_meet = {
            "zoom_name": self.zoom_name_entry.get(),
            "zoom_link": self.zoom_entry.get(),
            "time": str(time_pick[0]) + ":" + str(time_pick[1]),
            "days": days_selected
        }

        self.meetings.append(new_zoom_meet)
        self.zoom_name_entry.delete(0, END)
        self.zoom_entry.delete(0, END)
        self.list.selection_clear(0, END)

    def display_scheduled(self):
        pass


window = AutoJoin()
window.mainloop()
