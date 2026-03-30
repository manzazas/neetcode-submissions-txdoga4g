class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #loop through each car, and find how many hours it takes to reach the target
        #for each car that reaches the target at the same time, they are a fleet
        #target - position[i] // speed[i] (round up)
        stacky = []
        newlist = []
        for i in range(0,len(position)):
            newlist.append((position[i],speed[i]))
        newlist.sort()
        for i in range(len(newlist) - 1, -1, -1):
            time = (target - newlist[i][0]) / newlist[i][1]
            if stacky:
                if stacky[-1] >= time:
                    continue
                else:
                    stacky.append(time)
            else:
                stacky.append(time)

        return len(stacky)




        """
        [1,12,7,3]
        """



        