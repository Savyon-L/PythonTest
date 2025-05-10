import socket

# 创建一个socket对象
socket_server = socket.socket()

# 绑定IP和端口
socket_server.bind(("localhost", 8080))

# 监听连接
socket_server.listen(1)#listen(1)表示最多允许一个连接

# 等待连接，accept()返回二元元组（连接对象，客户端地址信息）
conn, address = socket_server.accept()#conn是客户端和服务端连接对象，address是客户端的地址
#accept()会阻塞代码在这一行，直到有客户端连接
print(f"连接成功，客户端地址：{address}")

while True:
    # 接收数据,要使用客户端和服务端的本次链接对象，而非socket_server对象
    data: str = conn.recv(1024).decode("utf-8")#1024表示接收的最大字节数
    #recv()方法的返回值是一个字节数组也就是bytes类型，可以通过decode()方法转换为字符串
    print("接收到的数据：", data)
    # 发送数据
    msg = input("请输入要发送的数据：")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))

# 关闭连接
conn.close()
# 关闭socket_server
socket_server.close()


