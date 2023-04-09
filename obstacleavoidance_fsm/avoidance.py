import rclpy 
from sensor_msgs.msg import LaserScan
from rclpy.node import Node



class avoidancee(Node):
    def __int__(self):
        super().__init__("avoidance")
        self.laser_sub = self.create_subscription(LaserScan,'/scan',self.laser_callback,10)
        # self.time = 0.05
        # self.timer = self.create_timer(self.time)
        


    def laser_callback(self,msg):
        self.get_logger().info('The reading of laser sensor is : "%s"' %msg.ranges)



def main(args=None):
    rclpy.init(args=args)
    laser= avoidancee()
    rclpy.spin(laser)



if __name__ =='__main__':
    main()