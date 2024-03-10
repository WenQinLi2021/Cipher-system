import base64
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from Crypto.Random import get_random_bytes

import AES

def create_aes_interface(app):
    def encrypt_message():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        plaintext = txt_plaintext.get("1.0", tk.END).strip()
        encrypted = aes_encryptor.encrypt(plaintext)
        txt_ciphertext.delete('1.0', tk.END)
        txt_ciphertext.insert(tk.END, encrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    def decrypt_message():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="解密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        ciphertext = txt_ciphertext.get("1.0", tk.END).strip()
        decrypted = aes_encryptor.decrypt(ciphertext)
        txt_plaintext.delete('1.0', tk.END)
        txt_plaintext.insert(tk.END, decrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"解密时间: {end_time - start_time:.3f}秒")

    def encrypt_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            encrypted_path = filedialog.asksaveasfilename(defaultextension=".enc")
            if encrypted_path:
                aes_file_encryptor.encrypt_file(file_path, encrypted_path)
                messagebox.showinfo("加密", "文件加密成功")

    def decrypt_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            decrypted_path = filedialog.asksaveasfilename(defaultextension=".png")
            if decrypted_path:
                aes_file_encryptor.decrypt_file(file_path, decrypted_path)
                messagebox.showinfo("解密", "文件解密成功")

    def generate_key():
        global aes_encryptor, aes_file_encryptor
        # 生成随机密钥
        random_key = get_random_bytes(16)  # AES-128位密钥
        random_iv = get_random_bytes(16)  # AES的初始化向量同样是16字节
        # 显示密钥（以Base64格式方便复制粘贴）
        displayed_key = base64.b64encode(random_key).decode('utf-8')
        txt_key.delete('1.0', tk.END)
        txt_key.insert(tk.END, displayed_key)
        # 重新创建加密器实例
        aes_encryptor = AES.AESEncryptor(random_key,random_iv)
        aes_file_encryptor = AES.AESFileEncryptor(random_key,random_iv)

    def load_plaintext_from_file():
        # 使用文件对话框让用户选择文件
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # 读取并显示文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                txt_plaintext.delete('1.0', tk.END)
                txt_plaintext.insert(tk.END, data)




    # 密钥显示框
    tk.Label(app, text="密钥（Base64编码）").grid(row=0, column=0, sticky='w')
    txt_key = scrolledtext.ScrolledText(app, height=4, width=70)
    txt_key.grid(row=1, column=0,columnspan=2)
    # 初始化加密器实例（可以用任意初始密钥，因为会在生成新密钥时被替换）
    initial_key = get_random_bytes(16)
    initial_iv = get_random_bytes(16)  # AES的初始化向量同样是16字节
    aes_encryptor = AES.AESEncryptor(initial_key,initial_iv)
    aes_file_encryptor = AES.AESFileEncryptor(initial_key,initial_iv)
    # 显示密钥（以Base64格式方便复制粘贴）
    displayed_key = base64.b64encode(initial_key).decode('utf-8')
    txt_key.delete('1.0', tk.END)
    txt_key.insert(tk.END, displayed_key)



    # 文本加密界面
    tk.Label(app, text="明文").grid(row=2, column=0, columnspan=2, sticky='w')
    txt_plaintext = scrolledtext.ScrolledText(app, height=10, width=70)
    txt_plaintext.grid(row=3, column=0, columnspan=2)

    tk.Label(app, text="密文").grid(row=4, column=0, columnspan=2, sticky='w')
    txt_ciphertext = scrolledtext.ScrolledText(app, height=10, width=70)
    txt_ciphertext.grid(row=5, column=0, columnspan=2)

    btn_encrypt = tk.Button(app, text="加密文本", command=encrypt_message)
    btn_encrypt.grid(row=6, column=2,  sticky='w')
    btn_decrypt = tk.Button(app, text="解密文本", command=decrypt_message)
    btn_decrypt.grid(row=6, column=3,  sticky='w')

    # 文件加密界面
    btn_encrypt_file = tk.Button(app, text="加密图片文件", command=encrypt_file)
    btn_encrypt_file.grid(row=7, column=0, sticky='w')
    btn_decrypt_file = tk.Button(app, text="解密图片文件", command=decrypt_file)
    btn_decrypt_file.grid(row=7, column=1,sticky='w')



    # 生成密钥按钮
    btn_generate_key = tk.Button(app, text="生成随机密钥", command=generate_key)
    btn_generate_key.grid(row=6, column=0, sticky='w')

    # 添加加载明文文件的按钮
    btn_load_plaintext = tk.Button(app, text="加载文本文件", command=load_plaintext_from_file)
    btn_load_plaintext.grid(row=6, column=1, columnspan=2, sticky='w')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=7, column=2, columnspan=2, sticky='w')
    app.mainloop()
