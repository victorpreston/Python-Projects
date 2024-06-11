import os
class QuizCreation:
    def process(self, question, choices, answer, question_number=""):
        choices_dict = {'a':1, 'b':2, 'c':3, 'd':4}
        with open("sample.txt", "a") as f:
            f.write(f"\nQUESTION {question_number}:- "+question)
            f.write("\n")
            count = 65
            for i in range(len(choices)):
                f.write(f"({chr(count)}) "+choices[i])
                f.write("\n")
                count += 1
            f.write(f"Answer :- ({answer.upper()}) "+choices[choices_dict[answer]-1])
            f.write("\n")
    
    def open_file(self):
        os.startfile("sample.txt")

Quiz = QuizCreation()