class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<=2:
            return False

        countup=0
        slope=[]
        i=1
        while i<=len(arr)-1:
             if arr[i]>arr[i-1]:
                    slope.append('up')
                    countup+=1
                    i+=1

             elif arr[i]<arr[i-1]:
                    slope.append('down')
                    i+=1
             else: 
                    slope.append('flat')
                    i+=1
        idx=len(slope)-countup

        if slope[0]=='down':
            return False
        if 'up' in  slope[-idx:]:
            #print('Not a Mountain')
            return False

        elif 'flat' in slope[-idx:]:
            return False
        else:
            #print('Mountain Array')
            return True
