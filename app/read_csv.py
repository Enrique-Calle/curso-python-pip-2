import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)#Devuelve una tupla
      country_dict = {key: value for key, value in iterable}#Lo transformamos en un iterable
      data.append(country_dict)#Agregamos los diccionarios a la lista
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])