class Solution(object):
    def maximumWealth(self, accounts):
        mam=sum(accounts[0])
        for i in range(len(accounts)):
            if(mam<sum(accounts[i])):
                mam=sum(accounts[i])
        return(mam)