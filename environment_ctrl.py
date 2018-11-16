class A:
    def __enter__(self):
        print('进入with语句')
        return self  # 返回的对象由as绑定

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print("正常离开with语句")
        else:
            print("离开with语句出现异常")
            print("exc_type，异常类型:",exc_type)
            print("exc_value，错误对象:",exc_value )
            print("exc_tb，traceback对象（谁调用的）:",exc_tb )



with A() as a:
    print("这是with语句")
    int(input("请输入"))