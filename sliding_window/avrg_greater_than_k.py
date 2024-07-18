class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        avrg = 1
        count = 0
        start = 0
        ans = 0

        i = 0
        n = len(arr)

        while(i < n):
            sum += arr[i]
            count += 1 
            avrg = sum // count
            end = i
            if end - start + 1 == k :
                if(avrg >= threshold):
                    ans += 1
                sum -= arr[start]
                count -= 1
                avrg = sum // count if count > 0 else 1
            i += 1
            
        return ans


            