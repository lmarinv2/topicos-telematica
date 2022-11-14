from mrjob.job import MRJob


class M2_1(MRJob):

    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, (float(price),date)

    def reducer(self, company, values):
        l = list(values)
        min_value = min(l)
        max_value = max(l)
        yield company, (min_value, max_value)


if __name__ == '__main__':
    M2_1.run()