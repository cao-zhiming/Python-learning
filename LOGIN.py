msg = '''
输入“名称”来查看用户名，
输入“年龄”来查看年龄，
输入“性别”来查看性别。
输入“帮助”来查看所有指令。
输入“退出”退出程序。
'''
print("欢迎注册！")
username = input("请输入用户名：")
password = input("请输入密码：")
print("注册成功！请登录")
logged_times = 0
while logged_times < 4:
    shuruyonghuming = input("请输入用户名：")
    if shuruyonghuming == username:
        shurumima = input("请输入密码：")
        if shurumima == password:
            print("登录成功！")
            age = input("请输入年龄：")
            sex = input("请输入性别：")
            while True:
                want = input('请输入需要执行的指令：（输入“帮助”来查看所有指令）')
                if want == '名称':
                    print("您的用户名为", username)
                elif want == '年龄':
                    print("您的年龄为", age)
                elif want == '性别':
                    print("您的性别为", sex)
                elif want == '帮助':
                    print(msg)
                elif want == '退出':
                    quit()
        else:
            print("密码错误。请重试。")
            logged_times+=1
    else:
        print("用户名有误。")
        logged_times+=1
else:
    print("您已经连续三次用户名或密码输入错误。")
    quit()
