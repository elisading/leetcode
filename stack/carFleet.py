class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        time = [(target - p) / s for p, s in cars]

        prev_time = 0
        for t in reversed(time):
            if t > prev_time:
                fleets += 1
                prev_time = t

        return fleets


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        arrive_time = []

        for p, s in reversed(cars):
            dist = target - p
            time = dist / s
            if not arrive_time:
                arrive_time.append(time)
            elif time > arrive_time[-1]:
                arrive_time.append(time)

        return len(arrive_time)
