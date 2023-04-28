import json
import dotenv
from fuzzywuzzy import fuzz
import copy
import os

dotenv.load_dotenv()

class Resume:
    def __init__(self,filename,job_keywords=None,debug=False,fuzz_work=int(os.getenv('fuzz_work_strength')),fuzz_skills=int(os.getenv('fuzz_skills_strength')),fuzz_projects=int(os.getenv('fuzz_projects_strength'))):
        self.filename = filename
        self.resume_load = json.loads(open(f'{self.filename}', "r").read())
        self.resume_output = copy.deepcopy(self.resume_load)
        self.job_keywords = job_keywords
        self.debug = debug
        self.fuzz_work_strength = fuzz_work
        self.fuzz_skills_strength = fuzz_skills
        self.fuzz_projects_strength = fuzz_projects
        self.fuzz_work = None
        self.fuzz_skills = None
        self.fuzz_projects = None

    #Functions to output only necessary highlights of resume to limit token usage
    def work_trim(self):
        work_trim = [{'position': item['position'], 'highlights': item['highlights']} for item in self.resume_load['work']]
        return work_trim

    def projects_trim(self):
        projects_trim = [{'name': item['name'], 'highlights': item['highlights']} for item in self.resume_load['projects']]
        return projects_trim

    def skills_trim(self):
        return self.resume_load['skills']

    #Functions to trim the existing resume based on exctracted keywords
    def fuzz_trim_work(self):
        #typing.assert_type(self.job_keywords, list[str])
        if self.debug:
            print('-----------work-------------')
        jobs_to_delete = []
        for job_number,job in enumerate(self.resume_load['work']):
            new_highlights = [highlight for highlight in job['highlights']
                              for skill in self.job_keywords
                              if fuzz.token_set_ratio(highlight.lower(), skill.lower()) >= self.fuzz_work_strength]
            if self.debug:
                print('Current new_highlights: ', new_highlights)
            if len(new_highlights) != 0:
                self.resume_output['work'][job_number]['highlights'] = list(set(new_highlights))
            else:
                jobs_to_delete.append(job_number)
        if self.debug:
            print('jobs to delete: ', jobs_to_delete)
        for number in sorted(jobs_to_delete, reverse=True):
            del self.resume_output['work'][number]
        self.fuzz_work = self.resume_output['work']
        return self

    def fuzz_trim_skills(self):
        #typing.assert_type(self.job_keywords, list[str])
        if self.debug:
            print('-----------skills-------------')
        skills_to_delete = []
        for skill_number, skill in enumerate(self.resume_load['skills']):
            if skill['name'] == 'Programming Languages': #We don't want to cut any languages
                continue
            new_highlights = [keyword for keyword in skill['keywords']
                            for skill_in_set in self.job_keywords
                            if fuzz.partial_ratio(keyword.lower(), skill_in_set.lower()) > self.fuzz_skills_strength]
            if self.debug:
                print('Current new_highlights: ', new_highlights)
            if len(new_highlights) != 0:
                self.resume_output['skills'][skill_number]['keywords'] = list(set(new_highlights))
            else:
                skills_to_delete.append(skill_number)
            if skill['name'] == 'Soft Skills' and len(self.resume_output['skills'][skill_number]['keywords']) > 4:
                    self.resume_output['skills'][skill_number]['keywords']=self.resume_output['skills'][skill_number]['keywords'][:4]
        if self.debug:
            print('skills to delete: ', skills_to_delete)
        for number in sorted(skills_to_delete, reverse=True):
            del self.resume_output['skills'][number]

        self.fuzz_skills = self.resume_output['skills']
        return self
    def fuzz_trim_projects(self):
        #typing.assert_type(self.job_keywords, list[str])
        if self.debug:
            print('-----------projects-------------')
        del_counter = 0
        for project_number, project in enumerate(self.resume_load['projects']):
            new_highlights = []
            rescopy_number = project_number - del_counter
            new_keywords=[keyword for keyword in project['keywords']
                          for skill in self.job_keywords
                          if fuzz.partial_ratio(keyword.lower(), skill.lower()) > self.fuzz_projects_strength]
            if len(new_keywords) != 0:
                self.resume_output['projects'][rescopy_number]['keywords'] = list(set(new_keywords))
            else:
                del self.resume_output['projects'][rescopy_number]
                del_counter += 1
                continue #Do not execute the remainder of the loop
            new_highlights = [highlight for highlight in project['highlights']
                              for skill in self.job_keywords
                              if fuzz.token_set_ratio(highlight.lower(), skill.lower()) > self.fuzz_projects_strength]
            if len(new_highlights) != 0:
                self.resume_output['projects'][rescopy_number]['highlights'] = list(set(new_highlights))
            else:
                del self.resume_output['projects'][rescopy_number]
                del_counter += 1
        self.fuzz_projects = self.resume_output['projects']
        return self
    def sort_resume(self):
        def sort_by_keywords(e):
            if e['name'] != ['Soft skills']:
                return len(e['keywords'])
            else:
                return len(e)

        def sort_by_highlights(e):
            return len(e['keywords'])

        self.resume_output['skills'].sort(reverse=True, key=sort_by_keywords)
        self.resume_output['projects'].sort(reverse=True, key=sort_by_highlights)
        return self
    def save_resume(self):
        trim_res = json.dumps(self.resume_output)
        with open('resume_output.json', 'w') as f:
            # Write the JSON string to the file
            f.write(trim_res)


