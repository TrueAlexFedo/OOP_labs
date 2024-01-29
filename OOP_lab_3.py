class Array3d:
    def __init__(self, width, height, depth, values):
        self.__width = width        #ширина
        self.__height = height      #высота
        self.__depth = depth        #глубина
        self.__values = values
        self.__length = width * height * depth  #общая длина нашего одномерного массива, хранящегося внутри класса
        self.__data = [values] * self.__length  #заполняем массив значениями int

    #функция переводит индекс трехмерного массива в индекс одномерного
    def __transform_index(self, x, y, z):
        return x + self.__width * (y + self.__height * z)

    #таким образом трехмерный массив в классе будет храниться как одномерный

    #магический метод для печати
    def __str__(self):
        result = ""
        for z in range(self.__depth):
            result += f"Глубина: {z}\n"
            for y in range(self.__height):
                for x in range(self.__width):
                    result += f"{self.__data[self.__transform_index(x, y, z)]} "
                result += "\n"
            result += "\n"
        return result

    def GetValues_1(self, z):       #получаем значение по первому приближению, двумерный массив
        result = ""
        for y in range(self.__height):
            result += "\n"
            for x in range(self.__width):
                result += f"{self.__data[self.__transform_index(x, y, z)]}"
        return result

    def GetValues_2(self, z, y):    #получаем значение по 2 приближению, одномерный массив
        result = ""
        for x in range(self.__width):
            result += f"{self.__data[self.__transform_index(x, y, z)]} "
        return result

    def GetValues_3(self, z, y, x): # получаем само значение
        result = f"{self.__data[self.__transform_index(x, y, z)]} "
        return result


    #запись данных
    def SetValues_1(self, z, array):    #в 1 приближении на элемент [0] ставим двумерный массив [[3,3,3],...]
        for y in range(self.__height):
            for x in range(self.__width):
                self.__data[self.__transform_index(x, y, z)] = array[y][x]

    def SetValues_2(self, z, y, array): # во 2 приближении на элемент [0][0] ставим одномерный массив
        for x in range(self.__width):
            self.__data[self.__transform_index(x, y, z)] = array[x]

    def SetValues_3(self, z, y, x, value): # на элемент [0][0][0] ставим значение value
        self.__data[self.__transform_index(x, y, z)] = value

    # таким образом трехмерный массив в классе будет храниться как одномерный

    #заполнение массива одинаковыми значениями values
    def npfill(self, values):
        self.__data = [values] * self.__length


if __name__ == '__main__':
    array = Array3d(3, 3, 3, 10)
    #array.npfill(0)

    array.SetValues_3(0, 0, 0, 1)
    array.SetValues_3(1, 1, 1, 8)

    print(array.GetValues_1(0))
    print('\n')
    print(array.GetValues_2(0, 0))
    print('\n')
    print(array.GetValues_3(0, 0, 0))

    print(array)