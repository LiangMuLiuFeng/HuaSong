#  npstream

#  文件编译

import npstream
import os


#  Normal Program Stream
#  一般程序算法流

#  Main compile program

def com(file, name="pro", dirs="C:\\Users\\Administrator\\Desktop\\"):
    f = open(file, "r")
    fil = len(f.readlines()) - 1
    f.close()

    f = open(file, "r")
    for x in range(fil):
        npstream.sc(f.readline()[:-1])
    npstream.sc(f.readline())

    os.system(r"copy C:\text.bat " + dirs + name + ".bat")


if __name__ == "__main__":
    while True:
        pro = input("C:\\cmd.exe> ")

        p = pro.split(" ")

        if p[0] == "compile":
            if p[1] == "nps":
                if len(p) == 3:
                    com(p[2])
                elif len(p) == 4:
                    com(p[2], p[3])
                else:
                    com(p[2], p[3], p[4])
            else:
                print(None)
        else:
            print(None)
