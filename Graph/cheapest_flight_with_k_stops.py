class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [10**9] * n

        prices[src] = 0
        for i in range(k+1):
            # print("inn")
            temp = prices.copy()
            for u, v, w in flights:
                # print(prices[v])
                # print(prices[u]+w)
                temp[v] = min(temp[v], prices[u] + w)
            prices = temp
            # print(prices)

        return prices[dst] if prices[dst] < 10 ** 9 else -1
        

        

        