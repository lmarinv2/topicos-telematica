from mrjob.job import MRJob

class M3_1(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        lista = [int(movie), float(rating)]
        yield user, lista

    def reducer(self, user, values):
        l = list(values)
        sum = 0
        for i in l:
            sum += i[1]

        avg = sum / len(l)
        yield user, (len(l), avg)

if __name__ == '__main__':
    M3_1.run()