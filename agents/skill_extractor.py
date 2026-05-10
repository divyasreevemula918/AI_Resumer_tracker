skills_database = [
    "python",
    "machine learning",
    "deep learning",
    "langchain",
    "sql",
    "tensorflow",
    "pytorch",
    "data analysis",
    "java",
    "c++",
    "aws",
    "docker"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return found_skills