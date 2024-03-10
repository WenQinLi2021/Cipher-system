import time
import tkinter as tk
from tkinter import scrolledtext

def create_ASCII_interface(app):
    def text_to_ascii():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="转换中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        input_text = entry_text.get("1.0", tk.END).strip()
        ascii_conversion = ' '.join(str(ord(char)) for char in input_text)
        entry_ascii.delete("1.0", tk.END)
        entry_ascii.insert("1.0", ascii_conversion)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"转换时间: {end_time - start_time:.3f}秒")

    def ascii_to_text():
        start_time = time.time()  # 记录开始时间
        status_label.config(text="转换中，请稍后……")
        app.update()  # 更新界面以显示新的标签文本

        ascii_string = entry_ascii.get("1.0", tk.END).strip()
        text_conversion = ''.join(chr(int(ascii)) for ascii in ascii_string.split())
        entry_text.delete("1.0", tk.END)
        entry_text.insert("1.0", text_conversion)

        end_time = time.time()  # 记录结束时间
        status_label.config(text=f"转换时间: {end_time - start_time:.3f}秒")


    #文本
    tk.Label(app, text="文本:").grid(row=0, column=0, sticky='w')
    entry_text =scrolledtext.ScrolledText(app,  height=2, width=60)
    entry_text.grid(row=1, column=0)
    #ASCII
    tk.Label(app, text="ASCII:").grid(row=3, column=0, sticky='w')
    entry_ascii = scrolledtext.ScrolledText(app,  height=2, width=60)
    entry_ascii.grid(row=4, column=0)
    #按钮
    btn_to_ascii = tk.Button(app, text="将文本转换为ASCII码", command=text_to_ascii)
    btn_to_ascii.grid(row=2, column=0,sticky='w')

    btn_to_text = tk.Button(app, text="将ASCII码转换为文本", command=ascii_to_text)
    btn_to_text.grid(row=2, column=0,sticky='e')

    # 提示加解密运行时间信息标签
    status_label = tk.Label(app, text="")
    status_label.grid(row=5, column=0, sticky='e')
    app.mainloop()



