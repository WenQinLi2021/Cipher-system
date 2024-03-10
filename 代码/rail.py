def rail_fence_encrypt(text, num_rails):
    if num_rails == 1:
        return text

    rails = [''] * num_rails
    rail = 0
    direction = 1

    for char in text:
        rails[rail] += char
        rail += direction

        if rail == num_rails - 1 or rail == 0:
            direction *= -1

    return ''.join(rails)


def rail_fence_decrypt(encrypted_text, num_rails):
    if num_rails == 1:
        return encrypted_text

    # 初始化栅栏
    rails = [''] * num_rails
    rail_lengths = [0] * num_rails

    # 计算每个栅栏的长度
    rail = 0
    direction = 1
    for char in encrypted_text:
        rail_lengths[rail] += 1
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction *= -1

    # 重构栅栏
    index = 0
    for i in range(num_rails):
        rails[i] = encrypted_text[index:index + rail_lengths[i]]
        index += rail_lengths[i]

    # 重建原文
    decrypted_text = ''
    rail = 0
    direction = 1
    for _ in encrypted_text:
        decrypted_text += rails[rail][0]
        rails[rail] = rails[rail][1:]

        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction *= -1

    return decrypted_text

def main():
    original_text = "HelloWorld"
    num_rails = 3
    encrypted_text = rail_fence_encrypt(original_text, num_rails)
    print("Encrypted:", encrypted_text)

    decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
    print("Decrypted:", decrypted_text)
if __name__ == "__main__":
    main()