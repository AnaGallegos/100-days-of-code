class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f'Q{self.q_number}: {current_question.question} (True/False): ')
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You\'re right!')
            
        else:
            print(f'That\'s wrong!! \n The correct answer was {correct_answer}')
        print(f'Your current score is {self.score}/{self.q_number}')
        print('\n')