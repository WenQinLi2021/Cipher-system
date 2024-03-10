# gui_vigenere.py
import time
import tkinter as tk
from tkinter import scrolledtext
from vigenere import vigenere_cipher

def create_vigenere_interface(app):
    def encrypt_text():
        input_text = entry_text.get("1.0", tk.END).strip()
        key = entry_key.get().strip()
        if not key.isalpha():
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", "密钥无效，请输入字母组成的密钥")
            return

        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        encrypted = vigenere_cipher(input_text, key)
        entry_result.delete("1.0", tk.END)
        entry_result.insert("1.0", encrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    def decrypt_text():
        input_text = entry_text.get("1.0", tk.END).strip()
        key = entry_key.get().strip()
        if not key.isalpha():
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", "密钥无效，请输入字母组成的密钥")
            return
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        decrypted = vigenere_cipher(input_text, key, mode='decrypt')
        entry_result.delete("1.0", tk.END)
        entry_result.insert("1.0", decrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    # 输入文本
    tk.Label(app, text="文本（字母组成）:").grid(row=0, column=0, sticky='w')
    entry_text = scrolledtext.ScrolledText(app, height=6, width=50)
    entry_text.grid(row=1, column=0, columnspan=2)

    # 密钥
    tk.Label(app, text="密钥（字母组成）:").grid(row=2, column=0, sticky='w')
    entry_key = tk.Entry(app)
    entry_key.grid(row=2, column=1, sticky='w')

    # 输出结果
    tk.Label(app, text="结果:").grid(row=4, column=0, sticky='w')
    entry_result = scrolledtext.ScrolledText(app, height=6, width=50)
    entry_result.grid(row=5, column=0, columnspan=2)

    # 按钮
    btn_encrypt = tk.Button(app, text="加密", command=encrypt_text)
    btn_encrypt.grid(row=3, column=0, sticky='w')

    btn_decrypt = tk.Button(app, text="解密", command=decrypt_text)
    btn_decrypt.grid(row=3, column=1, sticky='e')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=6, column=1, sticky='e')
    app.mainloop()

