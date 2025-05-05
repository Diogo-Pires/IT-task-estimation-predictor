import pandas as pd
import random

# Possible values
levels = ["Junior", "Mid", "Senior"]
tech_stacks = [
    ["HTML", "CSS", "JavaScript"],
    [".NET", "SQL"],
    ["Python", "Flask", "PostgreSQL"],
    ["Node.js", "MongoDB"],
    ["React", "Redux", "TypeScript"],
    ["Java", "Spring", "MySQL"]
]

task_templates = [
    "Build a user login and registration page",
    "Create a REST API for task management",
    "Design a database schema for a blog",
    "Fix layout issues on mobile view",
    "Implement caching for improved performance",
    "Optimize SQL queries for analytics"
]

# Function to simulate time taken
def simulate_finished_time(experience, tech_count):
    base_time = random.uniform(4, 12)
    experience_factor = max(0.5, 1.5 - (experience / 10))
    tech_factor = 1 + (tech_count - 2) * 0.15
    noise = random.uniform(0.9, 1.1)
    return round(base_time * experience_factor * tech_factor * noise, 2)

# Generate data
num_samples = 100
data = []
for i in range(1, num_samples + 1):
    experience = random.randint(0, 15)
    level = random.choices(levels, weights=[0.3, 0.4, 0.3])[0]
    task = random.choice(task_templates)
    tech_stack = random.choice(tech_stacks)
    time_taken = simulate_finished_time(experience, len(tech_stack))

    data.append({
        "id": i,
        "years_experience": experience,
        "level": level,
        "task_description": task,
        "tech_stack": ", ".join(tech_stack),
        "finished_at_hours": time_taken
    })

# Create DataFrame and export
df = pd.DataFrame(data)
df.to_csv("synthetic_programming_tasks.csv", index=False)
print("CSV file 'synthetic_programming_tasks.csv' created.")