import tkinter as tk
from DES_tk import create_des_interface
from RSA_tk import create_rsa_interface
from AES_tk import create_aes_interface
from Base_64_tk import create_base64_interface
from MD5_tk import  create_MD5_interface
from SHA_256_tk import create_SHA_interface
from RC4_tk import  create_RC4_interface
from ASCII_tk import create_ASCII_interface
from KaiSa_tk import create_KaiSa_interface
from vigenere_tk import  create_vigenere_interface
from rail_tk import  create_rail_fence_interface
from morse_tk import create_morse_interface

def switch_interface(choice):
    # 清除旧界面
    for widget in interface_frame.winfo_children():
        widget.destroy()

    # 根据选择加载新界面
    if choice == "DES":
        create_des_interface(interface_frame)
    elif choice == "RSA":
        create_rsa_interface(interface_frame)
    elif choice == "AES":
        create_aes_interface(interface_frame)
    elif choice == "Base64":
        create_base64_interface(interface_frame)
    elif choice == "MD5":
        create_MD5_interface(interface_frame)
    elif choice == "SHA3-256":
        create_SHA_interface(interface_frame)
    elif choice == "RC4":
        create_RC4_interface(interface_frame)
    elif choice == "ASCII":
        create_ASCII_interface(interface_frame)
    elif choice == "凯撒加密":
        create_KaiSa_interface(interface_frame)
    elif choice == "维基利亚密码":
        create_vigenere_interface(interface_frame)
    elif choice == "栅栏密码":
        create_rail_fence_interface(interface_frame)
    elif choice == "摩斯密码":
        create_morse_interface(interface_frame)

app = tk.Tk()
app.title("可视化多密码算法集成系统")
# 创建一个包含标签和下拉菜单的框架
top_frame = tk.Frame(app)
top_frame.pack(side=tk.TOP, fill=tk.X, anchor='nw')

# 在这个框架内创建一个标签
algorithm_label = tk.Label(top_frame, text="密码类型（十二月支持十二种）：")
algorithm_label.pack(side=tk.LEFT)
# 创建下拉菜单
algorithm_choice = tk.StringVar(top_frame)
algorithm_choice.set("RSA")  # 默认设置为DES
drop_down_menu = tk.OptionMenu(top_frame, algorithm_choice, "RSA", "DES","AES", "Base64","MD5","SHA3-256","RC4","ASCII","凯撒加密","维基利亚密码","栅栏密码","摩斯密码",command=switch_interface)
drop_down_menu.pack(side=tk.LEFT)


# 创建界面容器
interface_frame = tk.Frame(app)
interface_frame.pack()

# 默认加载RSA界面
create_rsa_interface(interface_frame)

app.mainloop()
