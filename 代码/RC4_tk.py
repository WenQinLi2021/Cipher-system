import os
import time
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import random
import  RC4

# GUI函数
def create_RC4_interface(app):
    def generate_key():
        try:
            # 获取用户输入的密钥长度
            key_length = key_length_entry.get()
            if not key_length.isdigit():
                key_length = 8#默认8字节
            else:
                key_length = int(key_length)

            if 1 <= key_length <= 256:
                key = os.urandom(key_length)  # 生成指定长度的密钥
                txt_key.delete('1.0', tk.END)
                txt_key.insert(tk.END, key.hex())
            else:
                messagebox.showerror("错误", "密钥长度必须在1到256字节之间")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的密钥长度")

    def encrypt_text():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        plaintext = txt_plaintext.get("1.0", tk.END).strip()
        key = txt_key.get("1.0", tk.END).strip()
        if plaintext and key:
            plaintext = plaintext.encode('utf-8')
            key=key.encode('utf-8')
            encrypted_text = RC4.rc4_encrypt(plaintext, key)
            txt_ciphertext.delete('1.0', tk.END)
            txt_ciphertext.insert(tk.END, encrypted_text)

            end_time = time.time()  # 记录结束时间
            status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                txt_plaintext.delete('1.0', tk.END)
                txt_plaintext.insert(tk.END, data)

    # 密钥显示框
    tk.Label(app, text="密钥（Hex）:").grid(row=0, column=0, sticky='w')
    txt_key = scrolledtext.ScrolledText(app, height=2, width=60)
    txt_key.grid(row=1, column=0, columnspan=2)

    # 明文输入框
    tk.Label(app, text="明文:").grid(row=2, column=0, sticky='w')
    txt_plaintext = scrolledtext.ScrolledText(app, height=8, width=60)
    txt_plaintext.grid(row=3, column=0, columnspan=2)

    # 加密按钮
    btn_encrypt = tk.Button(app, text="加密", command=encrypt_text)
    btn_encrypt.grid(row=7, column=1, sticky='w')

    # 随机密钥按钮
    btn_generate_key = tk.Button(app, text="生成随机密钥", command=generate_key)
    btn_generate_key.grid(row=6, column=2, columnspan=4,sticky='w')
    # 自定义密钥长度
    tk.Label(app, text="密钥长度（字节）").grid(row=6, column=0, sticky='w')
    key_length_var = tk.StringVar(value="16")  #
    key_length_entry = tk.Entry(app, textvariable=key_length_var)
    key_length_entry.grid(row=6, column=1, sticky='w')

    # 密文显示框
    tk.Label(app, text="密文（Hex）:").grid(row=4, column=0, sticky='w')
    txt_ciphertext = scrolledtext.ScrolledText(app, height=8, width=60)
    txt_ciphertext.grid(row=5, column=0, columnspan=2)

    # 读取文件按钮
    btn_load_file = tk.Button(app, text="加载文本文件", command=load_file)
    btn_load_file.grid(row=7, column=0, sticky='w')
    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=7, column=2, sticky='e')
    app.mainloop()
