from mrjob.job import MRJob
from mrjob.job import MRStep


class M3_2(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer1),
            MRStep(reducer=self.reducer2)
        ]

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, 1

    def reducer1(self, date, values):
        total = sum(values)
        yield None, (total, date)

    def reducer2(self, date, values):
        max_value = max(values)
        yield "Date max movies", max_value[1]


if __name__ == '__main__':
    M3_2.run()