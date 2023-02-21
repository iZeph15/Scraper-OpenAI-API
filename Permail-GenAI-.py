import openai
import csv

openai.api_key = ""

with open('input.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

greetings = []

for row in data:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"I love {row['company_description']}. | I'm humbled by {row['company_description']}. "),
        max_tokens=30,
        n=5,
        temperature=0.5,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=2,
    )

    best_response = response.choices[0].text
    greetings.append(best_response)

with open('final.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['personalized_response']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for greeting in greetings:
        writer.writerow({'personalized_response': greeting})

#I changed the directory and API to number sign for privacy.
#I played around with the penalty settings to see which will generate better results