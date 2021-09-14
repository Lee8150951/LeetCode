from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = list()
        for i in sorted(dictionary):
            s_list = list(s)
            ans.append(i)
            for j in i:
                if j in s_list:
                    s_list = s_list[s_list.index(j) + 1:]
                elif j not in s_list:
                    ans.pop()
                    break
        length = [len(i) for i in ans]
        if length:
            return ans[length.index(max(length))]
        else:
            return ""

if __name__=="__main__":
  s = "aewfafwafjlwajflwajflwafj"
  dictionary = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
  method = Solution()
  answer = method.findLongestWord(s, dictionary)
  print(answer)