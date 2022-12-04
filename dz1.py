# Вычислить число pi c заданной точностью d

d = int(input('Число c заданной точностью: '))
pi = 0

for i in range(1, 1000000, 4):
        turnover = (4 / i) - (4 / (i + 2))
        pi += turnover
print(round(pi, d))