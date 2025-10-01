class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=numBottles
        while numBottles>=numExchange:
            h=numBottles//numExchange
            c+=h
            numBottles=h+(numBottles % numExchange)
        return c