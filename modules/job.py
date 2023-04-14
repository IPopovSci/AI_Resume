'''Data Object to store job information'''
class Job():
    def __init__(self,job_pos,job_desc,comp_desc,comp_name):
        self.job_pos=job_pos #position title
        self.job_desc=job_desc
        self.comp_desc=comp_desc
        self.comp_name=comp_name

    @staticmethod
    def remove_job_dups(job):
        # Split the relevant attributes into lists of words
        job_desc_words = job.job_desc.split()
        comp_desc_words = job.comp_desc.split()

        # Remove duplicate words from each list
        job_desc_words = list(set(job_desc_words))
        comp_desc_words = list(set(comp_desc_words))

        # Join the lists back into strings and update the attributes
        job.job_desc = ' '.join(job_desc_words)
        job.comp_desc = ' '.join(comp_desc_words)

        # Return the modified job instance
        return job
