import pandas as pd

# Sample data
data = {
    "Pclass": [1, 1, 2, 2, 3, 3],
    "Sex": ["male", "female", "male", "female", "male", "female"],
    "Embarked": ["S", "C", "S", "C", "S", "C"],
    "Age": [20, 25, 30, 35, 40, 45],
    "Survived": [1, 0, 1, 0, 1, 0]  # Example survival data (1 for survived, 0 for not survived)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Grouping by multiple columns
grouped = df.groupby(['Pclass', 'Sex', 'Embarked']).size().unstack(fill_value=0)
print(grouped)
