import os

path = "C:\\Users\\Kcat\\Desktop\\"

if os.path.exists(path):
    print("존재합니다.")
    if os.path.isfile(path):
        print("파일이 존재합니다.")
    elif os.path.isdir(path):
        print("폴더가 존재합니다.")
else:
    print("400 error")