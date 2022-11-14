from mrjob.job import MRJob


class M1_2(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, int(salary)

    def reducer(self, idemp, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield idemp, avg


if __name__ == '__main__':
    M1_2.run()