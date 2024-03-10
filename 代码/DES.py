from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import Base_64
#文字
class DESEncryptor:
    def __init__(self,key):
        # 生成8字节的随机密钥
        self.key = key

    def encrypt(self, plaintext):
        # 如果plaintext不是字节格式，那么将其编码为utf-8格式的字节
        if not isinstance(plaintext, bytes):
            plaintext = plaintext.encode('utf-8')

        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_text = pad(plaintext, DES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        # 对加密数据进行Base64编码
        return base64.b64encode(encrypted_text)

    def decrypt(self, encrypted_text, is_binary_data=False):
        # 初始化DES解密器，使用相同的密钥和ECB模式
        cipher = DES.new(self.key, DES.MODE_ECB)

        # 先对数据进行Base64解码，因为加密后的数据是以Base64编码的形式存储的
        decoded_encrypted_text = base64.b64decode(encrypted_text)

        # 使用DES解密器解密数据
        decrypted_padded_text = cipher.decrypt(decoded_encrypted_text)

        # 移除填充，因为加密数据在加密前被填充到适合DES加密块的大小
        decrypted_text = unpad(decrypted_padded_text, DES.block_size)

        # 如果处理的是二进制数据（如图片），则直接返回解密后的字节数据
        # 如果处理的是文本数据，尝试将其解码为UTF-8格式的字符串
        if is_binary_data:
            return decrypted_text
        else:
            return decrypted_text.decode('utf-8')

#图片
class DESFileEncryptor(DESEncryptor):
    def encrypt_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.encrypt(file_data)
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)  # 已经是Base64编码过的数据

    def decrypt_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.decrypt(encrypted_data, is_binary_data=True)
        with open(output_file_path, 'wb') as file:
            file.write(decrypted_data)

def generate_key():
    # 生成随机密钥
    random_key = get_random_bytes(8)
    return random_key
    # 创建一个文件加密器实例
def main():
    key=generate_key()
    file_encryptor = DESFileEncryptor(key)

    # 路径
    input_image_path = r'C:\Users\86180\Desktop\密码算法\file.png'
    output_encrypted_image_path = r'C:\Users\86180\Desktop\密码算法\DES_enfile.png'
    output_decrypted_image_path = r'C:\Users\86180\Desktop\密码算法\DES_defile.png'
    # 加密图片
    file_encryptor.encrypt_file(input_image_path, output_encrypted_image_path)
    # 解密图片
    file_encryptor.decrypt_file(output_encrypted_image_path, output_decrypted_image_path)

    #文字
    encryptor = DESEncryptor(key)
    text = "135052021091 李文钦 fjnu "
    print("原文：",text)
    encrypted = encryptor.encrypt(text)
    print("加密后：",encrypted)
    decrypted = encryptor.decrypt(encrypted)
    print("解密后：",decrypted)

    #读取文本
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    print("原文：",plaintext)
    encrypted = encryptor.encrypt(plaintext)
    print("加密后：",encrypted)
    decrypted = encryptor.decrypt(encrypted)
    print("解密后：",decrypted)
if __name__ == "__main__":
    main()