matplotlib.pyplot是一些命令行风格函数的集合，使matplotlib以类似于MATLAB的方式工作。每个pyplot函数对一幅图片(figure)做一些改动：比如创建新图片，在图片创建一个新的作图区域(plotting area)，在一个作图区域内画直线，给图添加标签(label)等。matplotlib.pyplot是有状态的，亦即它会保存当前图片和作图区域的状态，新的作图函数会作用在当前图片的状态基础之上。

```
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

上图的X坐标是1-3，纵坐标是1-4，这是因为如果你只提供给plot()函数一个列表或数组，matplotlib会认为这是一串Y值(Y向量)，并且自动生成X值(X向量)。而Python一般是从0开始计数的，所以X向量有和Y向量一样的长度(此处是4)，但是是从0开始，所以X轴的值为[0,1,2,3]。

  如果要显示的制定X轴的坐标，可以像如下一样：

plt.plot([1,2,3,4],[1,4,9,16])
  

  也可以给plt.plot()函数传递多个序列(元组或列表)，每两个序列是一个X,Y向量对，在图中构成一条曲线，这样就会在同一个图里存在多条曲线。

  为了区分同一个图里的多条曲线，可以为每个X,Y向量对指定一个参数来标明该曲线的表现形式，默认的参数是'b-'，亦即蓝色的直线，如果想用红色的圆点来表示这条曲线，可以：

```
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
```

  axis()函数接受形如[xmin,xmax,ymin,ymax]的参数，指定了X,Y轴坐标的范围。

  matplotlib不仅仅可以使用序列(列表和元组)作为参数，还可以使用numpy数组。实际上，所有的序列都被内在的转化为numpy数组。

```
import numpy as np
import matplotlib.pyplot as plt
t=np,arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')

```
  控制曲线的属性

  曲线有许多我们可以设置的性质：曲线的宽度，虚线的风格，抗锯齿等等。有多种设置曲线属性的方法：

  1.使用关键词参数：

>plt.plot(x,y,linewidth=2.0)

  2.使用Line2D实例的设置(Setter)方法。plot()返回的是曲线的列表，比如line1,line2=plot(x1,y1,x2,y2).我们取得plot()函数返回的曲线之后用Setter方法来设置曲线的属性。

>line,=plt.plot(x,y,'-')
>line.set)antialliased(False)  #关闭抗锯齿

  3.使用setp()命令：

```
lines=plt.plot(x1,y1,x2,y2)
plt.setp(lines,color='r',linewidth=2.0)
plt.setp(lines,'color','r','linewidth','2.0')
```

  处理多个图和Axe

  MATLAB和pyplot都有当前图和当前axe的概念。所有的作图命令都作用在当前axe。

  函数gca()返回当前axe，gcf()返回当前图。


```
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
```

  figure()命令是可选的，因为figure(1)会被默认创建，subplot(111)也会被默认创建。subplot()命令会指定numrows,numcols,fignum，其中fignum的取值范围为从1到numrows*numcols。如果numrows*numcols小于10则subplot()命令中的逗号是可选的。所以subplot(2,1,1)与subplot(211)是完全一样的。

  如果你想手动放置axe，而不是放置在矩形方格内，则可以使用axes()命令，其中的参数为axes([left,bottom,width,height])，每个参数的取值范围为(0,1)。

  你可以使用多个figure()来创建多个图，每个图都可以有多个axe和subplot：

```
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1,2,3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4,5,6])


plt.figure(2)                # a second figure
plt.plot([4,5,6])            # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1,2,3')   # subplot 211 title
```

  你可以使用clf()和cla()命令来清空当前figure和当前axe。

  如果你创建了许多图，你需要显示的使用close()命令来释放该图所占用的内存，仅仅关闭显示在屏幕上的图是不会释放内存空间的。

  处理文本

  text()命令可以用来在任意位置上添加文本，xlabel(),ylabel(),title()可以用来在X轴，Y轴，标题处添加文本。

```
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
```

  每个text()命令都会返回一个matplotlib.text.Text实例，就像之前处理曲线一样，你可以通过使用setp()函数来传递关键词参数来定制文本的属性。

>t=plt.xlabel('my data',fontsize=14,color='red')

  在文本中使用数学表达式

  matplotlib在任何文本中都接受Text表达式。

  Tex表达式是有两个dollar符号环绕起来的,比如的Tex表达式如下

>plt.title(r'$\sigma_i=15$')

参考链接：https://blog.csdn.net/hemuxiao/article/details/78491143
