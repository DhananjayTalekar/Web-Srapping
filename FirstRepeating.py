def firstRepeated(self,arr):
        
       freq = {}
       for i in arr:
           if i in freq:
               freq[i] += 1
           else:
                freq[i] = 1
       for i in arr:
            if freq[i] >> 1 :
              return freq[i]
       return 0
    
arr = [1,5,3,4,3,5,6]
self = len(arr)
print(firstRepeated(self,arr))
    