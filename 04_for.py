point_list = [75, 80, 91]
total = 0
for point in point_list:
    print(point)
    total += point
print(total)

point_number = len(point_list)

average = total / point_number

print('合計点は{}平均点{}'.format(total, average))

for number in range(1, 11):
    print(number)

colors = [
    'red',
    'blue',
    'green',
    ]

for i, color in enumerate(colors):
    print(i, color)