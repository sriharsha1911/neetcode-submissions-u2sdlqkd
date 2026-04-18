class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_lis=[]
        t_sum=0
        for i in range(0,len(operations)):
            if operations[i]=='+':
                a=my_lis[-2]+my_lis[-1]
                my_lis.append(a)
                t_sum=t_sum+a
            elif operations[i]=='C':
                t_sum=t_sum-my_lis[-1]
                a=my_lis.pop()
            elif operations[i]=='D':
                a=2*my_lis[-1]
                my_lis.append(a)
                t_sum=t_sum+a
            else:
                my_lis.append(int(operations[i]))
                t_sum=t_sum+int(operations[i])
        return t_sum

