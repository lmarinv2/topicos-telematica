from mrjob.job import MRJob

precio_dia_negro = 0
fecha = ""

class M2_3(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield date, float(price)

    def reducer(self, date, values):
        l = list(values)
        mayor = precio_dia_negro

        if precio_dia_negro < sum(l):
            precio_dia_negro = sum(l)
            fecha = date


if __name__ == '__main__':
    M2_3.run()