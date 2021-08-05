from enum import Enum

class Result(Enum):
    WIN = 1
    LOSS = 0


class PokerHand:
    _card_rnk: str = "23456789TJQKA"
    hand = list()

    def __init__(self, input_hand: str):
        self.hand = []  #empty hand
        for card in input_hand.split(" "):
            if len(card) == 2:
                self.hand.append(card)
        assert len(self.hand) == 5

    def _get_rank_val(self, rnk: str):
        return self._card_rnk.find(rnk)

    def compare_with(self, pk_hand: 'PokerHand'):
        assert isinstance(pk_hand, PokerHand)
        scor_list = [(idx, self._score_hand(val)) for idx, val in enumerate([self.hand, pk_hand.hand])]
        winner = sorted(scor_list, key=lambda x:x[1])[-1][0]
        return Result.WIN if winner == 0 else Result.LOSS


    def _score_hand(self, hand: list):
        rnk_counts = {self._get_rank_val(r): ''.join(hand).count(r) for r, _ in hand}.items()
        score, rnks = zip(*sorted((cnt, rnk) for rnk, cnt in rnk_counts)[::-1])
        # checking more specific combinations
        if len(score) == 5:
            if rnks[:2] == (12, 3):
                rnks = (3, 2, 1, 0, -1)
            mstraight = rnks[0] - rnks[4] == 4
            mflush = len({suit for _, suit in hand}) == 1
            # no pair, straight flush, or strainght flush found
            score = ([1, (3,1,1,1)], [(3,1,1,2), (5,)])[mflush][mstraight]
        return score, rnks
