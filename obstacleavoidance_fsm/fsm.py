#using finite state machine for object avoidance.
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.time import Time
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

#create a class that contains the main code.
class finite_state(Node):
    def __init__(self):
        super().__init__('fsm')
        self.pub = self.create_publisher(Twist,'/cmd_vel',10) #initilizing the publsiher.
        self.sub_laser_scan = self.create_subscription(LaserScan,'/scan',self.scan_callback,10)
        self.velocity_message = Twist()
        self.time = 0.05
        self.timer = self.create_timer(self.time,self.velocity_movement_cycle)
        self.laser_scan = None
        self.state_time = self.get_clock().now() #getting the clock time.

        #initilize the direction the robot should go when it sees an obstacle.
        self.forward = 0
        self.backward = 1
        self.turn = 1
        self.stop = 3
        self.state = self.forward #The state of the robot is equals to the robot driving forward.

        #The linear and angular velocity speed ot the robot.
        self.liner_speed = 0.3 #robot drives forward.
        self.angular_speed = 0.3 #robot drives/turn right(z axis)
        self.distance_of_obstacle = 1.0 #distance of obstacle from the robot.


    def scan_callback(self,data):
        self.laser_scan == data
          
    
    def velocity_movement_cycle(self):
        if self.laser_scan == None:
            return  #return nothing(execute nothing)
        
        self.velocity_message = Twist()
        # self.pub.publish(self.velocity_message) #publish to the wheel of the robot.
        if self.state == self.forward:
            self.velocity_message.linear.x = self.liner_speed
        

def main(args=None):
    rclpy.init(args=args)
    store = finite_state()
    store.velocity_movement()
    rclpy.spin(store)


if __name__ == '__main__':
    main()

    

