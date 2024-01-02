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

    fig = plt.figure(facecolor='black')
    ax1 = fig.add_subplot(1,1,1)
    labels=['used','free']

    def animate(i):

        
        
            
        nums=[float(get_gb(virtual_memory().used)),float(get_gb(virtual_memory().free))]
        ax1.clear()
        ax1.pie(nums, labels=labels, autopct='%1.1f%%',colors=["#FAD8C1", "#D4E6C7"])
        
        
        ax1.legend(loc=2)
        plt.draw()
    
    
   
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()

    

if __name__ == "__main__":
    main()
