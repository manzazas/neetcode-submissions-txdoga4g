class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #If two cars collide, choose the smaller speed
        '''
        Pos, speed:
        [[0,1],[1,2],[4,2],[7,1]]
        '''
        cars = []
        for i in range(0,len(speed)):
            cars.append([position[i],speed[i]])
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        fleets = []
        for i in range(0,len(cars)):
            fleets.append((target - cars[i][0]) / cars[i][1])
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            
        return len(fleets)

            





        