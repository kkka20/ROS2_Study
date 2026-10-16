import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__ (self):
        super().__init__("talker_node")
        self.pub=self.create_publisher(String,"/chatter",10)
        self.timer_period=0.5
        self.timer=self.create_timer(self.timer_period,self.timer_callback)
        self.count=0

    def timer_callback(self):
        msg=String()
        msg.data=f"hello ros2{self.count}"
        self.pub.publish(msg)
        self.get_logger().info(f"发布:{msg.data}")
        self.count+=1

def main():
    rclpy.init()
    node=TalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
     main