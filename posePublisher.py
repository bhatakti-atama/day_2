#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Pose

def talker():
    pub = rospy.Publisher('/odom', Pose, queue_size=10)
    rospy.init_node('positionPublisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        position = Pose()
        position.position.x = 5
        position.position.y = 5
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass