import hashlib
import time
import tkinter as tk
from tkinter import filedialog, scrolledtext

# 定义SHA3-256加密函数
def create_SHA_interface(app):
    def sha_encrypt(input_text):
        start_time = time.time()  # 记录开始时间
        status_label.config(text="加密中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        sha_obj = hashlib.sha3_256()
        sha_obj.update(input_text.encode('utf-8'))
        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"加密时间: {end_time - start_time:.3f}秒")
        return sha_obj.hexdigest()

    # 加密输入的文本并显示结果
    def encrypt_input():
        input_text = txt_input.get("1.0", tk.END).strip()
        encrypted_text = sha_encrypt(input_text)
        txt_result.delete("1.0", tk.END)
        txt_result.insert(tk.END, encrypted_text)

    # 从文件中读取文本，显示原文并加密显示结果
    def encrypt_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                # 显示原始文本
                txt_input.delete("1.0", tk.END)
                txt_input.insert(tk.END, data)
                # 加密并显示结果
                encrypted_text = sha_encrypt(data)
                txt_result.delete("1.0", tk.END)
                txt_result.insert(tk.END, encrypted_text)


    # 输入文本框
    tk.Label(app, text="输入文本或文件内容:").grid(row=0, column=0, sticky='w')
    txt_input = scrolledtext.ScrolledText(app, height=6, width=70)
    txt_input.grid(row=1, column=0, sticky='w',columnspan=3)

    # 结果显示框
    tk.Label(app, text="SHA3-256 加密结果:").grid(row=2, column=0, sticky='w')
    txt_result = scrolledtext.ScrolledText(app, height=6, width=70)
    txt_result.grid(row=3, column=0, sticky='w',columnspan=3)

    # 加密按钮
    btn_encrypt = tk.Button(app, text="加密文本", command=encrypt_input)
    btn_encrypt.grid(row=4, column=0, sticky='w')

    # 读取文件并加密按钮
    btn_encrypt_file = tk.Button(app, text="读取文件并加密", command=encrypt_file)
    btn_encrypt_file.grid(row=4, column=1, sticky='w')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=4, column=2, sticky='e')
    app.mainloop()
