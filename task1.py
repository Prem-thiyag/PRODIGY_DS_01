# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:59:50 2024

@author: PREM
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Christ Uni Acad/Trimester 2/Python Personal/ex_1_data.csv")

age = df['Age Group']
male = df['Males']
female = df['Females']

plt.figure(figsize=(10, 6))

plt.barh(age, male, label='Male', alpha=0.7)
plt.barh(age, female, label='Female', alpha=0.7, left=male)  

plt.xlabel('Count')
plt.ylabel('Age')
plt.title('Horizontal Bar Plot by Age and Gender')

plt.legend()

plt.show()

