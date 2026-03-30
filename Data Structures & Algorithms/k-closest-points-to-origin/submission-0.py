class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = {}
        for x,y in points:
            dist = math.sqrt((x - 0)** 2 + (y - 0)**2)
            if dist in dist_map:
                dist_map[dist].append([x,y])
            else:
                dist_map[dist] = [[x,y]]



        #{3:(0,1), 5:(2,4)}

        distances = []
        heapq.heapify(distances)
        for keys in dist_map:
            heapq.heappush(distances,keys)
        i = 0
        res = []
        while i < k:
            distance = heapq.heappop(distances)
            for coords in dist_map[distance]:
                res.append(coords)
                i += 1
                if i == k:
                    break

        return res





        



        