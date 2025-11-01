from mrjob.job import MRJob
from mrjob.step import MRStep
class MRWordFrequency(MRJob):
  def steps(self):
    return [
      MRStep(mapper=self.mapper_get_words,
         reducer=self.reducer_count_words),
      MRStep(reducer=self.reducer_sort_counts)
    ]
  def mapper_get_words(self, _, line):
    for word in line.split():
      yield word.lower(), 1
  def reducer_count_words(self, word, counts):
    yield None, (sum(counts), word)
  def reducer_sort_counts(self, _, word_count_pairs):
    for count, word in sorted(word_count_pairs, reverse=True):
      yield word, count
if __name__ == '__main__':
  MRWordFrequency.run()
