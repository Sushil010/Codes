class Solution(object):
    def numberOfSteps(self, num):
        sums=0
        while(num!=0):
            if(num%2==0):
                num=num/2
            else:
                num=num-1
            
            sums=sums+1    
        
        return(sums)