import time


class Person():
    name = ""
    surname = ""
    size = 0
    height = 0
    weight = 0

    def set(self, name, surname, size, height, weight):
        self.name = name
        self.surname = surname
        self.size = size
        self.height = height
        self.weight = weight


n = int(input("Сколько человека хочешь добавить: "))
i = 0
person = []
person.append(1)
person[0] = Person()
person[0].set("Erasyl", "Kabulbekov", "XL", 185, 75)

person.append(1)
person[1] = Person()
person[1].set("Azamat", "Seitzhanuly", "XXL", 192, 95)

person.append(1)
person[2] = Person()
person[2].set("Xamit", "Kotibaruly", "L", 182, 65)

person.append(1)
person[3] = Person()
person[3].set("Serega", "Abayev", "M", 165, 65)

person.append(1)
person[4] = Person()
person[4].set("Islam", "Nurbayev", "XL", 175, 65)

persons = []

while (i < 5):
    print(
        person[i].name + " " + person[i].surname + " " + str(person[i].size) + " " + str(person[i].height) + " " + str(
            person[i].weight))
    i += 1

i = 0
while (i < n):
    name = input("Имя: ")
    surname = input("Фамилия: ")
    size = int(input("Размер: "))
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    person.append(1)
    person[i + 5] = Person()
    person[i + 5].set(name, surname, size, height, weight)
    print(person[i + 5].name + " " + person[i + 5].surname + " " + str(person[i + 5].size) + " " + str(
        person[i + 5].height) + " " + str(person[i + 5].weight))
    i += 1
    print("\n")

print("\n")

print("Выберите вид сортировки")
print("Нажмите [1] для пузырьковой сортировки")
print("Нажмите [2] для сортировки вставками")
print("Нажмите [3] для сортировки выбора")
s = 5 + n
choice = int(input())
start_time = time.time()
if choice == 1:

    print("\n Сортировка класса по методу пузырьковой сортировки ")
    print(" Сортировка по росту   [1]")
    print(" Сортировка по весу    [2]")
    print(" Cортировка по имени   [3]")
    print(" Сортировка по фамилию [4]")
    choice1 = int(input(" Выбор :"))
    if (choice1 == 1):
        i = 0
        while (i < s):
            j = 0
            while (j < s - i - 1):
                if (person[j].height < person[j + 1].height):
                    temp = person[j]
                    person[j] = person[j + 1]
                    person[j + 1] = temp
                j += 1
            i += 1
    elif (choice1 == 2):
        i = 0
        while (i < s):
            j = 0
            while (j < s - i - 1):
                if (person[j].weight < person[j + 1].weight):
                    temp = person[j]
                    person[j] = person[j + 1]
                    person[j + 1] = temp
                j += 1
            i += 1
    elif (choice1 == 3):
        i = 0
        while (i < s):
            j = 0
            while (j < s - i - 1):
                if (person[j].name < person[j + 1].name):
                    temp = person[j]
                    person[j] = person[j + 1]
                    person[j + 1] = temp
                j += 1
            i += 1
    elif (choice1 == 4):
        i = 0
        while (i < s):
            j = 0
            while (j < s - i - 1):
                if (person[j].surname < person[j + 1].surname):
                    temp = person[j]
                    person[j] = person[j + 1]
                    person[j + 1] = temp
                j += 1
            i += 1
elif (choice == 2):
    print("\n Сортировка класса по методу сортировки вставками:  ")
    print(" Сортировка по росту   [1]")
    print(" Сортировка по весу    [2]")
    print(" Cортировка по имени   [3]")
    print(" Сортировка по фамилию [4]")
    choice1 = int(input(" Выбор :"))
    if (choice1 == 1):
        i = 0
        while (i < s - 1):
            key = i + 1
            temp = person[key]
            j = i + 1
            while (j > 0):
                if (temp.height > person[j - 1].height):
                    person[j] = person[j - 1]
                    key = j - 1
                j -= 1
            person[key] = temp
            i += 1
    elif (choice1 == 2):
        i = 0
        while (i < s - 1):
            key = i + 1
            temp = person[key]
            j = i + 1
            while (j > 0):
                if (temp.weight > person[j - 1].weight):
                    person[j] = person[j - 1]
                    key = j - 1
                j -= 1
            person[key] = temp
            i += 1
    elif (choice1 == 3):
        i = 0
        while (i < s - 1):
            key = i + 1
            temp = person[key]
            j = i + 1
            while (j > 0):
                if (temp.name > person[j - 1].name):
                    person[j] = person[j - 1]
                    key = j - 1
                j -= 1
            person[key] = temp
            i += 1
    elif (choice1 == 4):
        i = 0
        while (i < s - 1):
            key = i + 1
            temp = person[key]
            j = i + 1
            while (j > 0):
                if (temp.surname > person[j - 1].surname):
                    person[j] = person[j - 1]
                    key = j - 1
                j -= 1
            person[key] = temp
            i += 1
elif (choice == 3):
    print("\n Сортировка класса по методу сортировки выбора: ")
    print(" Сортировка по росту   [1]")
    print(" Сортировка по весу    [2]")
    print(" Cортировка по имени   [3]")
    print(" Сортировка по фамилию [4]")
    choice1 = int(input(" Выбор :"))
    if (choice1 == 1):
        startIndex = 0
        while (startIndex < s - 1):
            smallestIndex = startIndex
            currentIndex = startIndex + 1
            while (currentIndex < s):
                if (person[currentIndex].height < person[smallestIndex].height):
                    smallestIndex = currentIndex
                temp = person[startIndex]
                person[startIndex] = person[smallestIndex]
                person[smallestIndex] = temp
                currentIndex += 1
            startIndex += 1
    elif (choice1 == 2):
        startIndex = 0
        while (startIndex < s - 1):
            smallestIndex = startIndex
            currentIndex = startIndex + 1
            while (currentIndex < s):
                if (person[currentIndex].weight < person[smallestIndex].weight):
                    smallestIndex = currentIndex
                temp = person[startIndex]
                person[startIndex] = person[smallestIndex]
                person[smallestIndex] = temp
                currentIndex += 1
            startIndex += 1
    elif (choice1 == 3):
        startIndex = 0
        while (startIndex < s - 1):
            smallestIndex = startIndex
            currentIndex = startIndex + 1
            while (currentIndex < s):
                if (person[currentIndex].name < person[smallestIndex].name):
                    smallestIndex = currentIndex
                temp = person[startIndex]
                person[startIndex] = person[smallestIndex]
                person[smallestIndex] = temp
                currentIndex += 1
            startIndex += 1
    elif (choice1 == 4):
        startIndex = 0
        while (startIndex < s - 1):
            smallestIndex = startIndex
            currentIndex = startIndex + 1
            while (currentIndex < s):
                if (person[currentIndex].surname < person[smallestIndex].surname):
                    smallestIndex = currentIndex
                temp = person[startIndex]
                person[startIndex] = person[smallestIndex]
                person[smallestIndex] = temp
                currentIndex += 1
            startIndex += 1

print("\n")
i = 0
while (i < s):
    print(
        person[i].name + " " + person[i].surname + " " + str(person[i].size) + " " + str(person[i].height) + " " + str(
            person[i].weight))
    i += 1

print("\n Время на сортировку: " + str(time.time() - start_time))
press = input("press Enter to close")