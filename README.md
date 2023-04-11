# Obstacle-avoidance-with-F.S.M-Finite-State-Machines-Using-ROS-2
This repository shows a robot which is able to avoid obstacles using a finite state machine,this is a very important field or aspect of mobile robotics. A back bone of autonomous control,as this makes or allow a robot be ale to reach it's destination without collusion.This algorithm is widely/mostly used in path planning.


# OBSTACLE AVOIDANCE USING F.S.M ROS 2.
The robot is able to detect an object in front of it,using the finite state machine procedure.



[Screencast from 03-19-2023 06:14:19 PM.webm](https://user-images.githubusercontent.com/97457075/226195951-c09fc38c-e9b9-4504-93a7-262247213e6f.webm)

[Screencast from 03-19-2023 07:55:31 PM.webm](https://user-images.githubusercontent.com/97457075/226200771-dd0ef50d-85e2-4891-b23a-7a013f97dcdd.webm)

NOTE: THE .cpp Node in the package is a ros1 node,that does the same task.

TASK: The robot turns exactly to the angle with no obstacles or the left and right.Instead of the robot always turning to the same side,it turns to the right or the left with no obstacle.


[avoid.webm](https://user-images.githubusercontent.com/97457075/226737749-47f27146-1c86-4cce-8efc-7ec714f71df7.webm)



[avoid5.webm](https://user-images.githubusercontent.com/97457075/226737826-bb44243f-713a-4288-97c9-016a33cd61ca.webm)

# USING TF2 Link from parent_frame to child_frame in avoiding an obstacle:
```
  ros2 run obstacleavoidance_fsm transform_object_detector
```
[Screencast from 04-09-2023 01:35:57 AM.webm](https://user-images.githubusercontent.com/97457075/230748322-f0a72433-0f08-4992-803e-72236b07fe29.webm)

# USING RVIZ 2 VISUAL MARKER.
  You can publish numerous markers simultaneously by using the visualization_msgs/MarkerArray message, which is also available. The visualization_marker_array topic is where you want to post in this situation.To install the package.
 
 ```
   sudo apt-get install ros-<ros_distro>-rviz-visual-tools 
 ```
 Run the Node:
 ```
   ros2 run obstacleavoidance_fsm marker_detection 
 ```
 
  

https://user-images.githubusercontent.com/97457075/231242907-72554731-65c4-40b1-b64e-4d89dad36690.mp4


