from helper import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        if gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX() + 1, self.Position.getY())) == 4:
            create_collect_action(Point(1, 0))
        elif gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX(), self.Position.getY() + 1)) == 4:
            create_collect_action(Point(0, 1))
        elif gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX() - 1, self.Position.getY())) == 4:
            create_collect_action(Point(-1, 0))
        elif gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX(), self.Position.getY() - 1)) == 4:
            create_collect_action(Point(0, -1))
        else:
            create_move_action(Point(0, 1))
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
