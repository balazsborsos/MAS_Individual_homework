
# Init settings

BOARD_ROWS = 9
BOARD_COLS = 9
WIN_STATE = (8, 8)
LOSE_STATE = (6, 5)
START = (2, 0)
DETERMINISTIC = True


def giveReward(self):
        if self.state == WIN_STATE:
            return 50
        elif self.state == LOSE_STATE:
            return -50
        else:
            return -1