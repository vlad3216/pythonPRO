import os
import csv
import json

print("Добро пожаловать в конвертер JSON-CSV")
print("Этот волшебный скрипт умеет преобразовывать файл формата JSON в формат CSV")
print("Какой файл вы хотите преобразовать?")
try:
   filename = input("Имя файла: ")
   extension = filename.split(".")[-1].lower()
   f = open(filename)
except FileNotFoundError as error:
    print('Файл не найден!!!')
    quit()

if extension == "json":
    with open(filename) as json_file:
           data = json.load(json_file)
           keys = []
    for i in range(0,len(data)):
      for j in data[i]:
         if j not in keys:
            keys.append(j)

converted = []
converted.append(keys)
for i in range(0,len(data)):
   row = []
   for j in range(0,len(keys)):
      if keys[j] in data[i]:
         row.append(data[i][keys[j]])
      else:
         row.append(None)
   converted.append(row)

converted_file_basename = os.path.basename(filename).split(".")[0]
converted_file_extension = ".json" if extension == "csv" else ".csv"
if (os.path.isfile(converted_file_basename + converted_file_extension)):
    counter = 1
    while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension):
        counter += 1
        converted_file_basename = converted_file_basename + " (" + str(counter) + ")"
try:
   if converted_file_extension == ".json":
      with open(converted_file_basename + converted_file_extension, 'w') as outfile:
         json.dump(converted, outfile)
   elif converted_file_extension == ".csv":
      with open(converted_file_basename + converted_file_extension, 'w') as outfile:
         writer = csv.writer(outfile)
         writer.writerows(converted)
except:
   print("Ошибка создания файла")
else:
   print("Файл создан!:",converted_file_basename + converted_file_extension)
