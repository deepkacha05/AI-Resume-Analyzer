import pandas as pd

skills_df = pd.read_csv("data/skills_database.csv")

skills = skills_df['skill'].tolist()

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))