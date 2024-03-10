from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# 文字
class AESEncryptor:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt(self, plaintext):
        # 确保plaintext是bytes类型
        if not isinstance(plaintext, bytes):
            plaintext = plaintext.encode('utf-8')

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_text = pad(plaintext, AES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted_text)

    def decrypt(self, encrypted_text, is_binary_data=False):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decoded_encrypted_text = base64.b64decode(encrypted_text)
        decrypted_padded_text = cipher.decrypt(decoded_encrypted_text)
        decrypted_text = unpad(decrypted_padded_text, AES.block_size)
        if is_binary_data:
            return decrypted_text
        else:
            return decrypted_text.decode('utf-8')

# 图片
class AESFileEncryptor(AESEncryptor):
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

def generate_key_iv():
    # 生成随机密钥和IV
    random_key = get_random_bytes(16)  # AES-128位密钥
    random_iv = get_random_bytes(16)   # AES的初始化向量同样是16字节
    return random_key, random_iv

def main():
    key, iv = generate_key_iv()
    file_encryptor = AESFileEncryptor(key, iv)
    # 路径
    input_image_path = r'C:\Users\86180\Desktop\密码算法\file.png'
    output_encrypted_image_path = r'C:\Users\86180\Desktop\密码算法\AES_enfile.png'
    output_decrypted_image_path = r'C:\Users\86180\Desktop\密码算法\AES_defile.png'
    # 加密图片
    file_encryptor.encrypt_file(input_image_path, output_encrypted_image_path)
    # 解密图片
    file_encryptor.decrypt_file(output_encrypted_image_path, output_decrypted_image_path)

    # 文字
    encryptor = AESEncryptor(key,iv)
    text = "135052021091 李文钦 fjnu "
    print("原文：", text)
    encrypted = encryptor.encrypt(text)
    print("加密后：", encrypted)
    decrypted = encryptor.decrypt(encrypted)
    print("解密后：", decrypted)

    # 读取文本
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    print("原文：", plaintext)
    encrypted = encryptor.encrypt(plaintext)
    print("加密后：", encrypted)
    decrypted = encryptor.decrypt(encrypted)
    print("解密后：", decrypted)


if __name__ == "__main__":
    main()