import os


def replace_name(path, originalName, replaceName):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:
        if os.path.isdir(path + '/' + file):
            print(file)
            replace_name(path + '/' + file, originalName, replaceName)
        else:
            print("before change")
            if originalName in file:
                new = str(path + '/' + file.replace(originalName, replaceName))
                old = str(path + '/' + str(file))
                try:
                    os.rename(old, new)
                    print("after change")
                except IOError:
                    continue


path = "../../detection"
originalName = '.png'
replaceName = '.jpg'

replace_name(path, originalName, replaceName)