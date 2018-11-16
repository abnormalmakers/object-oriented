# def read_file():
#     try:
#         f=open("./MRO.py",'rb')
#         try:
#             while True:
#                 data=f.readline()
#                 data=data[:-1]
#                 if not data:
#                     break
#                 print(data.decode())
#         finally:
#             f.close()
#     except OSError:
#         print('文件打开失败')
#
# read_file()


# 用with语句
def read_file():
    try:
        with open('./MRO.py','rb') as f:
            while True:
                data=f.readline()
                if not data:
                    break
                data=data[:-1]
                print(data.decode())
    except OSError:
        print('文件打开失败')

read_file()