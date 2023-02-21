import csv
import openai

openai.api_key = "#" #You can't go anywhere without this. 

with open('test.csv', 'r', encoding='utf-8') as csv_file: #Now this is where the trainer file goes in. 
    csv_reader = csv.reader(csv_file)

    with open('results.csv', 'w', encoding='utf-8', newline='') as results_file: #What's a data without clean output right? This line fixes the weird stuffs inside the csv.
        csv_writer = csv.writer(results_file, delimiter='|')

        for row in csv_reader: #loops on the headers, impt.
            website_description = row[0] #Reads the first row, counts starts -> 1
            response = openai.Completion.create( #Now, check the docs. These can be replaced based on your goal. But in this case. This will call the api to create a a response in the form of string.
                engine="text-davinci-003", #You can also use davinci-002 or 1. 003 is beneficial and is much faster compared to the lesser versions.
                prompt=(f"Basically, you just need to put stuffs in here. {test_row}"),  #This is the goal, to give a response similar to chatgpt.
                max_tokens=50, #Play with these settings based on your budget.
                n = 1,
                stop=None,
                temperature=0.7,
                best_of = 1,
                frequency_penalty = 0,
                top_p = 1,
                presence_penalty = 0
            )
            csv_writer.writerow([response["choices"][0]["text"].replace("\n", " ")]) #This is where you save the stuffs the AI gives. 
            
#I changed the API to number sign for privacy.
#I played around with the penalty settings to see which will generate better results
