import re



def main():

    names = ["name","_name", "2_name", "__name__"]

    for name in names:
        ret = re.match("[a-zA-Z]+[\w]*", name)
        if ret:
            print("变量名 %s 有效" % name)
        else:
            print("变量名 %s 无效"% name)

if __name__ == "__main__":
    main()
