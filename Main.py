import os

print("Started program")
filePath = "C:\\Users\\edgib102\\Documents\\blender\\saves\\cache_fluid_4b85f272"
NameList = ["config", "data", "noise"]
Startframe = 3

def Delete(Files):
    FileList = []
    for file in Files:
        FileList.append(file)
    for i in range(Startframe-1):
        os.remove(FileList[i])
        print("Deleted " + FileList[i].name)


def Rename(Files, name, strFiles):
    i = 1
    for file in Files:
        if name != "config":
            os.rename(file, strFiles + "\\" + "fluid_" +
                      name + '_' + str(i).zfill(4) + ".uni")
            i += 1
        else:
            os.rename(file, strFiles + "\\" + name +
                      '_' + str(i).zfill(4) + ".uni")
            i += 1


def CheckBase():
    entries = os.scandir(filePath)
    for entry in entries:
        for x in NameList:
            if x == entry.name:
                print(entry.name + " found")
                DataFilepath = filePath + "\\" + entry.name
                print("filepath gotten: " + DataFilepath)
                Delete(os.scandir(DataFilepath))
                Rename(os.scandir(DataFilepath), entry.name, DataFilepath)


CheckBase()
