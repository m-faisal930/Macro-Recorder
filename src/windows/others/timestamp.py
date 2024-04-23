from tkinter import *
from tkinter.ttk import *
from windows.popup import Popup


class Timestamp(Popup):
    def __init__(self, parent, main_app):
        super().__init__("Timestamp Settings", 300, 150, parent)
        main_app.prevent_record = True
        self.settings = main_app.settings
        Label(self, text="Enter Fixed Timestamp ", font=('Segoe UI', 10)).pack(side=TOP, pady=10)
        userSettings = main_app.settings.get_config()
        fixed_timetamp = Spinbox(self, from_=0, to=100000000, width=7, validate="key",
                              validatecommand=(main_app.validate_cmd, "%d", "%P"))
        fixed_timetamp.insert(0, userSettings["Others"]["Fixed_timestamp"])
        fixed_timetamp.pack(pady=20)
        buttonArea = Frame(self)
        Button(buttonArea, text="Confirm",
               command=lambda: [self.settings.change_settings("Others", "Fixed_timestamp", None, float(fixed_timetamp.get())),
                                self.destroy()]).pack(side=LEFT, padx=10)
        Button(buttonArea, text="Cancel", command=self.destroy).pack(side=LEFT, padx=10)
        buttonArea.pack(side=BOTTOM, pady=10)
        self.wait_window()
        main_app.prevent_record = False

