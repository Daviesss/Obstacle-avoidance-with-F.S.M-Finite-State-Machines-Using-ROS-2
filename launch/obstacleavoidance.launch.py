from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pub_cmd = Node(
        package='obstacleavoidance_fsm',
        executable='finite_state',
        output='screen')

    ld = LaunchDescription() #created an object called ld.
    ld.add_action(pub_cmd) #calling the pub_cmd object that launches the node.

    return ld
