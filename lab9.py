def calc():
    sum_num = 0.0
    sum_sq = 0.0
    count = 0
    while True:
        number = yield
        count += 1
        sum_num += number
        sum_sq += number ** 2

        average = sum_num / count
        average_sq = sum_sq / count
        print(f"{count} чисел введено, среднее значение {average}, дисперсия {average_square - average ** 2}")


coprog = calc()
next(coprog)
for i in range(5):
    number = float(input())
    coprog.send(number)