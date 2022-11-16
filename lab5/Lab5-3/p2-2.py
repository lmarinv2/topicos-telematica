from mrjob.job import MRJob


class M2_2(MRJob):

    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, float(price)

    def reducer(self, company, values):
        l = list(values)
        price1 = l[0]
        stable = 1
        for i in l:
            if i < price1:
                stable = 0
            price1 = i
        if stable:
            yield "Stable company", company


if __name__ == '__main__':
    M2_2.run()