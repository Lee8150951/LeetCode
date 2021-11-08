from collections import Counter
class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    times = len(secret)
    s_dictory, g_dictory = Counter(), ""
    bulls, cows = 0, 0
    for i in range(times):
      if secret[i] == guess[i]:
        bulls += 1
      else:
        s_dictory[secret[i]] += 1
        g_dictory += guess[i]
    for i in g_dictory:
      if i in s_dictory and s_dictory[i] > 0:
        s_dictory[i] -= 1
        cows += 1
    return f'{bulls}A{cows}B'


if __name__=="__main__":
  secret = "1"
  guess = "1"
  method = Solution()
  answer = method.getHint(secret, guess)
  print(answer)