import socket

# 创建一个socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("localhost", 8080))

while True:
    # 发送数据
    msg = input("请输入要发送的数据：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("utf-8"))
    # 接收数据
    recv_data = socket_client.recv(1024)  # 1024是缓冲区大小
    print("接收到的数据：", recv_data.decode("utf-8"))
# 关闭连接
socket_client.close()
