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
job_keywords = Interface.get_keywords_gpt(job=job,bot=bot)
#Trim the resume based on new keywords
resume.job_keywords=job_keywords
resume.fuzz_trim_work().fuzz_trim_skills().fuzz_trim_projects().sort_resume()
#Rewrite resume summary
Interface.rewrite_summary_gpt(job,resume,bot)
#Save new resume
resume.save_resume()