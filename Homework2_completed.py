#!/usr/bin/env python
# coding: utf-8

# # Homework 2

# # Part 1: Working with numpy, calculating final grades

# In[ ]:


import numpy as np

num_students = 10
num_assessments = 5
assessment_names = ["Homework", "Project", "Exam1", "Exam2", "Final Exam"]

names = []
grades_matrix = np.zeros((num_students, num_assessments))

print(f"Please enter the names and grades for {num_students} students: ")

for g in range(num_students):
    name = input(f"\nEnter name for student {g+1}: ")
    names.append(name)

    for h in range(num_assessments):
        score = float(input(f"Enter score for {assessment_names[h]}: "))
        grades_matrix[g, h] = score

weights = np.array([0.15, 0.15, 0.20, 0.20, 0.30])

final_scores = np.dot(grades_matrix, weights)

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

letter_grades = [get_letter_grade(i) for i in final_scores]

print("\n" + "="*30)
print(f"{'Student Name':<15} | {'Score':<6} | {'Grade'}")
print("-" * 30)
for j in range(num_students):
    print(f"{names[j]:<15} | {final_scores[j]:<6.2f} | {letter_grades[j]}")


# # Part 2: Working with Pandas, Titanic dataset

# In[2]:


import pandas as pd


# ## Storing dataset into a dataframe

# In[4]:


df = pd.read_csv("C:/Users/hwang/OneDrive/Documents/MC stuff/Spring 2026/DATA 101 Introduction to Data Science/Classwork/Datasets/titanic.csv")


# ## Getting general information about the data

# In[5]:


df.info()


# In[7]:


df.describe()


# In[9]:


df.iloc[1:4]
a = [10,20,30,40,50,60,70,80,90,100]
df2 = df.loc[a,['Name','Age']]
df2.head()
df2.shape


# In[11]:


naf_info = df.loc[100:105, ['Name', 'Age', 'Fare']]
print(naf_info)


# # Creating two dataframes, one for categorical variables and one for quantitative variable

# In[16]:


df_categorical = df.select_dtypes(include=['object'])
df_quantitative = df.select_dtypes(include=['number'])


# # Save dataframes to .csv files

# In[22]:


df_categorical.to_csv('C:/Users/hwang/OneDrive/Documents/MC stuff/Spring 2026/DATA 101 Introduction to Data Science/Homework/Saved Dataframes/titanic_categorical.csv', index=False)
df_quantitative.to_csv('C:/Users/hwang/OneDrive/Documents/MC stuff/Spring 2026/DATA 101 Introduction to Data Science/Homework/Saved Dataframes/titanic_quantitative.csv', index=False)

