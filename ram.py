from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
from psutil import virtual_memory

def get_gb(value):

    """
    convert given value in bytes to GB
    """

    value /= (1028 ** 3)
    return f"{value:.2f}"

def main():

    virtual_memory()
    plt.style.use('fivethirtyeight')
    y_vals = []
    fig = plt.figure(figsize=(8,3))
    
    index = count()
    frame_len = 120

    def animate(i):
        """
        A function that creates a graph with live data
        of computer's memory.
        
        """
        y_vals.append(float(get_gb(virtual_memory().used)))
        if len(y_vals) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            plt.grid("")
            plt.cla()
            plt.plot(y_vals, '#FAD8C1', label= 'Real-Time Memory Usage')
            ax.set_xticks([])
        else:
            plt.cla()
            plt.plot(y_vals[-frame_len:], '#FAD8C1', label = 'Real-Time Memory Usage')

        

        plt.ylim(0, float(get_gb(virtual_memory().total)))
        plt.xlabel('Time (s)')
        plt.ylabel('Memory Usage (GB)')
        plt.legend(loc=1)
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()
   



if __name__ == "__main__":
    main()
