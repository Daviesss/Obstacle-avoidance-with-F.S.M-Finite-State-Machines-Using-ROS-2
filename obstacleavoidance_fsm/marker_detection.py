# using tf2 laser_scan to detect an object
import rclpy
from rclpy.node import Node  
from geometry_msgs.msg import Twist ,TransformStamped,Point
from sensor_msgs.msg import LaserScan 
from visualization_msgs.msg import Marker #Rviz marker library
from rclpy.duration import Duration
from rclpy.clock import Clock
import tf2_ros
from tf2_ros import TransformListener #listens to the tf2 topic.
import numpy as np 
from math import pi 
import time

class Avoid_obstacle(Node):
    def __init__(self):
        super().__init__('obstacle_detector_using_tf2')
        self.sub_laser = self.create_subscription(LaserScan,'/scan',self.laser_callback,qos_profile=10)
        self.velocity_pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.marker = self.create_publisher(Marker,'/Rviz_marker',10) #publish marker.
        self.clock = self.get_clock()
        self.velocity_message = Twist()
        self.duration = Duration()
        self.transform_stamped = TransformStamped()
        self.tf2_buffer = tf2_ros.Buffer()
        self.tf2_listener = tf2_ros.TransformListener(self.tf2_buffer,self) # Transform listener
        self.time = time.time()
        self.rate = self.create_rate(10) #Hz 
        self.get_logger().info('The Node is about to start reading....')
        
    def view_marker(self):
        self.marker_object = Marker()
        self.marker_object.header.frame_id = "laser_frame" #frame of the sensor
        # self.marker_object.header.stamp = self.clock.now() #get clock function(ros 2 time)
        self.marker_object.ns = "robot_namespace"
        self.marker_object.id = 0
        self.marker_object.type = Marker.ARROW #specify the shape of the marker
        self.marker_object.action = Marker.ADD 
        self.geometry_point = Point()
        self.geometry_point.z = 0.0
        self.marker_object.pose.position = self.geometry_point
        

        #Publish the marker from the "laser_frame" to the object
        self.marker_object.pose.position.x = 0.0
        self.marker_object.pose.position.y = 0.0
        self.marker_object.pose.position.z = 0.0
        # self.marker_object.pose.position.w = 0
        self.marker_object.scale.x = 0.7 #reduce the scale lesser, if you feel its too big
        self.marker_object.scale.y = 0.7
        self.marker_object.scale.z = 0.7

        #r,g,b color for the marker
        self.marker_object.color.r = 0.0
        self.marker_object.color.g = 0.0
        self.marker_object.color.b = 1.0

        self.marker_object.color.a = 1.0 #set so arrow becomes visible
        # self.marker_object.lifetime = rclpy.duration.Duration(0)

        while True:
            self.marker.publish(self.marker_object)


    def laser_callback(self,scan_msg):
        self.get_logger().info('Reading laser scan messages:"%s"' %scan_msg.ranges)
        #Look up at the tranform from base_link to laser_frame of the robot
        #transform = self.tf2_buffer.lookup_transform("base_link","laser_frame",rclpy.self.time)
        
        #converting the laser readings with a numpy array.
        self.ranges = np.array(scan_msg.ranges)

        #We create an empty list 
        transform_ranges = []

        #Loop through to transform the laser_frame(child_frame) to the base_link(parent_frame)
        for rangee in self.ranges:
            #transition = transform.transform_point(rangee)
            transform_ranges.append(rangee)

        #We check if there is an obstacle in front of the robot at 1m 
        if np.min(transform_ranges) < 1:
            self.velocity_message.linear.x = 0.0
            self.velocity_message.angular.z = 0.2
            self.get_logger().info('Robot turns at velocity speed of:'+str(0.2))
           
        else:
            self.velocity_message.linear.x = 0.2
            self.velocity_message.angular.z = 0.0
            self.get_logger().info('Robot moves forward at velocity speed of:'+str(0.2))
            

        self.velocity_pub.publish(self.velocity_message)

def main(args=None):
    rclpy.init(args=args)
    store = Avoid_obstacle()
    store.view_marker()
    rclpy.spin(store)

if __name__ == '__main__':
    main()