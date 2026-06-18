class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # car cannot pass car ahead of it can only catch up
        # car fleet = cars driving same position/speed
        # return # car fleets 
        # target = 10
        # position = [4 1 0 7]
        # speed = [2 2 1 1]

        # position  [0 1 4 7]
        # speed     [1 2 2 1]
        # 1         [1 3 6 8]
        # 2         [2 5 8 9]
        # 3         [3 7 10 10]
        # 4         [4 9 10 10]
        # 5         [5 11 10 10]
        # target = position + speed x time
        # time = (target - position) / speed (!!)
        # time = (10 - 7) / 1 = 3
        # time = (10 - 4) / 2 = 2
        # time = (10 - 1) / 2 = 5 (round up)
        # time = (10 - 0) / 1 = 10 (round up)   

        # STACK | time: O(nlogn), space: O(n)
        # sort (position, speed) in descending order so closer cars processed first
        # for each car, compute time to reach target
        # add car time to stack
        # if next car reaches target before/same time, fleet formed, remove from stack

        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse = True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
