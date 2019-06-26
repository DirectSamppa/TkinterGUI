import tkinter as tk
from tkinter import messagebox

# SampleApp -class takes care of creating window and switching between frames
# Then there are classes for every frame including the elements it holds



class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):        #Function that creates window for Tkinter GUI
        tk.Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):        #Function for switching frames
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()               #Destroys current window and creates a new one
        self._frame = new_frame
        self._frame.pack()

    def show_info(static):
        messagebox.showinfo("Info", "much wow, such info")
                                                                #Popup messageboxes
    def saved_info(self, master):
        messagebox.showinfo("SAVED", "SETTINGS SAVED!")
        master.switch_frame(MainMenu)


    def quit(self):
        self.destroy()


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="BELI").pack(side="top", fill="x", pady=100, padx=100)
        tk.Button(self, text="NEW GAME",
                  command=lambda: master.switch_frame(PlayFrame)).pack()
        tk.Button(self, text="LOAD GAME",
                  command=lambda: master.switch_frame(LoadFrame)).pack()
        tk.Button(self, text='SETTINGS',
                  command=lambda: master.switch_frame(SettingsFrame)).pack()
        tk.Button(self, text="QUIT",
                  command=lambda: master.quit()).pack()
        tk.Button(self, text="HELP",
                  command=lambda: master.show_info()).pack(pady=50)


class PlayFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="COMING SOON..").pack(side="top", fill="x", pady=100)
        tk.Button(self, text="CANCEL",
                  command=lambda: master.switch_frame(MainMenu)).pack(side="top", fill="y", pady=100, padx=100)


class LoadFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="LOAD GAME").pack(side="top", fill="x", pady=100)
        listbox = tk.Frame(self)
        buttons = tk.Frame(self)
        loadgamelb = tk.Listbox(listbox, width=60, height=6)
        loadgamelb.insert(1, "<  Slot1: Empty  >")
        loadgamelb.insert(2, "<  Slot2: Empty  >")
        loadgamelb.insert(3, "<  Slot3: Empty  >")
        loadgamelb.insert(4, "<  Slot4: Empty  >")
        loadgamelb.insert(5, "<  Slot5: Empty  >")
        loadgamelb.insert(6, "<  Slot6: Empty  >")
        loadgamelb.insert(7, "<  Slot7: Empty  >")
        loadgamelb.insert(8, "<  Slot8: Empty  >")
        loadgamelb.insert(9, "<  Slot9: Empty  >")
        loadgamelb.insert(10, "<  Slot10: Empty  >")
        loadgamelb.insert(11, "<  Slot11: Empty  >")
        loadgamelb.insert(12, "<  Slot12: Empty  >")
        scrollbar = tk.Scrollbar(listbox, orient="vertical", command=loadgamelb.yview)
        scrollbar.pack(side="right", fill= "y")
        loadgamelb.config(yscrollcommand=scrollbar.set)
        loadgamelb.pack()
        tk.Button(buttons, text="CONINUE GAME", state="disabled",
                  command=lambda: master.switch_fame(MainMenu)).pack()
        tk.Button(buttons, text="CANCEL",
                  command=lambda: master.switch_frame(MainMenu)).pack()

        listbox.pack(side="top")
        buttons.pack(side="top")


class SettingsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        left = tk.Frame(self, borderwidth=1, relief="solid")
        right = tk.Frame(self, borderwidth=1, relief="solid")
        bottom = tk.Frame(self, borderwidth=0, relief="solid")
        header = tk.Frame(self, borderwidth=1, relief="solid")
        tk.Label(bottom, text="\n\n")
        tk.Label(header, text="SETTINGS").pack(side="top", fill="both", pady=10)
        tk.Label(left, text="AUDIO").pack(side="top", fill="x", pady=0)
        tk.Label(left, text="MUSIC VOLUME").pack(side="top", fill="x", pady=10, padx=10)
        mv = tk.Scale(left, from_=0, to=100, orient=tk.HORIZONTAL).pack(side="top")
        tk.Label(left, text="GAME SOUNDS").pack(side="top", fill="x", pady=10)
        gs = tk.Scale(left, from_=0, to=100, orient=tk.HORIZONTAL).pack(side="top")
        tk.Label(right, text="VIDEO").pack(side="top", fill="x", pady=10)
        tk.Label(right, text="RESOLUTION").pack(side="top", fill="x", pady=10)
        a = "640x480"
        b = "800x600"
        c = "960x720"
        d = "1024x768"
        resoptions = [a, b, c, d]
        resvar = tk.StringVar(master)
        resvar.set(resoptions[0])
        resmenu = tk.OptionMenu(right, resvar, *resoptions, command=lambda: master.getData())
        resmenu.pack(side="top", fill="x", pady=10)
        tk.Label(right, text="VSYNC").pack(side="top", fill="x", pady=10)
        MODES = [("ON", "1"),
                 ("OFF", "2")]
        vs = tk.StringVar()
        vs.set("1")
        for text, mode in MODES:
            tk.Radiobutton(right, text=text, variable=vs, value=mode).pack(side="left", fill="x", pady=2)
        b1 = tk.Button(bottom, text="SAVE",
                    command=lambda: master.saved_info(master.switch_frame(MainMenu)))
        b2 = tk.Button(bottom, text="CANCEL",
                    command=lambda: master.switch_frame(MainMenu))
        b3 = tk.Button(bottom, text="HELP",
                    command=lambda: master.show_info())

        b1.pack(side="right", padx=30)
        b2.pack(side="left", padx=30)
        b3.pack(side="bottom", padx=30)

        header.grid(row=1, column=3)
        left.grid(row=2, column=2)
        right.grid(row=2, column=4)
        bottom.grid(row=5, column=3)




if __name__ == "__main__":

    app = SampleApp()
    app.resvar = '800x600'
    app.geometry(app.resvar)
    app.resizable(0, 0)
    app.mainloop()
