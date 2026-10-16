import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__("listener_node")
        # 创建订阅者：消息类型、话题名、收到消息后的回调函数、QoS
        self.sub = self.create_subscription(
            String,
            "/chatter",
            self.msg_callback,
            10
        )

    # 收到话题消息，自动执行这个回调，msg就是收到的数据
    def msg_callback(self, msg):
        self.get_logger().info(f"收到消息: {msg.data}")

def main():
    rclpy.init()
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
