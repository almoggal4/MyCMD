# Imports:
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from psutil import cpu_percent
import matplotlib

#  Backgrounds:
BACKGROUND_MAIN_TASK_MANGER = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\main_TM.png"
BACKGROUND_MAIN = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\main.png"
BACKGROUND_CPU = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\cpu_background.png"
BACKGROUND_RAM = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\ram_background.png"
BACKGROUND_STORAGE = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\storage_background.png"
BACKGROUND_NETWORK = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\network_background.png"

#  Buttons:
BUTTON_START = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\start.png"
BUTTON_CPU = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\cpu.png"
BUTTON_RAM = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\ram.png"
BUTTON_STORAGE = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\storage.png"
BUTTON_NETWORK = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\network.png"
BUTTON_BACK = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\back.png"
BUTTON_HOME = r"C:\Users\almog\Python_Advanced_Course\TaskManger\pictures\home.png"

Root = tk.Tk()
Root.resizable(0, 0)


# The main window of the app.
def main_window(background=BACKGROUND_MAIN_TASK_MANGER):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    start_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_START))
    button_start = tk.Button(Root, font=40, image=start_image_tk, borderwidth=0, activebackground='black',
                             command=(lambda: options_window()))
    button_start.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.16)
    button_start.config(bg="black")

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


# Close The last window.
def close_window():
    Root.quit()
    Root.destroy()
    return


# The page of the options.
def options_window(background=BACKGROUND_MAIN):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    cpu_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_CPU))
    button_cpu = tk.Button(Root, font=40, image=cpu_image_tk, borderwidth=0, activebackground='black',
                           command=(lambda: cpu_page(BACKGROUND_CPU)))
    button_cpu.place(relx=0.25, rely=0.15, relheight=0.32, relwidth=0.25)
    button_cpu.config(bg="black")

    ram_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_RAM))
    button_ram = tk.Button(Root, font=40, image=ram_image_tk, borderwidth=0, activebackground='black',
                           command=(lambda: ram_page(BACKGROUND_RAM)))
    button_ram.place(relx=0.25, rely=0.55, relheight=0.32, relwidth=0.25)
    button_ram.config(bg="black")

    storage_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_STORAGE))
    button_storage = tk.Button(Root, font=40, image=storage_image_tk, borderwidth=0, activebackground='black',
                               command=(lambda: storage_page(BACKGROUND_STORAGE)))
    button_storage.place(relx=0.5, rely=0.15, relheight=0.32, relwidth=0.25)
    button_storage.config(bg="black")

    network_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_NETWORK))
    button_network = tk.Button(Root, font=40, image=network_image_tk, borderwidth=0, activebackground='black',
                               command=(lambda: network_page(BACKGROUND_NETWORK)))
    button_network.place(relx=0.5, rely=0.55, relheight=0.32, relwidth=0.25)
    button_network.config(bg="black")

    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


# The page that present CPU uses.
def cpu_page(background):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    fig = plt.Figure()
    y = []
    cpu_percent()
    matplotlib.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120
    def animate(i):
        y.append(cpu_percent())
        if len(y) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            #plt.grid("")
            plt.cla()
            plt.plot(y, '#FAD8C1', label='Real-Time CPU Uses')
            ax.set_xticks([])

        else:
            plt.cla()
            plt.plot(y[-frame_len:], '#FAD8C1', label='Real-Time CPU Uses')

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Uses (%)')
        plt.legend(loc=1)
        plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


# The page that present RAM uses.
def ram_page(background):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    fig = plt.Figure()
    y = []
    cpu_percent()
    matplotlib.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120
    def animate(i):
        y.append(cpu_percent())
        if len(y) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            #plt.grid("")
            plt.cla()
            plt.plot(y,'#FAD8C1', label='Real-Time CPU Uses')
            ax.set_xticks([])

        else:
            plt.cla()
            plt.plot(y[-frame_len:], '#FAD8C1', label='Real-Time CPU Uses')

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Uses (%)')
        plt.legend(loc=1)
        plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


# The page that present Storage uses.
def storage_page(background):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    fig = plt.Figure()
    y = []
    cpu_percent()
    matplotlib.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120
    def animate(i):
        y.append(cpu_percent())
        if len(y) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            #plt.grid("")
            plt.cla()
            plt.plot(y,'#FAD8C1', label='Real-Time CPU Uses')
            ax.set_xticks([])

        else:
            plt.cla()
            plt.plot(y[-frame_len:], '#FAD8C1', label='Real-Time CPU Uses')

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Uses (%)')
        plt.legend(loc=1)
        plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


# The page that present network uses.
def network_page(background):
    for widget in Root.winfo_children():
        widget.destroy()

    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    fig = plt.Figure()
    y = []
    cpu_percent()
    matplotlib.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120
    def animate(i):
        y.append(cpu_percent())
        if len(y) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            #plt.grid("")
            plt.cla()
            plt.plot(y,'#FAD8C1', label='Real-Time CPU Uses')
            ax.set_xticks([])

        else:
            plt.cla()
            plt.plot(y[-frame_len:], '#FAD8C1', label='Real-Time CPU Uses')

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Uses (%)')
        plt.legend(loc=1)
        plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.bind("<Return>", lambda event: None)  # changing the event when pressing enter.
    Root.mainloop()


def main():
    main_window()


if __name__ == "__main__":
    main()
