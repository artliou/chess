#Fun fact: the ELO rating system used for chess is also used to rank Players in League of Legends (LoL)
#Rating_a is Rating for Arthur (example)
#Rating_b is Rating for Bob


class Player(object):
    def __init__(self, name, rating, p):
        self.name = name
        self.rating = rating
        p = 1 #player starts having playing one rated game

    def game(self, opponent, result, p):
        #p marks the number of previous games the player has played
        expected_score_a = expected_a(self.rating, opponent.rating)
        expected_score_a = expected_a(opponent.rating, self.rating)

        #this section is based on the game result and relevant rating changes
        if result == 'Draw':
            self.rating = rating_change(self.rating, expected_score_a, 0.5)
            opponent.rating = rating_change(opponent.rating, 1 - expected_score, 0.5)
            if self.rating < opponent.rating
                print('Not bad, good luck next time!')
            elif self.rating > opponent.rating
                print('You shouldve won!')

        elif result == opponent.name or 'Loss':
            self.rating = rating_change(self.rating, expected_score_a, 0)
            opponent.rating = rating_change(opponent.rating, 1 - expected_score, 1)
            print('You need to keep practicing')

        elif result == self.name or 'Win':
            self.rating = rating_change(self.rating, expected_score_a, 1)
            opponent.rating = rating_change(opponent.rating, 1 - expected_score, 0)
            print('Congrats! You have won!')
        p += 1 #The person's number of games increases by 1

        print(self.name + 'has played' + p + 'games')

        if p < 26: #if a player has playing 25 or fewer games, they are considered provisional
                    #this is a designation to say this player only has a few games and his/her actual rating may fluctuate by a large number
            print('You have a USCF Provisional Rating of ' + rating)
