# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import websockets
import os, base64

# 检测客户端权限，用户名密码通过才能退出循环
async def check_permit(websocket):
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        if cred_dict[0] == "admin" and cred_dict[1] == "123456":
            response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
            print("连接成功")
            await websocket.send(response_str)
            return True
        else:
            response_str = "sorry, the username or password is wrong, please submit again"
            await websocket.send(response_str)


# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    count = 0
    while True:
        recv_text = await websocket.recv()
        print(recv_text)
        data = recv_text.split(',')[1]
        image_data = base64.b64decode(data)
        count = count + 1
        print(count)
        with open('datasets/server/' + str(count)+'.jpg', 'wb') as f:
            f.write(image_data)
        response_text = f"your submit context: {count}"
        await websocket.send(response_text)


# 服务器端主逻辑
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket, path):
    await check_permit(websocket)

    await recv_msg(websocket)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 把ip换成自己本地的ip
    start_server = websockets.serve(main_logic, '127.0.0.1', 5678)
    # 如果要给被回调的main_logic传递自定义参数，可使用以下形式
    # 一、修改回调形式
    # import functools
    # start_server = websockets.serve(functools.partial(main_logic, other_param="test_value"), '10.10.6.91', 5678)
    # 修改被回调函数定义，增加相应参数
    # async def main_logic(websocket, path, other_param)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
