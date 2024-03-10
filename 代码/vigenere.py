def vigenere_cipher(text, key, mode='encrypt'):
    key_length = len(key)
    key_as_int = [ord(i.upper()) - ord('A') for i in key]  # 转换密钥为大写，并计算相对于'A'的位置
    result = ""

    for i, char in enumerate(text):
        if char.isalpha():
            key_index = key_as_int[i % key_length]
            new_char = char.upper() if char.isupper() else char.lower()
            alpha_start = ord('A') if char.isupper() else ord('a')

            if mode == 'encrypt':
                new_index = (ord(new_char) - alpha_start + key_index) % 26
            elif mode == 'decrypt':
                new_index = (ord(new_char) - alpha_start - key_index) % 26

            result += chr(new_index + alpha_start)
        else:
            result += char

    return result

def main():
    key = "KEY"
    original_text = "HELLOworld"
    encrypted_text = vigenere_cipher(original_text, key)
    decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')

    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
if __name__ == "__main__":
    main()