import random
from Crypto.Util import number
import math
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成一个大的质数
def generate_large_prime(bit_length):
    prime = number.getPrime(bit_length)
    return prime


# 生成两个大质数，即p和q
def generate_large_primes(bit_length):
    p = generate_large_prime(bit_length)
    q = generate_large_prime(bit_length)
    while p == q:  # 防止 p 和 q 相同
        q = generate_large_prime(bit_length)
    return p, q


# 计算最大公约数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 计算模反元素
def mod_inverse(e, phi_n):
    x1, y1, x2, y2 = 1, 0, 0, 1
    a, b = e, phi_n

    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        temp_x, temp_y = x2, y2
        x2, y2 = x1 - q * x2, y1 - q * y2
        x1, y1 = temp_x, temp_y

    gcd, x, y = a, x1, y1
    if gcd != 1:
        return None
    else:
        return x % phi_n


# 生成公私钥对
def generate_key_pair(bit_length):
    p, q = generate_large_primes(bit_length)
    p_binary = bin(p)
    q_binary = bin(q)

    print("p in binary:", p_binary)
    print("q in binary:", q_binary)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # 选择 e 作为公共密钥
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)

    return (n, e), (n, d)


# 对明文进行分组加密
def encrypt(plaintext, public_key):
    n, e = public_key
    # 计算分组的大小。因为RSA加密时需要将明文分组，并且每个分组需要转换成小于n的整数，所以分组的大小是由n的长度决定的。
    block_size = len(str(public_key[0])) // 2
    plaintext_blocks = [plaintext[i:i + block_size] for i in range(0, len(plaintext), block_size)]
    ciphertext_blocks = []
    # 遍历每个明文分组，先将分组转换成整数，然后用公钥的e进行指数运算，模n，将得到的值添加到密文分组列表中。
    for block in plaintext_blocks:
        # encode默认utf-8，big为大端字节转换
        block_int = int.from_bytes(block.encode(), 'big')
        ciphertext_blocks.append(pow(block_int, e, n))

    return ciphertext_blocks


# 对密文进行解密
def decrypt(ciphertext_blocks, private_key):
    n, d = private_key
    block_size = len(str(private_key[0])) // 2
    plaintext_blocks = []

    for block in ciphertext_blocks:
        block_int = pow(block, d, n)
        block_str = block_int.to_bytes(block_size, 'big').decode('utf-8', 'ignore')
        plaintext_blocks.append(block_str)

    # 拼接所有解密后的文本块
    decrypted_text = ''.join(plaintext_blocks)
    # 去除字符串开头的空字符
    decrypted_text = decrypted_text.lstrip('\x00')
    return decrypted_text



def blocks_to_text(blocks):
    # 计算每分组能包含的最大字符数，因为每个分组在加密时是一个数值
    block_size = len(str(blocks[0]))
    # 初始化空字符串
    result = ""
    # 遍历所有分组，将每个分组中的数字转换为对应的字符，并添加到结果中
    for block in blocks:
        # 将分组中的数字转换为对应的ASCII字符
        block_str = str(block).zfill(block_size)
        block_text = ""
        for i in range(0, block_size, 2):
            char_code = int(block_str[i:i + 2])
            if chr(char_code).isprintable():
                block_text += chr(char_code)
        # 添加该分组中转换后的字符
        result += block_text
    # 返回可视化的字符串
    return result


# 测试代码
if __name__ == '__main__':
    # 生成密钥对
    key_length=512
    public_key, private_key = generate_key_pair(key_length)

    # 打印生成的密钥对
    print(f"Public Key:   {public_key}")
    print(f"Private Key:  {private_key}")

    # 加密文件中的文本
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext = data.decode("utf-8")
    start_time=time.time()

    ciphertext_blocks = encrypt(plaintext, public_key)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"加密运行时间: {elapsed_time:.3f} 秒")
    # 打印密文分组
    ciphertext_text = blocks_to_text(ciphertext_blocks)
    print(f"\nCiphertext Text: {ciphertext_text}")

    # 解密密文
    start_time = time.time()
    plaintext_recovered = decrypt(ciphertext_blocks, private_key)
    # 打印解密后的明文
    print(f"\nRecovered Plaintext: {plaintext_recovered}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"解密运行时间: {elapsed_time:.3f} 秒")


