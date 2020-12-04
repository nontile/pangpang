# __init__
# show_question
# check_answer
# word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)


class Word:
    def __init__(self, question, answer1, answer2, answer_no):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer_no = answer_no

    def show_question(self):
        print(f"\"{self.question}\"의 뜻은?")
        print(f"{self.answer1}")
        print(f"{self.answer2}")

    def check_answer(self, answer_no):
        if self.answer_no == answer_no:
            print("정답입니다.")
        else:
            print("틀렸습니다.")


word = Word("킹콩", "킹이 콩을 먹다", "킹콩이다", 2)
word.show_question()
word.check_answer(int(input("=> ")))