def KaiSa_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # 检查字符是否为字母
            # 计算移位后的字符
            shift_amount = ord(char) + shift
            if char.islower():
                if shift_amount > ord('z'):
                    shift_amount -= 26
                elif shift_amount < ord('a'):
                    shift_amount += 26
            elif char.isupper():
                if shift_amount > ord('Z'):
                    shift_amount -= 26
                elif shift_amount < ord('A'):
                    shift_amount += 26

            result += chr(shift_amount)
        else:
            # 对于非字母字符，保持原样
            result += char

    return result

def main():
    encrypted_text = KaiSa_cipher("Hello World!", 27)
    decrypted_text = KaiSa_cipher(encrypted_text, -27)

    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
if __name__ == "__main__":
    main()