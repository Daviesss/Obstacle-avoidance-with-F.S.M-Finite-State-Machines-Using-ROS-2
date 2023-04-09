import rclpy
from geometry_msgs.msg import Twist,TransformStamped
from rclpy.node import Node 
from sensor_msgs.msg import LaserScan
from tf2_msgs.msg import TFMessage

class Movement(Node):
    def __init__(self):
        super().__init__('obstacle')
        self.pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.sub = self.create_subscription(LaserScan,'/scan', self.call_back,10)
        self.pub_transform = self.create_publisher(TransformStamped,'/cmd_vel',10)
        self.velocity_message = Twist()
        self.transform = TransformStamped()

        
    #call_back function.
    def call_back(self,msg):
        self.get_logger().info('The laser scan message is: "%f"' %msg.ranges[100])
        distance = msg.ranges[100]/2
        if distance:
            self.transform.header = msg.header 
            self.transform.child_frame_id = "right_wheel"
            self.transform.transform.translation.x = msg.ranges[100]/2
            self.pub_transform.publish(self.transform)

def main(args=None):
    rclpy.init(args=args)
    store = Movement()  
    rclpy.spin(store)



if __name__ == '__main__':
    main()


        


