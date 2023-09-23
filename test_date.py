from faker import Faker
fake = Faker('ja-JP')
file_name = 'fake.txt'
output_file = open(file_name, 'w', encoding='utf-8')
for i in range(100):
  name = fake.name()
  datetime = fake.date_of_birth().strftime('%Y年%m月%d日')
  address = fake.address()
  text = fake.text()
  output = ('番号:{}\n名前:{}\n誕生日:{}\n住所:{}\n紹介文:\n{}\n').format(i, name, datetime, address, text)
  output_file.write(output)
output_file.close()