import hashlib


# 定义MD5加密函数
def md5_encrypt(input_text):
    # 创建md5对象
    md5_obj = hashlib.md5()

    # 如果输入不是字节类型，则将其转换为字节
    if not isinstance(input_text, bytes):
        input_text = input_text.encode('utf-8')

    # 更新md5对象
    md5_obj.update(input_text)

    # 返回十六进制MD5加密结果
    return md5_obj.hexdigest()

def main():
    # 测试MD5加密函数
    text_to_encrypt = "Hello, MD5!"
    encrypted_text = md5_encrypt(text_to_encrypt)
    print(f"原文：'{text_to_encrypt}' 进行MD5加密后为: {encrypted_text}")
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    encrypted_text = md5_encrypt(plaintext)
    print(f"原文：'{plaintext}' 进行MD5加密后为: {encrypted_text}")

if __name__ == "__main__":
    main()