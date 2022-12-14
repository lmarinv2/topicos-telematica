from mrjob.job import MRJob

lista = []
class M3_3(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, movie

    def reducer(self, date, values):
        l = list(values)
        lista.append((len(l), date))

        yield date, len(l)

if __name__ == '__main__':
    M3_3.run()
    menor = 100000000000000000
    fecha = ""
    for i in lista:
        if i[0] < menor:
            menor = i[0]
            fecha = i[1]

    print(fecha)