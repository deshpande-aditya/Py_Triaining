#Programs for Questions.
from Question import Question

question_prompts = [
    "What color are cherries?\n (a)Red\n(b)Purple\n(c)Orange\n\n",
    "What color is sky?\n (a)Green/Yellow\n(b)Red\n(c)Blue\n\n",
    "Which fruit keeps doctors away?\n(a)Orange\n(b)Banana\n(c)Apple\n\n"
]

questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer =