# Part-B
---привет.  
---здесь мы объясняем как  запустить нашу работу  
---Нужно скачать архив и 3 файла перенести в папку scripts  на виртуалке.  
---далее нужно открыть терминал написать roscore и написать след команды для запуска   
---естетвенно все скрипты нужно сделать исполняемыми chmod +x *  
---далее мы пишем $ rosrun beginner_tutorials listener.py для запуска listening  
---Полсе этого открываем новое окно терминала и пишем $ export TURTLEBOT3_MODEL=waffle; roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch в одну строку для запуска робота  
---Потом пишем в новом окне терминала  rosrun beginner_tutorials Nodule2.py для запуска Nodule2 Подробнее описанно в отчете для чего каждый файл.  
---А так же можно написать в новом окне rosrun rqt_graph rqt_graph для запуска графа и просмотря связей между узлами  
---Теперь код---

```Listening.py

#!/usr/bin/env python  
import rospy  
from std_msgs.msg import Float32,String  
from geometry_msgs.msg import Twist  
Inc1=0  
Inc2=0  
def callback(data):  
    global Inc1  
    global Inc2  
    rospy.loginfo(data.linear)  
    rospy.loginfo(data.angular)  
    pub1 = rospy.Publisher('inc1', Float32, queue_size=10)  
    pub2 = rospy.Publisher('inc2', Float32, queue_size=10)  
    Inc1=Inc1+1  
    Inc2=Inc2+1  
    pub1.publish(Float32(Inc1))  
    pub2.publish(Float32(Inc2))  
   
def listener():  
    rospy.init_node('Robotsim', anonymous=True)  
    rospy.Subscriber('cmd_vel', Twist, callback, queue_size=10)  
     # spin() simply keeps python from exiting until this node is stopped  
    rospy.spin()  

if __name__ == '__main__':  
    try:  
    	listener()  
    except rospy.ROSInterruptException:  
        pass  
 ```       
Nodule2 
```
#!/usr/bin/env python  
import rospy  
from std_msgs.msg import Float32,String  

def callback1(data):  
    rospy.loginfo(rospy.get_caller_id() + "Inc1 %s", data.data)  
def callback2(data):  
    rospy.loginfo(rospy.get_caller_id() + "Inc2 %s", data.data)  
def listener():  
    rospy.init_node('Nodule2', anonymous=True)  
    rospy.Subscriber("inc1",Float32, callback1, queue_size=10)  
    rospy.Subscriber("inc2",Float32, callback2, queue_size=10)  
    # spin() simply keeps python from exiting until this node is stopped  
    rospy.spin()  

if __name__ == '__main__':  
    listener() 
    ```
