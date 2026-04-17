import random, string
from datetime import datetime
def generate_name(length):
    """生成指定长度的随机名字，包含大小写字母、数字和下划线"""
    characters = string.ascii_letters + string.digits + "_"
    name = ''.join(random.choice(characters) for _ in range(length))
    return name
def main():
    try:
        quantity = int(input("请输入需要生成的名字数量："))
        if quantity <= 0:
            print("生成数量必须大于0！")
            return
    except ValueError:
        print("请输入有效的数字！")
        return
    results = []
    for _ in range(quantity):
        name_length = random.randint(3, 15)
        name = generate_name(name_length)
        result = f"fp spawn {name}"
        results.append(result)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"fp-{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for result in results:
            file.write(result + "\n")
    print(f"生成完成，结果已保存到文件 {filename}")
if __name__ == "__main__":
    main()