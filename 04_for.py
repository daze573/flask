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

your_point = input('点数をカンマ区切りで入力して下さい:')
point_input = your_point.split(',')
total = 0

for point in point_input:
  total += int(point)
print(total)

subject_number = len(point_input)

average_point = total / subject_number

excellent = subject_number * 100 * 0.8
good = subject_number * 100 * 0.65

if total >= excellent:
    evaluation = 'Excellent'
elif total >= good:
    evaluation = 'Good'
else:
    evaluation = 'Bad'
print('点数の評価は{}です。'.format(evaluation))