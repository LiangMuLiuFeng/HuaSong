#  npstream

#  单行代码编译

import re
import os

#  Normal Program Stream
#  一般程序算法流

pro = open(r"C:\text.bat", "w")
pro.close()
pro = open(r"C:\text.bat", "a")


#  Main program

def sc(file):

    c = ""

    files = open(r"C:\text.bat", "a")

    b2 = re.match("set undefinded ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c = "@echo off"
        files.write(c + "\n")
        return 0

    b2 = re.match("non ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c = "cls"
        files.write(c + "\n")
        return 0

    b2 = re.match("shut ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c = "shutdown -s -t 0"
        files.write(c + "\n")
        return 0

    b2 = re.match("mod ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        f = file.split(" ")
        c = "mode con: cols=" + f[1] + " lines=" + f[2]
        files.write(c + "\n")
        return 0

    b2 = re.match("reop ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c = "shutdown -r -t 0"
        files.write(c + "\n")
        return 0

    b2 = re.match("cal ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "set /a " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("cop ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "copy " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("^if.*{$", file)
    if str(type(b2)) != "<class 'NoneType'>":
        if "var " in file:
            f = file.split(" ")
            if "string " in file:
                c = f[0] + " " + "\"%" + f[3] + "%\"" + f[4] + f[5] + " " + "("
                files.write(c + "\n")
                return 0
            c = f[0] + " " + "%" + f[2] + "%" + f[3] + f[4] + " " + "("
            files.write(c + "\n")
        c = str(list(file).pop())
        files.write(c + "\n")
        return 0

    b2 = re.match("^if up ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c = (file.replace("{", "(")).replace("}", ")")
        files.write(c + "\n")
        return 0

    b2 = re.match("^} elseif .*{$", file)
    if str(type(b2)) != "<class 'NoneType'>":
        if "var " in file:
            f = file.split(" ")
            if "string " in file:
                c = ")" + " " + "else if " + "\"%" + f[4] + "%\"" + f[5] + f[6] + " " + "("
                files.write(c + "\n")
                return 0
            c = ")" + " " + "else if " + "%" + f[3] + "%" + f[4] + f[5] + " " + "("
            files.write(c + "\n")
        c = ")" + (file.strip("}")).strip("{") + "("
        files.write(c + "\n")
        return 0

    b2 = re.match("for ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        if "range" in file:
            c1 = file.replace("range", "")
            c = c1.replace("var ", "%%")
            files.write(c + "\n")
            return 0
        c = file.replace("var ", "%%")
        files.write(c + "\n")
        return 0

    b2 = re.match("} else {", file)
    if str(type(b2)) != "<class 'NoneType'>":
        files.write(") else (\n")
        return 0

    if str(list(file)[-1]) == "{":
        c = str(list(file).pop()) + "("
        files.write(c + "\n")

    if str(list(file)[0]) == "}":
        c = ")" + file[1:]
        files.write(c + "\n")

    b2 = re.match("dir ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "cd " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("del ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "del " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("ren ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "ren " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("mdr ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "md " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("ddr ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "rd " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("adr ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "dir " + file[4:]
        files.write(c + "\n")
        return 0

    b = re.match("out ", file)
    if str(type(b)) != "<class 'NoneType'>":
        if "var " in file:
            file = file.replace("var ", "%")
            file += "%"
        c += "echo " + file[4:]
        files.write(c + "\n")
        return 0

    b = re.match("not ", file)
    if str(type(b)) != "<class 'NoneType'>":
        c += "::" + file[4:]
        files.write(c + "\n")
        return 0

    b = re.match("! ", file)
    if str(type(b)) != "<class 'NoneType'>":
        c += "::" + file[2:]
        files.write(c + "\n")
        return 0

    b2 = re.match("set ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        if "var " in file:
            c = "set " + file[8:]
            files.write(c + "\n")
            return 0
        c = "set /p " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("lif ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "echo."
        files.write(c)
        return 0

    b2 = re.match("wai ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "ping -n " + str(int(file[4:]) + 1) + " 127.1 >nul"
        files.write(c + "\n")
        return 0

    b2 = re.match("pau ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "pause>null"
        files.write(c + "\n")
        return 0

    b2 = re.match("cap ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "title " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("pro ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("col ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "color " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("open ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "start " + file[5:]
        files.write(c + "\n")
        return 0

    b2 = re.match("fun ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += ":" + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("use ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        c += "goto " + file[4:]
        files.write(c + "\n")
        return 0

    b2 = re.match("run ", file)
    if str(type(b2)) != "<class 'NoneType'>":
        os.system(r"C:\text.bat")

    files.close()
