### The Head Data Scientist at Training Data Ltd. has asked you to create a DataFrame called ds_jobs_clean that stores the data in customer_train.csv much more efficiently. Specifically, they have set the following requirements:

### Columns containing integers must be stored as 32-bit integers (int32).
### Columns containing floats must be stored as 16-bit floats (float16).
### Columns containing nominal categorical data must be stored as the category data type.
### Columns containing ordinal categorical data must be stored as ordered categories, with an order that reflects the natural order of the column.
### The columns of ds_jobs_clean must be in the same order as the original dataset.
### The DataFrame should be filtered to only contain students with 10 or more years of experience at companies with at least 1000 employees, as their recruiter base is suited to more experienced professionals at enterprise companies.
### The final line must be ds_jobs_clean.head(100) to return only the first 100 rows.

```
import pandas as pd
import numpy as np

ds_jobs = pd.read_csv('customer_train.csv')

intcolumns = ['student_id', 'training_hours', 'job_change']
floatcolumns = ['city_development_index']
nominalcolumns = ['city', 'gender', 'major_discipline',  'company_type']
ordinalcolumns = ['relevant_experience', 'enrolled_university', 'education_level', 'experience',  'company_size', 'last_new_job']

ds_jobs[intcolumns] = ds_jobs[intcolumns].astype('int32')
ds_jobs[floatcolumns] = ds_jobs[floatcolumns].astype('float16')
ds_jobs[nominalcolumns] = pd.Categorical(ds_jobs[nominalcolumns])

relevant_experience_categories = pd.CategoricalDtype(['No relevant experience', 'Has relevant experience'], ordered=True)
enrolled_university_categories = pd.CategoricalDtype(['no_enrollment', 'Part time course', 'Full time course'], ordered=True)
education_level_categories = pd.CategoricalDtype(['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'], ordered=True)
experience_categories = pd.CategoricalDtype(['<1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '>20'], ordered=True)
company_size_categories = pd.CategoricalDtype(['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'], ordered=True)
last_new_job_categories = pd.CategoricalDtype(['never', '1', '2', '3', '4', '>4'], ordered=True)

ds_jobs['relevant_experience'] = ds_jobs['relevant_experience'].astype(relevant_experience_categories)
ds_jobs['enrolled_university'] = ds_jobs['enrolled_university'].astype(enrolled_university_categories)
ds_jobs['education_level'] = ds_jobs['education_level'].astype(education_level_categories)
ds_jobs['experience'] = ds_jobs['experience'].astype(experience_categories)
ds_jobs['company_size'] = ds_jobs['company_size'].astype(company_size_categories)
ds_jobs['last_new_job'] = ds_jobs['last_new_job'].astype(last_new_job_categories)

ds_jobs_clean = ds_jobs[(ds_jobs['experience'] >= '10') & (ds_jobs['company_size'] >= '1000-4999')]

ds_jobs_clean.head(100)
```
