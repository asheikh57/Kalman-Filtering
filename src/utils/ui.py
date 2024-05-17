from tkinter import *
def make_window():
    window = Tk()
    window.title("Kalman Filtering Denoising")
    window.geometry("1000x500")
    import_data_button = Button(master = window,
                                height = 2,
                                width = 20,
                                text = "Import .csv Data")
    export_data_button = Button(master = window,
                                height = 2,
                                width = 20,
                                text = "Export filtered data to .csv")
    import_data_button.pack()
    export_data_button.pack()
    
    master_opt = StringVar(window, "1")
    filter_opts = {"Basic Kalman Filter" : "1",
                   "Adaptive Kalman Filter" : "2",
                   "H Infinity Filter" : "3"}
    
    for (text, value) in filter_opts.items():
        Radiobutton(window, text = text, variable = master_opt,
                    value = value, indicator = 0, background="red").pack(side = TOP, ipady=5, ipadx= 10)
    return window

if __name__ == "__main__":
    window = make_window()
    window.mainloop()