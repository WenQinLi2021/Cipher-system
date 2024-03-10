def text_to_ascii(text):

    return ' '.join(str(ord(char)) for char in text)

def ascii_to_text(ascii_string):

    return ''.join(chr(int(ascii)) for ascii in ascii_string.split())

def main():
    example_text = "123 liwenqin fjnu"
    ascii_conversion = text_to_ascii(example_text)


    converted_back_text = ascii_to_text(ascii_conversion)

    print(f"转换后：{ascii_conversion} 原文为：{converted_back_text}")

if __name__ == "__main__":
    main()