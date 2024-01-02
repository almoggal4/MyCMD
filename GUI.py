# Imports:
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from psutil import cpu_percent,net_io_counters,virtual_memory, disk_io_counters
import matplotlib
import pathlib

#  Backgrounds:
BACKGROUND_MAIN_TASK_MANGER = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "main_TM.png"
BACKGROUND_MAIN = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "main.png"
BACKGROUND_CPU = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "cpu_background.png"
BACKGROUND_RAM = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "ram_background.png"
BACKGROUND_STORAGE = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "storage_background.png"
BACKGROUND_NETWORK = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "network_background.png"

#  Buttons:
BUTTON_START = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "start.png"
BUTTON_CPU = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "cpu.png"
BUTTON_RAM = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "ram.png"
BUTTON_STORAGE = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "storage.png"
BUTTON_NETWORK = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "network.png"
BUTTON_BACK = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "back.png"
BUTTON_HOME = str(pathlib.Path(__file__).parent.resolve()) + "\\photos\\" + "home.png"

# Create basic window.
Root = tk.Tk()
Root.resizable(0, 0)

# Network and storage settings
KB = float(1024)
last_write, write_speed = 0, 0
last_upload, last_download, upload_speed, down_speed = 0, 0, 0, 0


def main_window(background=BACKGROUND_MAIN_TASK_MANGER):
    """
    The main windows of the app.
    :param background: the background of each page
    :return:
    """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Start button
    start_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_START))
    button_start = tk.Button(Root, font=40, image=start_image_tk, borderwidth=0, activebackground='black',
                             command=(lambda: options_window()))
    button_start.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.16)
    button_start.config(bg="black")

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def close_window():
    """
    Close the window.
    :return:
    """
    Root.quit()
    Root.destroy()
    return


def options_window(background=BACKGROUND_MAIN):
    """
    The page that show the options of monitor.
    :param background:
    :return:
    """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # CPU button
    cpu_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_CPU))
    button_cpu = tk.Button(Root, font=40, image=cpu_image_tk, borderwidth=0, activebackground='black',
                           command=(lambda: cpu_page(BACKGROUND_CPU)))
    button_cpu.place(relx=0.25, rely=0.15, relheight=0.32, relwidth=0.25)
    button_cpu.config(bg="black")

    # RAM button
    ram_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_RAM))
    button_ram = tk.Button(Root, font=40, image=ram_image_tk, borderwidth=0, activebackground='black',
                           command=(lambda: ram_page(BACKGROUND_RAM)))
    button_ram.place(relx=0.25, rely=0.55, relheight=0.32, relwidth=0.25)
    button_ram.config(bg="black")

    # Storage button
    storage_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_STORAGE))
    button_storage = tk.Button(Root, font=40, image=storage_image_tk, borderwidth=0, activebackground='black',
                               command=(lambda: storage_page(BACKGROUND_STORAGE)))
    button_storage.place(relx=0.5, rely=0.15, relheight=0.32, relwidth=0.25)
    button_storage.config(bg="black")

    # Network button
    network_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_NETWORK))
    button_network = tk.Button(Root, font=40, image=network_image_tk, borderwidth=0, activebackground='black',
                               command=(lambda: network_page(BACKGROUND_NETWORK)))
    button_network.place(relx=0.5, rely=0.55, relheight=0.32, relwidth=0.25)
    button_network.config(bg="black")

    # Home button
    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def cpu_page(background):
    """
    This function displays the CPU page and the CPU usage live graph.
    :param background: The background of the page
    :return:
    """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Back to options window button
    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    # Back to home window button
    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    # Define a graph area.
    fig = plt.Figure(facecolor='black')
    y_vals = [] # Y values
    matplotlib.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(8, 3))

    def animate(i):
        """
        This function create a live plot graph of cpu uses.
        :param i: the interval when to check the cpu uses.
        :return:
        """
        y_vals.append(cpu_percent())
        ax = plt.axes()
        ax.set_facecolor("black")
        ax.clear()
        plt.cla() # Clear the graph.
        plt.plot(y_vals, '#FAD8C1', label='Real-Time CPU Uses')
        ax.set_xticks([])

        # Design setting.
        plt.ylim(0, 100)
        plt.xlabel('Time (s)') # X label
        plt.ylabel('CPU Uses (%)') # Y lebel
        plt.legend(loc=1)
        plt.tight_layout()

    # tkinter widget for matplotlib
    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def get_gb(value):
    """
    Convert given value in bytes to GB
    """

    value /= (1028 ** 3)
    return f"{value:.2f}"


