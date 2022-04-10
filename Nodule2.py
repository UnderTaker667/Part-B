#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32,String

def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "Inc1 %s", data.data)
def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "Inc2 %s", data.data)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Nodule2', anonymous=True)

    rospy.Subscriber("inc1",Float32, callback1, queue_size=10)
    rospy.Subscriber("inc2",Float32, callback2, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
