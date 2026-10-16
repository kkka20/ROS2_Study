import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ServerNode(Node):
    def __init__(self):
        super().__init__("my_server_node")
        # 创建服务: 服务类型,服务名字,收到请求的回调函数
        self.srv = self.create_service(
            SetBool,
            "set_bool_service",
            self.service_callback
        )
        self.get_logger().info("服务端已经启动，等待客户端请求...")

    # 服务回调: request=客户端发来请求，response=要返回给客户端的结果
    def service_callback(self, request, response):
        self.get_logger().info(f"收到客户端请求，data={request.data}")
        # 业务逻辑
        if request.data:
            response.success = True
            response.message = "收到，执行成功！"
        else:
            response.success = False
            response.message = "收到，执行失败！"
        return response

def main():
    rclpy.init()
    node = ServerNode()
    rclpy.spin(node) # spin驱动服务回调执行!必不可少
    rclpy.shutdown()

if __name__ == "__main__":
    main()
