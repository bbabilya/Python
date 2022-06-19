def shuffle(self):
        pull = self.cards
        shuffled = []
        while len(pull) > 0:
            r = random.randint(0, len(pull)-1)
            card = pull.pop(r)
            shuffled.append(card)