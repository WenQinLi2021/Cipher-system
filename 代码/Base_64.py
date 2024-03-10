import base64

# 定义Base64编码函数
def encode_to_base64(input_text):
    # 将输入字符串转换为字节
    input_bytes = input_text.encode('utf-8')
    # 对字节进行Base64编码
    encoded_bytes = base64.b64encode(input_bytes)
    # 将编码后的字节转换回字符串
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

# 定义Base64解码函数
def decode_from_base64(encoded_text):
    # 将编码后的字符串转换为字节
    encoded_bytes = encoded_text.encode('utf-8')
    # 尝试对字节进行Base64解码
    try:
        decoded_bytes = base64.b64decode(encoded_bytes)
        # 将解码后的字节转换回字符串
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except base64.binascii.Error as e:
        # 返回错误信息
        return f"An error occurred: {str(e)} - This may indicate the input is not properly Base64 encoded."
def main():
    # 测试编码和解码
    original_text = "135052021091 李文钦 fjnu"
    print("原文: ", original_text)

    # 编码
    encoded_text = encode_to_base64(original_text)
    print("编码后：: ", encoded_text)

    # 解码
    decoded_text = decode_from_base64(encoded_text)
    print("解码后： ", decoded_text)

    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    print("原文：", plaintext)
    # 编码
    encoded_text = encode_to_base64(plaintext)
    print("编码后：: ", encoded_text)

    # 解码
    decoded_text = decode_from_base64(encoded_text)
    print("解码后： ", decoded_text)

if __name__ == "__main__":
    main()