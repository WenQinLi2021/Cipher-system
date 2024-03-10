from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import chardet


def generate_keys(key_length):
    key = RSA.generate(key_length)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def get_block_size(key_length, for_encryption=True):
    # 将密钥长度从位转换为字节
    byte_length = key_length // 8
    # PKCS1_OAEP填充需要的空间
    padding_space = 42
    # 如果是加密操作，需要减去填充空间
    if for_encryption:
        return byte_length - padding_space
    # 对于解密操作，可以使用完整的字节长度
    return byte_length


def encrypt_block(public_key, block):
    rsa_key = RSA.import_key(public_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    return rsa_cipher.encrypt(block)


def decrypt_block(private_key, encrypted_block):
    rsa_key = RSA.import_key(private_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    return rsa_cipher.decrypt(encrypted_block)


def encrypt_file(public_key, file_path, encrypted_path, block_size):
    encrypted_data = b''

    with open(file_path, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            encrypted_data += encrypt_block(public_key, block)

    with open(encrypted_path, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(private_key, encrypted_path, decrypted_path, block_size):
    decrypted_data = b''

    with open(encrypted_path, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            decrypted_data += decrypt_block(private_key, block)

    with open(decrypted_path, 'wb') as file:
        file.write(decrypted_data)


key_length = 1024
private_key, public_key = generate_keys(key_length)
encrypt_block_size = get_block_size(key_length)
decrypt_block_size = get_block_size(key_length, for_encryption=False)
# 使用示例
private_key, public_key = generate_keys(key_length)
# 加密文件
"""encrypt_file(public_key, 'C:\\Users\\86180\\Desktop\密码算法\\file.png',
             'C:\\Users\\86180\\Desktop\\密码算法\\RSA_enfile.png', encrypt_block_size)

# 解密文件
decrypt_file(private_key, 'C:\\Users\\86180\\Desktop\\密码算法\\encrypt_file.png',
             'C:\\Users\\86180\\Desktop\\密码算法\\RSA_defile.png', decrypt_block_size)"""
