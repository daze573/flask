year_str = input('あなたの生まれた年を西暦４桁で入力して下さい')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_list = (
    '子', 
    '丑', 
    '寅', 
    '卯', 
    '辰', 
    '巳', 
    '午', 
    '未', 
    '申', 
    '酉', 
    '戌', 
    '亥',
    )

eto_name = eto_list[number_of_eto]
print('あなたの干支は', eto_name, 'です')

name = '東城つかさ'
age = 17
print("あなたの名前は{}です。年齢は{}です。".format(name, age))