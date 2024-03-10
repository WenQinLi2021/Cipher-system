import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import RSA
import time
ciphertext_blocks=None
import Encrypt_File
def create_rsa_interface(app):
    def generate_keys():
        # 获取用户输入的密钥长度，如果没有输入则使用默认值512
        key_length = key_length_entry.get()
        if not key_length.isdigit():
            key_length = 512
        else:
            key_length = int(key_length)

        public_key, private_key = RSA.generate_key_pair(key_length)
        txt_public_key.delete('1.0', tk.END)
        txt_public_key.insert(tk.END, str(public_key))
        txt_private_key.delete('1.0', tk.END)
        txt_private_key.insert(tk.END, str(private_key))

    def encrypt_message():
        global ciphertext_blocks
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        # 加密过程
        plaintext = txt_plaintext.get("1.0", tk.END).strip()
        public_key = eval(txt_public_key.get("1.0", tk.END).strip())
        ciphertext_blocks = RSA.encrypt(plaintext, public_key)
        ciphertext_text = RSA.blocks_to_text(ciphertext_blocks)
        txt_ciphertext.delete('1.0', tk.END)
        txt_ciphertext.insert(tk.END, ciphertext_text)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    def decrypt_message():
        global ciphertext_blocks
        start_time = time.time()  # 记录开始时间
        status_label.config(text="解密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        # 解密过程
        private_key = eval(txt_private_key.get("1.0", tk.END).strip())
        plaintext = RSA.decrypt(ciphertext_blocks, private_key)
        txt_plaintext.delete('1.0', tk.END)
        txt_plaintext.insert(tk.END, plaintext)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"解密时间: {end_time - start_time:.3f}秒")


    def load_file():
        # 使用文件对话框让用户选择文件
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # 读取并显示文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                txt_plaintext.delete('1.0', tk.END)
                txt_plaintext.insert(tk.END, data)

    # 文件加密
    def encrypt_file_gui():
        file_path = filedialog.askopenfilename()  # 让用户选择文件
        if file_path:
            encrypted_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                          filetypes=[("PNG files", "*.png")])  # 让用户选择保存加密文件的位置
            if encrypted_path:
                try:
                    Encrypt_File.encrypt_file(Encrypt_File.public_key, file_path, encrypted_path, Encrypt_File.encrypt_block_size)
                    tk.messagebox.showinfo("成功", "文件加密成功！")
                except Exception as e:
                    tk.messagebox.showerror("错误", str(e))

    # 文件解密
    def decrypt_file_gui():
        file_path = filedialog.askopenfilename()  # 让用户选择加密文件
        if file_path:
            decrypted_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                          filetypes=[("PNG files", "*.png")])  # 让用户选择保存解密文件的位置
            if decrypted_path:
                try:
                    Encrypt_File.decrypt_file(Encrypt_File.private_key, file_path, decrypted_path, Encrypt_File.decrypt_block_size)
                    tk.messagebox.showinfo("成功", "文件解密成功！")
                except Exception as e:
                    tk.messagebox.showerror("错误", str(e))


    # 公钥文本框
    tk.Label(app, text="公钥").grid(row=0, column=0, columnspan=2, sticky='w')
    txt_public_key = scrolledtext.ScrolledText(app, height=6, width=70)
    txt_public_key.grid(row=1, column=0, columnspan=2)

    # 私钥文本框
    tk.Label(app, text="私钥").grid(row=2, column=0, columnspan=2, sticky='w')
    txt_private_key = scrolledtext.ScrolledText(app, height=6, width=70)
    txt_private_key.grid(row=3, column=0, columnspan=2)

    # 明文文本框
    tk.Label(app, text="明文").grid(row=4, column=0, columnspan=2, sticky='w')
    txt_plaintext = scrolledtext.ScrolledText(app, height=8, width=70)
    txt_plaintext.grid(row=5, column=0, columnspan=2)

    # 密文文本框
    tk.Label(app, text="密文").grid(row=6, column=0, columnspan=2, sticky='w')
    txt_ciphertext = scrolledtext.ScrolledText(app, height=8, width=70)
    txt_ciphertext.grid(row=7, column=0, columnspan=2)

    # 自定义密钥长度
    tk.Label(app, text="密钥长度（位）").grid(row=8, column=0, sticky='w')
    key_length_var = tk.StringVar(value="512")  # 设置默认值为512
    key_length_entry = tk.Entry(app, textvariable=key_length_var)
    key_length_entry.grid(row=8, column=1, sticky='w')

    # 按钮
    btn_generate_keys = tk.Button(app, text="随机生成公私钥", command=generate_keys)
    btn_generate_keys.grid(row=9, column=0, sticky='w')

    btn_encrypt = tk.Button(app, text="加密文本", command=encrypt_message)
    btn_encrypt.grid(row=9, column=2, sticky='w')

    btn_decrypt = tk.Button(app, text="解密文本", command=decrypt_message)
    btn_decrypt.grid(row=9, column=3, sticky='w')

    # 添加一个按钮来加载文件
    btn_load_file = tk.Button(app, text="加载文本文件", command=load_file)
    btn_load_file.grid(row=9, column=1, sticky='w')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=10, column=2, columnspan=4, sticky='w')

    #文件加密解密
    btn_encrypt_file = tk.Button(app, text="加密图片文件", command=encrypt_file_gui)
    btn_encrypt_file.grid(row=10, column=0, columnspan=4, sticky='w')

    btn_decrypt_file = tk.Button(app, text="解密图片文件", command=decrypt_file_gui)
    btn_decrypt_file.grid(row=10, column=1, columnspan=4, sticky='w')

    app.mainloop()
