import pickle

shoplistfile = 'shoplist.dat'  # имя файла, в котором мы сохраним объект
shoplist = ['one', 'two', 'three']  # список покупок
# Запись в файл
with open(shoplistfile, 'wb') as f:  # открываем файл на запись
    pickle.dump(shoplist, f)  # помещаем объект в файл

# Считываем из файла
with open(shoplistfile, 'rb') as f:  # открываем файл на чтение
    storedlist = pickle.load(f)  # загружаем объект из файла

    print(storedlist)
