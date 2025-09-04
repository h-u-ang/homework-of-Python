import tkinter as tk
from tkinter import messagebox, scrolledtext
import getpass  # 虽然getpass在GUI中不太需要，但保留导入


def check_password():
    correct_password = "6"  # 正确密码

    # 获取用户输入的密码
    entered_password = password_entry.get()

    if entered_password == correct_password:
        messagebox.showinfo("成功", "恭喜你答对了!")
        show_heart()
        return True
    else:
        if not entered_password:
            messagebox.showerror("错误", "❌ 密码不能为空，请重新尝试")
        else:
            messagebox.showerror("错误", "❌ 密码错误，很伤心呢 💔")
        password_entry.delete(0, tk.END)  # 清空输入框
        return False


def show_heart():
    """显示爱心图案"""
    # 隐藏密码输入部分
    password_frame.pack_forget()

    # 创建并显示爱心图案
    heart_text = scrolledtext.ScrolledText(root, width=35, height=20, font=("Courier", 12))
    heart_text.pack(pady=20)

    heart_pattern = [
        "    ❤️      ❤️\n"
        "  ❤️❤️❤️  ❤️❤️❤️\n"
        "❤️❤️❤️❤️❤️❤️❤️❤️❤️\n"
        "❤️❤️❤️❤️❤️❤️❤️❤️❤️\n"
        " ❤️❤️❤️❤️❤️❤️❤️❤️\n"
        "   ❤️❤️❤️❤️❤️❤️\n"
        "    ❤️❤️❤️❤️❤️\n"
        "      ❤️❤️❤️\n"
        "       ❤️❤️\n"
    ]

    heart_content = "↓\n\n"
    for line in heart_pattern:
        heart_content += f"{line}\n"

    heart_text.insert(tk.END, heart_content)
    heart_text.config(state=tk.DISABLED)  # 设置为只读

    # 添加保存按钮
    save_button = tk.Button(root, text="保存到文件", command=lambda: save_to_file(heart_content))
    save_button.pack(pady=10)


def save_to_file(content):
    """保存爱心到文件"""
    with open("heart.md", "w", encoding="utf-8") as f:
        f.write(content)
    messagebox.showinfo("成功", "爱心已保存到 heart.md 文件")


def on_enter_pressed(event):
    """回车键事件处理"""
    check_password()


# 创建主窗口
root = tk.Tk()
root.title("嘛哩嘛哩，芝麻开门")
root.geometry("500x400")

# 创建标题
title_label = tk.Label(root, text="嘛哩嘛哩，芝麻开门", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# 创建提示
hint_label = tk.Label(root, text="温馨提示：输入密码后请按回车键确认", font=("Arial", 10))
hint_label.pack(pady=5)

# 创建分隔线
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=10)

# 创建密码输入框架
password_frame = tk.Frame(root)
password_frame.pack(pady=20)

# 密码标签和输入框
password_label = tk.Label(password_frame, text="请输入密码:")
password_label.grid(row=0, column=0, padx=5, pady=5)

password_entry = tk.Entry(password_frame, show="*", width=20)  # 用*显示密码
password_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry.focus()  # 设置焦点到密码输入框

# 绑定回车键事件
password_entry.bind("<Return>", on_enter_pressed)

# 提交按钮
submit_button = tk.Button(password_frame, text="提交", command=check_password)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# 运行主循环
root.mainloop()