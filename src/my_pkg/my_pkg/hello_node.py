import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node=Node("node_v")
    node.get_logger().info("hello ros2")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main