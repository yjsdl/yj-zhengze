import re



def main():

    name = input("请输入邮箱地址:")
    # 如果在正则表达式中需要用到某些普通的字符，比如. 比如？仅仅需要在他们前面添加一个\ 进行转义
    ret = re.match(r"[0-9a-zA-z_]{4,20}@163.com$", name)
    if ret:
        print("地址 %s 有效" % name)
    else:
        print("地址 %s 无效 "% name)

if __name__ == "__main__":
    main()
