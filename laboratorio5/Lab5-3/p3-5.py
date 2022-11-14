
from mrjob.job import MRJob

lista = []
class M3_5(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, int(rating)

    def reducer(self, date, values):
        l = list(values)
        avg = sum(l) / len(l)
        lista.append((avg, date))

        yield date, avg

if __name__ == '__main__':
    M3_5.run()
    peor = 100000000000000000
    fecha = ""
    for i in lista:
        if i[0] < peor:
            peor = i[0]
            fecha = i[1]

    print(fecha)