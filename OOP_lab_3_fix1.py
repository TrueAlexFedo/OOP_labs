class Array3d:
    def __init__(self, width, height, depth):
        # Инициализация размеров массива и самого массива данными
        self.width = width      #ширина
        self.height = height    #высота
        self.depth = depth      #глубина
        self.data = [0] * (width * height * depth) #заполняем массив нулями

    def __getitem__(self, index):
        # Перегрузка оператора [] для доступа к элементам массива
        i, j, k = index
        return self.data[i * self.height * self.depth + j * self.depth + k]

    def __setitem__(self, index, value):
        # Перегрузка оператора [] для установки значения элемента массива
        i, j, k = index
        self.data[i * self.height * self.depth + j * self.depth + k] = value



    def get_values_0(self, i):
        #получаем срез по первой оси
        return [self.data[i * self.height * self.depth + j * self.depth + k] for j in range(self.height) for k in range(self.depth)]

    def get_values_1(self, j):
        #получаем срез по второй оси
        return [self.data[i * self.height * self.depth + j * self.depth + k] for i in range(self.width) for k in range(self.depth)]

    def get_values_2(self, k):
        #получаем срез по третьей оси
        return [self.data[i * self.height * self.depth + j * self.depth + k] for i in range(self.width) for j in range(self.height)]


    #получаем срезы по плоскостям
    def get_values_01(self, i, j):
        return [self.data[i * self.height * self.depth + j * self.depth + k] for k in range(self.depth)]

    def get_values_02(self, i, k):
        return [self.data[i * self.height * self.depth + j * self.depth + k] for j in range(self.height)]

    def get_values_12(self, j, k):
        return [self.data[i * self.height * self.depth + j * self.depth + k] for i in range(self.width)]



    #устанавливаем значения в срезы по осям и плоскостям
    def set_values_0(self, i, values):
        for j in range(self.height):
            for k in range(self.depth):
                self.data[i * self.height * self.depth + j * self.depth + k] = values[j][k]

    def set_values_1(self, j, values):
        for i in range(self.width):
            for k in range(self.depth):
                self.data[i * self.height * self.depth + j * self.depth + k] = values[i][k]

    def set_values_2(self, k, values):
        for i in range(self.width):
            for j in range(self.height):
                self.data[i * self.height * self.depth + j * self.depth + k] = values[i][j]

    def set_values_01(self, i, j, values):
        for k in range(self.depth):
            self.data[i * self.height * self.depth + j * self.depth + k] = values[k]

    def set_values_02(self, i, k, values):
        for j in range(self.height):
            self.data[i * self.height * self.depth + j * self.depth + k] = values[j]

    def set_values_12(self, j, k, values):
        for i in range(self.width):
            self.data[i * self.height * self.depth + j * self.depth + k] = values[i]


    #функции для заполнения нулями/единицами/конкретными значениями
    def ones(self):
        self.data = [1] * (self.width * self.height * self.depth)

    def zeros(self):
        self.data = [0] * (self.width * self.height * self.depth)

    def fill(self, value):
        self.data = [value] * (self.width * self.height * self.depth)

    def array_print(self):
        for i in range(self.width):
            print(f"i = {i}")
            for j in range(self.height):
                for k in range(self.depth):
                    print(self.data[i * self.height * self.depth + j * self.depth + k], end=" ")
                print()
            print()


if __name__ == '__main__':
    arr = Array3d(2, 3, 4)

    arr.set_values_0(0, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    arr.set_values_0(1, [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])

    arr.array_print()

    slice = arr.get_values_0(1)

    for i in slice:
        print(i, end=" ")
    print()

