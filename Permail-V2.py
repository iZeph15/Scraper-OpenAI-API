import csv
import openai

openai.api_key = ""

with open('website_descriptions.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('results.csv', 'w', encoding='utf-8', newline='') as results_file:
        csv_writer = csv.writer(results_file, delimiter='|')

        for row in csv_reader:
            website_description = row[0]
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=(f"Basically, you just need to put stuffs in here. {website_description}"),
                max_tokens=50,
                n = 1,
                stop=None,
                temperature=0.7,
                best_of = 1,
                frequency_penalty = 0,
                top_p = 1,
                presence_penalty = 0
            )
            csv_writer.writerow([response["choices"][0]["text"].replace("\n", " ")])
            
#I changed the directory and API to number sign for privacy.
#I played around with the penalty settings to see which will generate better results
