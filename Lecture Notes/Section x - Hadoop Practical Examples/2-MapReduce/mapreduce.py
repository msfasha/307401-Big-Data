from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCountCustomerIDs(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get_ids,
                reducer=self.reducer_count_ids
            )
        ]

    # Mapper function
    def mapper_get_ids(self, _, line):
        # Split the line into customer IDs (assuming IDs are space-separated in each line)
        for customer_id in line.split():
            yield customer_id, 1

    # Reducer function
    def reducer_count_ids(self, customer_id, counts):
        # Sum up the counts for each customer ID
        yield customer_id, sum(counts)

if __name__ == '__main__':
    MRCountCustomerIDs.run()
