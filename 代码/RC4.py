class RC4:
    def __init__(self, key):
        self.state = list(range(256))  # 初始化状态向量
        self.x = self.y = 0  # 初始化x, y计数器
        self.key_schedule(key)

    def key_schedule(self, key):
        #初始化和准备密钥流生成器状态
        j = 0
        for i in range(256):
            j = (j + self.state[i] + key[i % len(key)]) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]

    def byte_generator(self):
        # 伪随机生成算法
        while True:
            self.x = (self.x + 1) % 256
            self.y = (self.y + self.state[self.x]) % 256
            self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
            yield self.state[(self.state[self.x] + self.state[self.y]) % 256]

    def encrypt(self, plaintext):
        output = []
        prga = self.byte_generator()
        for char in plaintext:
            keystream_byte = next(prga)
            output.append("%02X" % (char ^ keystream_byte))  # 异或输出
        return ''.join(output)

def rc4_encrypt(plaintext, key):
    rc4 = RC4(key)
    return rc4.encrypt(plaintext)

def main():
    input_key="secret"
    key = input_key.encode('utf-8')  # 将字符串密钥转换为字节
    input_plaintext="Hello, RC4!"
    plaintext = input_plaintext.encode('utf-8')  # 将字符串明文转换为字节


    encrypted_text = rc4_encrypt(plaintext, key)
    print(f"原文{input_plaintext}经过RC4加密后为: {encrypted_text}")
    with open('m.txt', 'rb') as f:
        data = f.read()
    plaintext2 = data.decode("utf-8")
    plaintext = plaintext2.encode('utf-8')  # 将字符串明文转换为字节
    key=input_key.encode('utf-8')
    encrypted_text = rc4_encrypt(plaintext, key)
    print(f"原文{plaintext2}经过RC4加密后为: {encrypted_text}")

if __name__ == "__main__":
    main()

