from helper import *
import point
import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

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

        # Analyse de la zone 5x5
        matrixInit = np.zeros([5,5])

        for i in range(5):
            for j in range(5):
                matrixInit[i][j] = gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX() + i, self.PlayerInfo.Position.getY() + j))
                if gameMap.getTileAt(self, Point(self.PlayerInfo.Position.getX() + i, self.PlayerInfo.Position.getY() + j)) == 4:
                    StorageHelper.write("positionCible", Point(self.PlayerInfo.Position.getX() + i, self.PlayerInfo.Position.getY() + j))

        # Check wether there is a positionCible
        if StorageHelper.read("positionCible") is None:
            return create_move_action(Point(0,-1))
        else:
            matrixPath = np.zeros([5,5])
            for i in range(5):
                for j in range(5):
                    if matrixInit[i][j] == 0 or matrixInit[i][j] == 4:
                        matrixPath[i][j] = 1
                    else:
                        matrixPath[i][j] = 0

            grid = Grid(matrix = matrixPath)
            start = grid.node(0,0)
            end = grid.node(StorageHelper.read("positionCible").getX(), StorageHelper.read("positionCible").getY())

            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)

            for y in range(len(self.nodes)):
                for x in range(len(self.nodes[y])):
                    node = self.nodes[y][x]
                    if path and ((node.x, node.y) in path or node in path):
                        return create_move_action(Point(node.x, node.y))


    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
