def create_heart_markdown():
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

    markdown_content = "恭喜你答对了↓\n\n"
    for line in heart_pattern:
        markdown_content += f"`{line}`  \n"

    return markdown_content


# 生成Markdown内容
markdown = create_heart_markdown()
print(markdown)

# 保存到文件
with open("heartsss.md", "w", encoding="utf-8") as f:
    f.write(markdown)