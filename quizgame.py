questions = ["what is the capital of kenya?",
             "what is 5 + 5?",
             "which language are we learning?",
             "how many days are there in a week?",
             "what keyword is used to create a condition in python?"]

answers = [["a)Nairobi", "b)Mombasa", "c)Kisumu", "d)Nakuru"],
           ["a)10", "b)15", "c)20", "d)25"],
           ["a)Java", "b)C++", "c)Python", "d)JavaScript"],
           ["a)5", "b)6", "c)7", "d)8"],
           ["a)for", "b)while", "c)if", "d)else"]]

correct_answers = ["a", "a", "c", "c", "c"]

score = 0
name = input("Enter your name: ")
print("\nwelcome to the quiz game, " + name + "!\n")

for i in range(len(questions)):
    print(questions[i])

    for options in answers[i]:
        print(options)
    answer = input("Enter your answer (a/b/c/d): ").lower()
    if answer == correct_answers[i]:
       print("Correct!")
       score = score + 1
    else:
        print("Incorrect! The correct answer is:", correct_answers[i])

print(name + ",your score is," + str(score) + "/ " + str(len(questions)))

if score == len(questions):
  print("exellent work! you got all the questions right!")
elif score == 3:
     print("good job!")
else:
   print("keep practicing!")
    






               