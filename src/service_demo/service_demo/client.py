import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ClientNode(Node):
    def __init__(self):
        super().__init__("my_client_node")
        # 创建客户端: 服务类型，服务名称（名字必须和服务端完全一致）
        self.client = self.create_client(SetBool, "set_bool_service")

        # 等待服务上线，最多等待3秒
        while not self.client.wait_for_service(timeout_sec=3.0):
            self.get_logger().warn("服务还没上线，继续等待...")

    def send_request(self, req_data):
        # 1.构造请求对象
        request = SetBool.Request()
        request.data = req_data
        # 2.发送同步请求，阻塞等待返回结果
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        # 拿到应答
        if future.result() is not None:
            res = future.result()
            self.get_logger().info(f"收到服务端结果 success:{res.success}, message:{res.message}")
        else:
            self.get_logger().error("服务调用失败！")
            
def main():
    rclpy.init()
    node = ClientNode()
    # 发送请求，参数True
    node.send_request(True)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
