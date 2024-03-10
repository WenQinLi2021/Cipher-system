import hashlib


# 定义SHA3-256加密函数
def sha3_encrypt(input_text):
    # 创建SHA3-256对象
    sha3_obj = hashlib.sha3_256()

    # 如果输入不是字节类型，则将其转换为字节
    if not isinstance(input_text, bytes):
        input_text = input_text.encode('utf-8')

    # 更新SHA3-256对象
    sha3_obj.update(input_text)

    # 返回十六进制SHA3-256加密结果
    return sha3_obj.hexdigest()

def main():
    # 测试SHA3-256加密函数
    text_to_encrypt = "Hello, SHA-3!"
    encrypted_text = sha3_encrypt(text_to_encrypt)
    print(f"原文： '{text_to_encrypt}' 进行SH3-256加密后为: {encrypted_text}")
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    encrypted_text = sha3_encrypt(plaintext)
    print(f"原文：'{plaintext}' 进行SH3-256加密后为: {encrypted_text}")

if __name__ == "__main__":
    main()