# airflow_etl_stock_pipeline

An airflow pipeline for daily updates on selected stock market companies news and prices.

## Table of contents

* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Setup and usage](#setup-and-usage)
* [Features](#features)
* [Author](#Author)

### Introduction

The aim of this project is to enable one-click optimization and customization of your JSON resume for specific job applications.
### Technologies and libraries

* Python 3.9
* fuzzywuzzy
* ChatGPT API

### Setup and usage

***Setup***

Clone the project and install dependancies: \
'pip install -r requirements.txt'

***Usage***

To use this project, you need to have your resume in JSON format. For more information on how to create a JSON resume, please refer to https://jsonresume.org/.

To achieve the best results, I recommend creating a comprehensive resume that includes all relevant experiences and projects. Any non-applicable items will be removed automatically.

Fill in the job information in the text_storage/job_info.py file, and run main.py. This will create a new JSON resume in the project folder named resume_companyname_output.json.

By default, the program will query ChatGPT to identify keywords relevant to the job description. The existing resume will then be edited to include only the sections with a partial ratio greater than the one specified in the .env file for each section.

Additionally, the resume summary will be rewritten based on the job and company descriptions. The prompts needed for this process are already provided in the /text_storage/prompts.py file. You just need to include the company information and your old resume summary for ChatGPT to rewrite.

The average cost of generating a new resume is very low, as the prompts are optimized to minimize the number of tokens. Unless you're dealing with very large job descriptions, the average price should be less than $0.002 per resume.

IMPORTANT: It's your responsibility to ensure the new resume is consistent and of high quality. I highly recommend proofreading it at least once to ensure it makes sense for the job you're applying to.

***.env settings***
```
OPENAI_API_KEY: Your OpenAI API Key
fuzz_skills_strength: Word-match strength to include in skills section.
fuzz_projects_strength: Word-match strength to include in projects section.
fuzz_work_strength: Word-match strength to include in work section.
```

I recommend tweaking the strength setting to achieve the resume length that's appropriate for your use.
Too high (90-100) might result in not including certain sections, while too low might make 
your resume too long.

### Project Status
This project is operational, but incomplete.

Future steps to complete the project:

* Adding a cover letter generator
* Adding a non-api keyword extractor

### Author

Created by Ivan Popov

