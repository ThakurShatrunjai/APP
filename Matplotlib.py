from matplotlib import pyplot as plt
plt.plot([1,2,5,10],[10,13,16,20])
plt.show()


plt.plot([1,2,5,10],[10,13,16,20])
plt.title('Matplot Example')
plt.show()



from matplotlib import style
style.use('ggplot')
x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]
x2 = [5,10,15,20,25]
y2 = [15,20,25,30,35]
plt.plot(x1,y1,label='Line 1')
plt.plot(x2,y2,label='Line 2')
plt.title('Matplot Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

