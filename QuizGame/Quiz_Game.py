#Quiz Class
#Methods: add_players, ask_questions, show_winner
from typing import List

class Question:
    def __init__(self, prompt: str, answer: str):
        self.prompt = prompt
        self.answer = answer
        
class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

class Quiz:
    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.players = []
    #adds player to game
    def add_players(self, player: Player)-> None:
        self.players.append(player)

    def ask_questions(self) -> None:
        # Main logic for quiz
        for player in self.players:
            print(f"\n{player.name}'s turn")
            for question in self.questions:
                answer = input(question.prompt)
                if answer.lower() == question.answer.lower():
                    player.score += 1
            print(f"Player {player.name}, score: {player.score}")
 
    def show_winner(self):
        winner = max(self.players, key=lambda p: p.score)
        print(f"The winner is: {winner.name} with a score of {winner.score}")
questions = [
    Question("What is 2 + 2?", "4"),
    Question("What is the capital of Germany?", "Berlin"),
    Question("What is the capital of Italy?", "Rome")
]

alice = Player("Alice")
bob = Player("Bob")

quiz = Quiz(questions)
quiz.add_players(alice)
quiz.add_players(bob)

quiz.ask_questions()
quiz.show_winner()
