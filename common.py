import struct
# 读取包的二进制数据为一个列表

def read_one_message(f):
    # 读取版本号 (1 byte)
    version_data = f.read(1)
    if not version_data:
        return ""  # 到达文件末尾
    version = struct.unpack('b', version_data)[0]
    if version != 1:
        print(f"不支持的版本号: {version}")
        return ""

    # 读取时间戳 (8 bytes)
    timestamp_data = f.read(8)
    if len(timestamp_data) < 8:
        print("文件末尾或读取时间戳失败")
        return ""
    timestamp = struct.unpack('d', timestamp_data)[0]
    # print(f"时间戳: {timestamp}")  # 如果需要打印时间戳

    # 读取数据段长度 (2 bytes)
    data_length_data = f.read(2)
    if len(data_length_data) < 2:
        print("文件末尾或读取数据段长度失败")
        return ""
    data_length = struct.unpack('h', data_length_data)[0]

    # 检查是否有足够的剩余字节读取数据负载
    payload_data = f.read(data_length)
    if len(payload_data) < data_length:
        print("文件中剩余字节不足，文件可能不完整")
        return ""
    return payload_data

def get_messages(filename):
    result = []
    with open(filename, 'rb') as file:
        while True:
            message = read_one_message(file)
            if message == "":#返回空消息错误
                return result
            result.append(message)
    return result



# # main 测试函数
# def main():
#     filename = "bag/20230927101833_local_path.mbag"  # 请根据实际路径修改文件名
#     messages = get_messages(filename)

#     if not messages:
#         print("没有读取到任何消息")
#     else:
#         print(f"成功读取了 {len(messages)} 条消息。")
#         for idx, msg in enumerate(messages):
#             print(f"Message {idx + 1}: {msg}")

# # 执行 main 函数
# if __name__ == "__main__":
#     main()