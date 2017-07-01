import urllib.request as ur
from matplotlib import pyplot as plt
from matplotlib import animation
def get_data():
    try:
        data=ur.urlopen("http://这里换成自己获得的ip/").read()
    except Exception as err:
        return (float(str(err)))


def data_gen():
    total_data = []
    x = []
    r = 0
    while 1:
        total_data.append(get_data())#这里的get_data就是上面的函数
        x.append(r)#这个r可以改成当前时间
        r += 1
        time.sleep(.1)
        yield float(x[-1]) ,float(total_data[-1]) #每次yield列表的最后一个元素，考虑到数据最后要存储到文本中。
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 70)#设置scale
ax.set_xlim(0, 5)
ax.grid()
xdata, ydata = [], []
def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    ax.set_xlim(t-50, t)#这里设置图像的范围，具体效果运行一下就知道了
    ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,
ani = animation.FuncAnimation(fig, run,data_gen, blit=True, interval=.1,
                              repeat=False)
plt.show()