import os
import math
from termcolor import colored

cLinesCount = 0
cFilesCount = 0

swiftLinesCount = 0 
swiftFilesCount = 0

allLinesCount = 0
allFilesCount = 0

cppLinesCount = 0
cppFilesCount = 0

objcHeadersLinesCount = 0
objcHeadersFilesCount = 0

objcMainLinesCount = 0
objcMainFilesCount = 0

allSupportedFilesCount = 0

for root, dirs, files in os.walk(".", topdown=False):
   for name in files :
     with open(os.path.join(root, name)) as f:
      readLinesCount = len(f.readlines())
      allLinesCount += readLinesCount
      allFilesCount += 1

      if ".swift" in name:
        swiftLinesCount += readLinesCount
        swiftFilesCount += 1
        allSupportedFilesCount += 1
      if ".c" in name:
        cLinesCount += readLinesCount
        cFilesCount += 1
        allSupportedFilesCount += 1
      if ".cpp" in name:
        cppLinesCount += readLinesCount
        cppFilesCount += 1
        allSupportedFilesCount += 1
      if ".h" in name:
        objcHeadersLinesCount += readLinesCount
        objcHeadersFilesCount += 1
        allSupportedFilesCount += 1
      if ".m" in name:
        allSupportedFilesCount += 1
        objcMainLinesCount += readLinesCount
        objcMainFilesCount += 1


print("\n")        
print("=============================")
print("Result of parsing the folder:")
print("=============================")
print("\n")
print(colored('All files', 'cyan') + ":")
print("".join(["- Lines of code: ", str(allLinesCount)]))
print("".join(["- Count of files: ", str(allFilesCount)]))
print("\n")
print(colored('Swift', 'red') + ":")
print("".join(["- Lines of code: ", str(swiftLinesCount)]))
print("".join(["- Count of files: ", str(swiftFilesCount)]))
print("\n")
print(colored('Headers', 'green') + ":")
print("".join(["- Lines of code: ", str(objcHeadersLinesCount)]))
print("".join(["- Count of files: ", str(objcHeadersFilesCount)]))
print("\n")
print(colored('Main', 'yellow') + ":")
print("".join(["- Lines of code: ", str(objcHeadersLinesCount)]))
print("".join(["- Count of files: ", str(objcHeadersFilesCount)]))
print("\n")
print(colored('C', 'blue') + ":")
print("".join(["- Lines of code: ", str(cLinesCount)]))
print("".join(["- Count of files: ", str(cFilesCount)]))
print("\n")
print(colored('C++', 'magenta') + ":")
print("".join(["- Lines of code: ", str(cppLinesCount)]))
print("".join(["- Count of files: ", str(cppFilesCount)]))
print("\n")

def printPercentage(prefix, count):
  percent = round((float(count) / float(allSupportedFilesCount) * 100), 2)
  if percent == 0:
    return ""
  else:
    return " ".join([prefix + ":", str(percent) + "%"])

listOfPercentage = [printPercentage('Swift', swiftFilesCount), printPercentage('C', cFilesCount), printPercentage('C++', cppFilesCount), printPercentage('Headers', objcHeadersFilesCount), printPercentage('Main', objcMainFilesCount)]
stringOfList = ", ".join([x for x in listOfPercentage if x])
if stringOfList == "":
  print(colored('There is no supported languages in this project.', 'red'))
else:
  print(colored('Languages Percentage:', 'yellow'))
  print(stringOfList)