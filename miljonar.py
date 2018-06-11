import tkinter as tk

okno =  tk.Tk()
okno.overrideredirect(True)
okno.geometry("{0}x{1}+0+0".format(okno.winfo_screenwidth(), okno.winfo_screenheight()))
okno.mainloop()
