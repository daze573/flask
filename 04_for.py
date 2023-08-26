point_list = [75, 80, 91]
total = 0
for point in point_list:
    print(point)
    total += point
print(total)

point_number = len(point_list)

average = total / point_number

print('合計点は{}平均点{}'.format(total, average))