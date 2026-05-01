from src.models.animal import Animal

class Combat:

    def __init__(self, adversaire1: Animal, adversaire2: Animal, score1: int, score2: int):
        self.adversaire1 = adversaire1
        self.adversaire2 = adversaire2
        self.score1 = score1
        self.score2 = score2

    def __str__(self):
        return f"{self.adversaire1} ({self.score1}) vs {self.adversaire2} ({self.score2})"

    def modifier_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2        

    def liste_adversaire(self): 
        return [self.adversaire1, self.adversaire2]
    
    def resultat_str(self):
        if self.score1 > self.score2:
            return f"{self.adversaire1} gagne"
        elif self.score2 > self.score1:
            return f"{self.adversaire2} gagne"
        else:
            return "Match nul"
