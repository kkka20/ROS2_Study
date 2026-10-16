from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    talker_node = Node(
        package="my_pkg",
        executable="hello",
        name="my_talker",
        output="screen"
    )

    listener_node = Node(
        package="my_pkg",
        executable="class_node",
        name="my_listener",
        output="screen"
    )

    return LaunchDescription([
        talker_node,
        listener_node
    ])
