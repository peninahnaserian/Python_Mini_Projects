# a dict that stores the qns and answers
# have a variable that tracks the score of the player
# loop through the dict using the key value pairs
# display each qsn to the user and allow them to answer
# tell them if right or wrong
# show final result when quiz is completed

quiz = {
    "question1":{
        "question":"what is the capital of France?",
        "answer":"Paris"
    },
    "question2":{
        "question":"what is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"what is the capital of Italy?",
        "answer": "Rome"
    },
    "question4":{
        "question":"what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5":{
        "question":"what is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6":{
        "question":"what is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7":{
        "question":"what is the capital of Austria?",
        "answer": "Vienna"
    }     
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print(f"Correct answer is {value['answer']}")
    
print(f"Your score is {score}/7.")
print(f"Your percentage is {int(score/7 *100)} %")
    

