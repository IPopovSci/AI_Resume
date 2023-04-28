from text_storage.job_info import job_pos,job_desc,comp_desc,comp_name
from modules.job import Job
from modules.resume import Resume
from chatgpt_wrapper import OpenAIAPI
from interface import Interface

#Load API and resume
bot = OpenAIAPI()
resume=Resume('resume.json')
#Get the job keywords
job= Job(job_pos,job_desc,comp_desc,comp_name)
#Get the relevant keywords from job description
#Add so that if keywords exist, we don't double tap gpt again
job_keywords = Interface.get_keywords_gpt(job=job,bot=bot)
#Trim the resume based on new keywords
resume.job_keywords=job_keywords
resume.fuzz_trim_work().fuzz_trim_skills().fuzz_trim_projects().sort_resume()
#Rewrite resume summary
Interface.rewrite_summary_gpt(job,resume,bot)
#Save new resume
resume.save_resume()

summarized_job_info = Interface.summarize_descriptions(job,bot)
trimmed_resume = str('work experience:' + f'{resume.fuzz_work}; \n' + ' skills:' + f'{resume.fuzz_skills}; \n' + ' projects:' + f'{resume.fuzz_projects};\n' + 'education:' + f'{resume.resume_output["education"]}\n')
with open(f'condensed_{job.comp_name}.txt', 'w') as f:  # how do we make this unique?
    f.write(f'My resume (JSON format): \n "{trimmed_resume}"; \n '+ f'Position title: \n "{job.job_pos}"; \n' + f'Company name: \n "{job.comp_name}"; \n ' + f'Job keywords: \n "{job_keywords}"; \n' + f'Company description: \n "{comp_desc}";' )