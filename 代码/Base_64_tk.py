import base64
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Define the Base64 encoding and decoding functions
def encode_to_base64(input_text):
    input_bytes = input_text.encode('utf-8')
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

def decode_from_base64(encoded_text):
    encoded_bytes = encoded_text.encode('utf-8')
    try:
        decoded_bytes = base64.b64decode(encoded_bytes)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except base64.binascii.Error as e:
        return f"An error occurred: {str(e)} - This may indicate the input is not properly Base64 encoded."

def create_base64_interface(app):
    def encode_message():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="编码中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        plaintext = txt_plaintext.get("1.0", tk.END).strip()
        encoded = encode_to_base64(plaintext)
        txt_ciphertext.delete('1.0', tk.END)
        txt_ciphertext.insert(tk.END, encoded)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"编码时间: {end_time - start_time:.3f}秒")

    def decode_message():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="解码中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        encoded_text = txt_ciphertext.get("1.0", tk.END).strip()
        decoded = decode_from_base64(encoded_text)
        txt_plaintext.delete('1.0', tk.END)
        txt_plaintext.insert(tk.END, decoded)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"解码时间: {end_time - start_time:.3f}秒")

    def load_plaintext_from_file():
        # 使用文件对话框让用户选择文件
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # 读取并显示文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                txt_plaintext.delete('1.0', tk.END)
                txt_plaintext.insert(tk.END, data)

    # Text encoding and decoding interface
    tk.Label(app, text="原文").grid(row=0, column=0, sticky='w')
    txt_plaintext = scrolledtext.ScrolledText(app, height=10, width=70)
    txt_plaintext.grid(row=1, column=0, columnspan=2)

    tk.Label(app, text="Base64编码文本").grid(row=2, column=0, sticky='w')
    txt_ciphertext = scrolledtext.ScrolledText(app, height=10, width=70)
    txt_ciphertext.grid(row=3, column=0, columnspan=2)

    btn_encode = tk.Button(app, text="编码文本", command=encode_message)
    btn_encode.grid(row=4, column=0, sticky='w')
    btn_decode = tk.Button(app, text="解码文本", command=decode_message)
    btn_decode.grid(row=4, column=1, sticky='w')

    # 添加加载明文文件的按钮
    btn_load_plaintext = tk.Button(app, text="加载文本文件", command=load_plaintext_from_file)
    btn_load_plaintext.grid(row=5, column=0, columnspan=2, sticky='w')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=5, column=1, columnspan=2, sticky='w')
    app.mainloop()

