import getpass  # 用于安全输入密码

def check_password():
    correct_password = "2056"  # 替换为您的正确密码
    print("-" * 30)
    print("温馨提示：输入密码后请按回车键确认")
    print("-" * 30)

    while True:
        entered_password = input("请输入密码: ")

        if entered_password == correct_password:
            return True
        else:
            if not entered_password:
                print("❌ 密码不能为空，请重新尝试")
            else:
                print("❌ 密码错误，很伤心呢 💔")

    # 调用函数
    check_password()


def create_heart_markdown():
    """创建爱心Markdown文档"""
    heart_pattern = [
        "    ❤️      ❤️\n"
        "  ❤️  ❤️  ️❤️   ❤️\n"
        "❤️      ❤️      ❤️\n"
        "❤️              ❤️\n"
        " ❤️            ❤️\n"
        "   ❤️        ❤️\n"
        "     ❤️    ❤️\n"
        "        ❤️\n"
    ]

    markdown_content = "↓\n"
    for line in heart_pattern:
        markdown_content += f"{line}  \n"
    return markdown_content


def main():
    """主函数"""
    print("=" * 40)
    print("           嘛哩嘛哩，芝麻开门")
    print("=" * 40)

    # 验证密码
    if check_password():
        print("恭喜你答对了!")

        # 生成Markdown内容
        markdown = create_heart_markdown()
        print(markdown)

        # 保存到文件
        with open("heart.md", "w", encoding="utf-8") as f:
            f.write(markdown)

# 运行程序
if __name__ == "__main__":
    main()