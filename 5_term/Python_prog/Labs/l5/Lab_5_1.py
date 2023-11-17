import helper as h


answer, data = h.chooseOpenFile()

if (answer == False):
    selectedMenu = h.selectBookTypeMenu()
    data = h.getDataByBookType(selectedMenu)

print(data)

h.chooseSaveDataToFile(data)