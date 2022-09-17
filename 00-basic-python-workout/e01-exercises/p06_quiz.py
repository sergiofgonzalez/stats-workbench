quiz = {
    "Q1": { "question": "What is the capital of Austria?", "answer": "Vienna" },
    "Q2": { "question": "What is the capital of Belgium?", "answer": "Brussels" },
    "Q3": { "question": "What is the capital of Bulgaria?", "answer": "Sofia" },
    "Q4": { "question": "What is the capital of Croatia?", "answer": "Zagreb" },
    "Q5": { "question": "What is the capital of Cyprus?", "answer": "Nicosia" },
    "Q6": { "question": "What is the capital of Czechia?", "answer": "Prague" },
    "Q7": { "question": "What is the capital of Denmark?", "answer": "Copenhagen" },
    "Q8": { "question": "What is the capital of Estonia?", "answer": "Tallinn" },
    "Q9": { "question": "What is the capital of Finland?", "answer": "Helsinki" },
    "Q10": { "question": "What is the capital of France?", "answer": "Paris" },
    "Q11": { "question": "What is the capital of Germany?", "answer": "Berlin" },
    "Q12": { "question": "What is the capital of Greece?", "answer": "Athens" },
    "Q13": { "question": "What is the capital of Hungary?", "answer": "Budapest" },
    "Q14": { "question": "What is the capital of Ireland?", "answer": "Dublin" },
    "Q15": { "question": "What is the capital of Italy?", "answer": "Rome" },
    "Q16": { "question": "What is the capital of Latvia?", "answer": "Riga" },
    "Q17": { "question": "What is the capital of Lithuania?", "answer": "Vilnius" },
    "Q18": { "question": "What is the capital of Luxembourg?", "answer": "Luxembourg" },
    "Q19": { "question": "What is the capital of Malta?", "answer": "Valletta" },
    "Q20": { "question": "What is the capital of Netherlands?", "answer": "Amsterdam" },
    "Q21": { "question": "What is the capital of Poland?", "answer": "Warsaw" },
    "Q22": { "question": "What is the capital of Portugal?", "answer": "Lisbon" },
    "Q23": { "question": "What is the capital of Romania?", "answer": "Bucharest" },
    "Q24": { "question": "What is the capital of Slovakia?", "answer": "Bratislava" },
    "Q25": { "question": "What is the capital of Slovenia?", "answer": "Ljubljana" },
    "Q26": { "question": "What is the capital of Spain?", "answer": "Madrid" },
    "Q27": { "question": "What is the capital of Sweden?", "answer": "Stockholm" }
}

print(len(quiz))

score = 0

for key, value in quiz.items():
    user_answer = input(value["question"] + " ")
    if user_answer.lower() == value["answer"].lower():
        print(">> correct!")
        score += 1
    else:
        print(f">> wrong: the correct answer was {value['answer']}")

print(f"Your score was: {score} ({round((score / len(quiz)) * 100)}%)")
