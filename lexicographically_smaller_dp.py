s1 = input().strip()
s2 = input().strip()  


def lexico_smaller(s1,s2):
    n,m = len(s1), len(s2)    

    dp = [["" for _ in range(m + 1)] for _ in range(n + 1) ]

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = s1[i] + dp[i + 1][j + 1]
            else:
                if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                    dp[i][j] = dp[i + 1][j]
                elif len(dp[i + 1][j]) < len(dp[i][j + 1]):   
                    dp[i][j] = dp[i][j + 1]
                else:   
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])  
    return dp[0][0]  

print(lexico_smaller(s1,s2) )
                

 
              