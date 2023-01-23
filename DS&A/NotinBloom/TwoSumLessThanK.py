def twoSumLessThanK(Array, k):
        sorted(Array);
        start = 0;
        end = len(Array)- 1;
        ans = -1;
        while (start < end):
            if (Array[start] + Array[end] >= k):
                end-=1
            else: #(Array[start] + Array[end] < k)
                ans = max(ans, Array[start] + Array[end]);
                start+=1
        return ans

Array = [5, 20, 110, 100, 10];
k = 85;

print(twoSumLessThanK(Array, k))
#####################################################################################################
