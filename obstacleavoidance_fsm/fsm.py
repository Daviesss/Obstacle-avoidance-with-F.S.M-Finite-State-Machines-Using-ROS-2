#implementing finite state machine , obstacle avoidance(rclpy)
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from rclpy.time import Time
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#create a class that stores all Node.
class object_bump_and_go_node(Node):
    def __init__(self):
        super().__init__('BumpandGo')
        self.pub = self.create_publisher(Twist,'/cmd_vel',100)
        self.sub_laser = self.create_subscription(LaserScan,'/scan',self.call_back_laser,10)
        self.velocity_message = Twist()
        self.laser_scan = None
        self.time = 0.05
        self.timer = self.create_timer(self.time,self.velocity_movement)


    #Subscribing to the laser_scan data.
    def call_back_laser(self,data):
        self.laser_scan = data
    def velocity_movement(self):
        if self.laser_scan ==  None:
            return 
        
        self.velocity_message = Twist() #storing the twist message into a variable
        self.pub.publish(self.velocity_message)

#The main function.
def main(args=None):
    rclpy.init(args=args)
    store = object_bump_and_go_node()
    rclpy.spin(store)
    #rclpy.shutdown()



if __name__ == '__main__':
    main()


    

