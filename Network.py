from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
from psutil import net_io_counters

from network import size

KB = float(1024)
last_upload, last_download, upload_speed, down_speed = 0, 0, 0, 0

def main():

    plt.style.use('fivethirtyeight')
    upload_vals = []
    download_vals = []
    fig = plt.figure(figsize=(8,3))
    index = count()
    frame_len = 120

    def animate(i):
        """
        Function that create graph with live data.
        :param i:
        :return:
        """
        counter = net_io_counters()
        global last_upload, last_download, upload_speed, down_speed
        print(counter)

        upload = counter.bytes_sent
        download = counter.bytes_recv

        print(upload)
        print(download)

        # spead calculation:
        # if there is a slowdown, the spead will be 0
        # else, the spead is: current bytes-last bytes
        if last_upload > 0:
            if upload < last_upload:
                upload_speed = 0
            else:
                upload_speed = float((upload - last_upload)/KB)

        if last_download > 0:
            if download < last_download:
                down_speed = 0
            else:
                down_speed =float((download - last_download)/KB)

        last_upload = upload
        last_download = download

        print(upload_speed, type(upload_speed))
        print(down_speed)

        upload_vals.append(upload_speed)
        download_vals.append(down_speed)

        if len(download_vals) <= frame_len and len(upload_vals) <= frame_len:
            """
            after 2 min clear the graph
            """
            ax = plt.axes()
            ax.set_facecolor("black")
            ax.clear()
            plt.grid("")
            plt.cla()
            plt.plot(upload_vals, '#D4E6C7', label= 'Send', linestyle = '--')
            plt.plot(download_vals, '#FAD8C1', label= 'Receive')
            ax.set_xticks([])
        else:
            plt.cla()
            plt.plot(upload_vals, '#D4E6C7', label= 'Send', linestyle = '--')
            plt.plot(download_vals, '#FAD8C1', label= 'Receive')

        plt.ylim(0, 100)
        plt.xlabel('Time (s)')
        plt.ylabel('Network Speed (KB/s)')
        plt.legend(loc=1)
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()

if __name__ == "__main__":
    main()
