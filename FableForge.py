import re
import openai

openai.api_key = 'your-api-key'

def ask_question(question):
    response = input(question + " ")
    return response

def generate_text_with_gpt3(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": prompt}
      ]
    )
    return response['choices'][0]['message']['content']

def generate_outline(prompt):
    return generate_text_with_gpt3(prompt)

def generate_narration(prompt):
    return generate_text_with_gpt3(prompt)

def get_input(question, example):
    while True:
        response = ask_question(question)
        print(f'You answered: {response}')
        user_satisfied = input('Is this correct? (yes/no) ')
        if user_satisfied.lower() == 'yes':
            return response

def is_roman_numeral(s):
    pattern = r'^[IVX]+'
    match = re.match(pattern, s.split()[0])
    return match is not None

def generate_and_confirm(prompt, generator):
    feedback_prompt = prompt
    while True:
        generated_text = generator(feedback_prompt)
        print(f"Generated Text:\n{generated_text}\n")
        user_feedback = input("If you want to revise this, please provide your feedback. Otherwise, type 'approve': ")
        
        if user_feedback.lower() == 'approve':
            return generated_text
        else:
            feedback_prompt += f"\nBased on the feedback, here's a revision: {user_feedback}."

print("Let's create your podcast script!")

subject = get_input("What's the subject of your podcast?", "e.g., technology trends")
style = get_input("What style should the podcast be?", "e.g., formal, conversational, humorous")
tone = get_input("What tone do you prefer?", "e.g., serious, light-hearted, sarcastic")

while True:
    length = get_input("How long should the podcast be in minutes?", "e.g., 30")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Please enter a valid number for the length of the podcast.")

outline_prompt = f"We're creating a podcast on {subject}. The style is {style} and the tone is {tone}. The podcast should be {length} minutes long. Please provide a detailed outline for the episode."
outline = generate_and_confirm(outline_prompt, generate_outline)

sections = outline.split('\n')

narrations = []
for i, section in enumerate(sections):
    if is_roman_numeral(section):
        continue

    print(f"\nProcessing section {i+1} of {len(sections)}: {section}")
    
    section_prompt = f"Based on the following outline: '{section}', generate a {style} and {tone} narration for this podcast section."
    section_narration = generate_and_confirm(section_prompt, generate_narration)
    
    narrations.append(section_narration)

with open('outline.txt', 'w') as file:
    for section in sections:
        file.write(f"{section}\n")

with open('narration.txt', 'w') as file:
    for i, narration in enumerate(narrations):
        file.write(f"Section {i+1}:\n{narration}\n\n")
