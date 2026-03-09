from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_sort_by_count)
        ]

    def mapper_get_ratings(self, _, line):
        # Input: userID, movieID, rating, timestamp (tab-separated)
        try:
            userID, movieID, rating, timestamp = line.strip().split('\t')
            yield rating, 1
        except ValueError:
            pass  # skip malformed lines

    def reducer_count_ratings(self, rating, counts):
        # Count how many times each rating appears
        yield None, (sum(counts), rating)

    def reducer_sort_by_count(self, _, count_rating_pairs):
        # Sort by count (descending)
        sorted_pairs = sorted(count_rating_pairs, reverse=True)
        for count, rating in sorted_pairs:
            yield rating, count

if __name__ == '__main__':
    RatingsBreakdown.run()
