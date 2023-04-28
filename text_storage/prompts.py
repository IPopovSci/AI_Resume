keyword_extract = ''' From the job description below, extract relevant keywords (hard and soft skills) for applying to $job_pos position. \
Make sure to capture ALL technologies that are relevant to $job_pos title.Output only the relevant keywords in a comma separated list.
Job description: "$job_desc" '''

rewrite_summary = '''Your job is to re-write my old resume summary. To ensure clarity and conciseness, please limit each sentence to a maximum of 20 words and strictly enforce a limit of no more than 2 commas per sentence, as well as stick to strict limit of 3 sentences. I will provide additional prompt fine-tuning information below. Output only new summary, and nothing else.
Fine-tuning information:"
Old-summary:
"As a freelance data scientist with expertise in machine learning techniques and database management, I have delivered strategic insights and competitive advantages to clients by identifying key features and insights and leveraging advanced data analysis techniques to guide model development and optimization. My technical skills in Python, SQL, and PostgreSQL, combined with my strong attention to detail, adaptability, and critical thinking, make me a valuable asset to any team. With a passion for innovation and a strategic approach to problem-solving, I am dedicated to leveraging my technical expertise to drive optimal outcomes and deliver value to clients through data engineering and science."
Resume (You are only allowed to mention skills/keywords that are present in this section in the new summary):
"work experiences:"$fuzz_work";"
skills:"$fuzz_skills";
projects:"$fuzz_projects";"
Job Description (You are not allowed to mention keywords present here, if they are not present in the resume section):
"Job position:"$job_pos";
Job description:"$job_desc";
Company description:"$comp_desc";
Company name:"$comp_name";""
'''

summarize = '''Please summarize the following job description focusing on the information relevant to applying to a $job_pos position at the company:
Job description: "$job_desc";'''