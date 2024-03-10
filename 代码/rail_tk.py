import time
import tkinter as tk
from tkinter import scrolledtext
from rail import rail_fence_encrypt, rail_fence_decrypt

def create_rail_fence_interface(app):
    def encrypt_text():
        input_text = entry_text.get("1.0", tk.END).strip()
        try:
            start_time = time.time()  # 记录开始时间
            status_label.config(text="加密中，请稍后……")
            app.update()  # 更新界面以显示新的标签文本
            num_rails = int(entry_key.get())
            encrypted = rail_fence_encrypt(input_text, num_rails)
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", encrypted)
            end_time = time.time()  # 记录结束时间
            status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")
        except ValueError:
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", "请输入数字")

    def decrypt_text():
        input_text = entry_text.get("1.0", tk.END).strip()
        try:
            start_time = time.time()  # 记录开始时间
            status_label.config(text="解密中，请稍后……")
            app.update()  # 更新界面以显示新的标签文本
            num_rails = int(entry_key.get())
            decrypted = rail_fence_decrypt(input_text, num_rails)
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", decrypted)
            end_time = time.time()  # 记录结束时间
            status_label.config(text=f"解密时间: {end_time - start_time:.3f}秒")
        except ValueError:
            entry_result.delete("1.0", tk.END)
            entry_result.insert("1.0", "请输入数字")

    # 输入文本
    tk.Label(app, text="文本:").grid(row=0, column=0, sticky='w')
    entry_text = scrolledtext.ScrolledText(app, height=6, width=50)
    entry_text.grid(row=1, column=0, columnspan=2)

    # 密钥（栅栏栏数）
    tk.Label(app, text="栅栏栏数:").grid(row=2, column=0, sticky='w')
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
    app.mainloop()


