from helper import *
import point
import numpy as np


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
            def plusProche(self, arrayDirection):
                closestPoint = Point(-1, -1)
                closestDistance = 1000
                for i in arrayDirection:
                    if Point.Distance(self.PlayerInfo.Position, arrayDirection[i]) < closestDistance:
                        closestDistance = Point.Distance(self.PlayerInfo.Position, arrayDirection[i])
                        closestPoint = arrayDirection[i]
                return closestPoint

                # Write your bot here. Use functions from aiHelper to instantiate your actions.
                arrayDirection = []
                for i in range(21):
                    for j in range(21):
                        if gameMap.getTileAt(
                                Point(self.PlayerInfo.Position.x + i, self.PlayerInfo.Position.y + j)) == TileContent.Resource:
                            arrayDirection.append(Point(self.PlayerInfo.Position.x + i, self.PlayerInfo.Position.y + j))
                matrixPath = np.zeros([plusProche(self, arrayDirection).x, plusProche(self, arrayDirection).y])
                grid = Grid(matrix=matrixPath)
                start = grid.node(0, 0)
                end = grid.node(StorageHelper.read("positionCible").getX(), StorageHelper.read("positionCible").getY())

                actualClosest = plusProche(self, arrayDirection)


                xRange = abs(self.PlayerInfo.Position.x - actualClosest.x)
                yRange = abs(self.PlayerInfo.Position.y - actualClosest.y)
                matrixPath = np.zeros([xRange, yRange])


                for i in range(xRange):
                    for j in range(yRange):
                        if gameMap.getTileAt(self, Point(self.PlayerInfo.Position.x + i, self.PlayerInfo.Position.y + j)) == 0 or gameMap.getTileAt(self, Point(self.PlayerInfo.Position.x + i, self.PlayerInfo.Position.y + j)) == 4:
                            matrixPath[i, j] = 1
                        else:
                            matrixPath[i, j] = 0

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
