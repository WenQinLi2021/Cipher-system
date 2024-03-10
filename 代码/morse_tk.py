import time
import tkinter as tk
from tkinter import scrolledtext
from morse import morse_encrypt, morse_decrypt

def create_morse_interface(app):
    def encrypt_text():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本
        input_text = entry_text.get("1.0", tk.END).strip()
        encrypted = morse_encrypt(input_text)
        entry_result.delete("1.0", tk.END)
        entry_result.insert("1.0", encrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")

    def decrypt_text():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="解密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本
        input_text = entry_text.get("1.0", tk.END).strip()
        decrypted = morse_decrypt(input_text)
        entry_result.delete("1.0", tk.END)
        entry_result.insert("1.0", decrypted)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"解密时间: {end_time - start_time:.3f}秒")

    # 输入文本
    tk.Label(app, text="文本:").grid(row=0, column=0, sticky='w')
    entry_text = scrolledtext.ScrolledText(app, height=6, width=50)
    entry_text.grid(row=1, column=0, columnspan=2)

    # 输出结果
    tk.Label(app, text="结果:").grid(row=3, column=0, sticky='w')
    entry_result = scrolledtext.ScrolledText(app, height=6, width=50)
    entry_result.grid(row=4, column=0, columnspan=2)

    # 按钮
    btn_encrypt = tk.Button(app, text="加密", command=encrypt_text)
    btn_encrypt.grid(row=2, column=0, sticky='w')

    btn_decrypt = tk.Button(app, text="解密", command=decrypt_text)
    btn_decrypt.grid(row=2, column=1, sticky='e')
    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=6, column=1, sticky='e')
    app.mainloop()


