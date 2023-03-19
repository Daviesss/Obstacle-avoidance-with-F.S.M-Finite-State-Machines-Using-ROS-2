import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist

class finite_state(Node):
    def __init__(self):
        super().__init__("finite_state")
        self.pub = self.create_publisher(Twist,'/cmd_vel',100)
        self.velocity_message = Twist()
        self.msg = 0.2
        
        

    def movement(self):
        print("The speed of the robot is",self.msg)
        self.velocity_message.linear.x = self.msg
        self.pub.publish(self.velocity_message)

    
#main function.
def main(args=None):
    rclpy.init(args=args)
    store = finite_state()
    store.movement()
    rclpy.spin(store)


if __name__ == '__main__':
    main()


        
