from text_storage.prompts import keyword_extract
from modules.utilities import prompt_optimize
from text_storage.prompts import rewrite_summary,summarize
import string

class Interface:
    @staticmethod
    def get_keywords_gpt(job,bot):
        prompt= string.Template(keyword_extract)
        prompt_fill = prompt.safe_substitute(job_pos=job.job_pos,job_desc=job.job_desc,comp_desc=job.comp_desc,comp_name=job.comp_name)
        optimized_prompt = prompt_optimize(prompt_fill)
        success, response, message = bot.ask(optimized_prompt)
        keywords_list = response.split(', ')
        keywords = [x.lower() for x in keywords_list]
        if ('shell'.lower() or 'linux'.lower()) in keywords:
            keywords.append('Bash')
        if ('ETL'.lower() or 'pipeline'.lower()) in keywords:
            keywords.append('Airflow')
        if 'AWS'.lower() in keywords:
            keywords.append('IBM')
        if 'container'.lower() in keywords:
            keywords.append('Docker')
        if 'mongodb' in keywords:
            keywords.append('IBM Cloudant')
        if 'mysql' in keywords:
            keywords.append(['SQL','PostgreSQL','SQlite','database'])
        if success:
            print(keywords)
            with open(f'prompt_{job.comp_name}_keywords.txt', 'w') as f: #how do we make this unique?
                    f.write(str(keywords))
            return(keywords)
        else:
            raise RuntimeError(message)

    @staticmethod
    def rewrite_summary_gpt(job,resume,bot):
        prompt= string.Template(rewrite_summary)
        prompt_fill = prompt.safe_substitute(fuzz_work=resume.fuzz_work,fuzz_skills=resume.fuzz_skills,fuzz_projects=resume.fuzz_projects, job_pos=job.job_pos, job_desc=job.job_desc, comp_desc=job.comp_desc, comp_name=job.comp_name)
        optimized_prompt = prompt_optimize(prompt_fill)
        success, response, message = bot.ask(optimized_prompt)
        resume.resume_output['basics']['summary'] = response

    @staticmethod
    def summarize_descriptions(job,bot):
        prompt= string.Template(summarize)
        prompt_fill = prompt.safe_substitute(job_pos=job.job_pos, job_desc=job.job_desc, comp_desc=job.comp_desc, comp_name=job.comp_name)
        optimized_prompt = prompt_optimize(prompt_fill)
        success, response, message = bot.ask(optimized_prompt)
        return response
