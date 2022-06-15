from typing import List
import json
import collections

class QnA:
    questions: List[str] = []
    answers: List[bool] = []
    def setup(self):
        self.answers = []
        self.load_questions()
    
    def getAnswer(self, question: str = ""):
        result = input(question).strip().lower()
        return result

    def execute(self):
        self.setup()
        for q in self.questions:
            print(q, end='(answer yes or no): ')
            if self.getAnswer() == "yes":
                self.answers.append(True)
            else:
                self.answers.append(False)
        if not self.show_result():
            self.show_warning()
            return
        self.show_compliment()
        while self.getAnswer("Do you want to add another? :") == "yes":
            print("another question : ", end="")
            self.add_question(self.getAnswer())

    def add_question(self, question: str):
        self.questions.append(question)
        with open('./questions.json', 'r') as f:
            json_data = json.load(f)
            if not question in json_data["questions"]:
                json_data["questions"].append(question)

        with open('./questions.json', 'w', encoding='utf-8') as make_file:
            json.dump(json_data, make_file, indent="\t")
           
    def load_questions(self):
        with open('./questions.json', 'r') as f:
            json_data = json.load(f)
            questions = json_data["questions"]
            for q in questions:
                if not q in self.questions:
                    self.questions.append(q)
    
    def show_result(self):
        result: bool = True
        for i in range(len(self.questions)):
            if self.answers[i] == True:
                print(self.questions[i] + ' ' + '\033[42m' + '\033[6m' + 'PASS' + '\033[0m')
            else:
                result = False
                print(self.questions[i] + ' ' + '\033[41m' + 'NOT YET' + '\033[0m')
        count = collections.Counter(self.answers)
        print("passed_work/total_work : "
         + str(count[1]) + '/' + str(len(self.answers)))
        return result

    def show_compliment(self):
        print("You are Great!")

    def show_warning(self):
        print("You are no right to add a question, You'd Better practice!")