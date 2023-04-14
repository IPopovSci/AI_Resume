keyword_extract = ''' From the job description below, extract relevant keywords (hard and soft skills) for applying to $job_pos position. \
Output only the relevant keywords in a comma separated list.
Job description: "$job_desc" '''

rewrite_summary = '''Your job is to re-write my old resume summary. To ensure clarity and conciseness, please limit each sentence to a maximum of 20 words and strictly enforce a limit of no more than 2 commas per sentence. I will provide additional prompt fine-tuning information below. Output only new summary, and nothing else.
Fine-tuning information:"
Old-summary:
"Write a nice summary/highlight for your resume. ChatGPT will try to emulate the style, so put some thought into it."
Resume:
"work experiences:"$fuzz_work";"
skills:"$fuzz_skills";
projects:"$fuzz_projects";"
Job Description:
"Job position:"$job_pos";
Job description:"$job_desc";
Company description:"$comp_desc";
Company name:"$comp_name";""
'''