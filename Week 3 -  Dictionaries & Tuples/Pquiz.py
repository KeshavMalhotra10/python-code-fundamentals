quiz = [
    {
        "question": "Which country has the highest life expectancy?",
        "options": ["Japan", "Switzerland", "Singapore", "Hong Kong"],
        "answer": "Hong Kong",
    },
    {
        "question": "What is the most common surname in the United States?",
        "options": ["Smith", "Johnson", "Williams", "Jones"],
        'answer': "Smith",
    },
    {
        "question": "Who was the Ancient Greek God of the Sun?",
        "options": ["Apollo", "Zeus", "Hades", "Hermes"],
        "answer": "Apollo",
    },
    {
        "question": "What is the capitial of France",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "What art form is described as 'decorative handwriting' or handwritten lettering?",
        "options": ["Calligraphy", "Typography", "Graffiti", "Cursive"],
        "answer": "Calligraphy",

    }
    
]

def quizGame():
    score = 0 
    for i in  quiz:
        print(i['question'])
        print() #blank space
        print(i['options'])
        print()
        userInput = input("Select the correct option: ").lower()
        if userInput == str(i['answer'].lower()):
            score+=1
            print("Correct! The answer is " + str(i["answer"]) + "!")
            print()
        else:
            print("Incorrect! The answer is " + str(i["answer"]) + "!")
            print()
    
    print('Your score is ' + str(score) + "/" + str(len(quiz)))



quizGame()
        