def ram_page(background):
    """
        This function displays the RAM page and the RAM usage live graph.
        :param background: The background of the page
        :return:
        """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Back to options window button
    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    # Back to home window button
    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    # Define a graph area.
    fig = plt.figure(facecolor='black')
    ax1 = fig.add_subplot(1, 1, 1)
    labels = ['used', 'free']

    def animate(i):
        """
        This function create a live pie graph of ram uses.
        :param i: the interval when to check the ram uses.
        :return:
        """

        # Pie graph : the memory used and free.
        nums = [float(get_gb(virtual_memory().used)), float(get_gb(virtual_memory().free))]
        ax1.clear()
        ax1.pie(nums, labels=labels, autopct='%1.1f%%', colors=["#FAD8C1", "#D4E6C7"])
        ax1.legend(loc=2)

        # Refresh the pie
        plt.draw()

    # tkinter widget for matplotlib
    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def storage_page(background):
    """
        This function displays the storage page and the storage usage live graph.
        :param background: The background of the page
        :return:
        """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Back to options window button
    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    # Back to home window button
    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")

    # Define a graph area.
    plt.style.use('fivethirtyeight')
    write_vals = []
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120

    def animate(i):
        """
        Function that create graph with live data.
        :param i:
        :return:
        """
        counter = disk_io_counters()
        global last_write, write_speed

        write = counter.write_bytes

        # speed calculation:
        # if there is a slowdown, the speed will be 0
        # else, the speed is: current bytes-last bytes
        if last_write > 0:
            if write < last_write:
                write_speed = 0
            else:
                write_speed = float((write - last_write) / KB)

        last_write = write

        write_vals.append(write_speed)

        ax = plt.axes()
        ax.set_facecolor("black")
        ax.clear()
        plt.cla()
        plt.plot(write_vals, '#D4E6C7', label='Write')
        ax.set_xticks([])

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('Write Speed (KB/s)')
        plt.legend(loc=1)
        plt.tight_layout()

    # tkinter widget for matplotlib
    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1500)

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def network_page(background):
    """
        This function displays the network page and the network usage live graph.
        :param background: The background of the page
        :return:
        """
    # This loop destroy every widget in the previous page.
    for widget in Root.winfo_children():
        widget.destroy()

    # Background
    image = Image.open(background)
    width, height = image.size
    my_canvas = tk.Canvas(Root, width=width, height=height)
    my_canvas.pack()

    Root.title("Task Manger")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(Root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Back to options window button
    back_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_BACK))
    button_back = tk.Button(Root, font=40, image=back_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: options_window()))
    button_back.place(relx=0.02, rely=0.8, relheight=0.17, relwidth=0.1)
    button_back.config(bg="black")

    # Back to home window button
    home_image_tk = ImageTk.PhotoImage(Image.open(BUTTON_HOME))
    button_home = tk.Button(Root, font=40, image=home_image_tk, borderwidth=0, activebackground='black',
                            command=(lambda: main_window()))
    button_home.place(relx=0.88, rely=0.02, relheight=0.17, relwidth=0.1)
    button_home.config(bg="black")


    plt.style.use('fivethirtyeight')

    # list of network upload speed values
    upload_vals = []
    # list of network download speed values
    download_vals = []

    # Define a graph area.
    fig = plt.figure(figsize=(8, 3))
    frame_len = 120

    def animate(i):
        """
        Function that create graph with live data.
        :param i:
        :return:
        """
        counter = net_io_counters()
        global last_upload, last_download, upload_speed, down_speed

        # get network sent bytes
        upload = counter.bytes_sent
        # get network receive bytes
        download = counter.bytes_recv

        # speed calculation:
        # if it's not the first sampling ->
        # check if there is a slowdown, the speed will be 0
        # else, the speed will be: current bytes-last bytes and turn it into KB
        if last_upload > 0:
            if upload < last_upload:
                upload_speed = 0
            else:
                upload_speed = float((upload - last_upload) / KB)

        if last_download > 0:
            if download < last_download:
                down_speed = 0
            else:
                down_speed = float((download - last_download) / KB)

        # update the last network upload bytes
        last_upload = upload
        # update the last network download bytes
        last_download = download

        # add the current upload speed value
        upload_vals.append(upload_speed)
        # add the current download speed value
        download_vals.append(down_speed)

        # define graph area
        ax = plt.axes()
        ax.set_facecolor("black")
        ax.clear()
        plt.cla()
        plt.plot(upload_vals, '#D4E6C7', label='Send', linestyle='--')
        plt.plot(download_vals, '#FAD8C1', label='Receive')
        ax.set_xticks([])

        # design settings
        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('Network Speed (KB/s)')
        plt.legend(loc=1)
        plt.tight_layout()

    # tkinter widget for matplotlib
    canvas = FigureCanvasTkAgg(fig, master=Root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

    ani = animation.FuncAnimation(fig, animate, interval=1000)

    # If the window get closed
    Root.protocol('WM_DELETE_WINDOW', lambda: close_window())
    Root.mainloop()


def main():
    main_window()


if __name__ == "__main__":
    main()
