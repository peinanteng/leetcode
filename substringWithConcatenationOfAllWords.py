class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        rsummary = {}
        res = []
        countWords = 0
        for word in words:
            summary[word] = summary.get(word, 0) + 1
            countWords += 1
        count = len(summary)
        start = 0
        wordlen = len(words[0])
        wordslen = len(words[0]) * countWords
        while start <= len(s) - wordslen:
            if s[start: start + wordlen] in words:
                slidingWindow = {}
                slidingCount = 0
                tempstart = start
                while slidingCount >= 0 and slidingCount < count:
                    word = s[tempstart: tempstart + wordlen]
                    if word in summary:
                        slidingWindow[word] = slidingWindow.get(word, 0) + 1
                        if slidingWindow[word] == summary[word]:
                            slidingCount += 1
                            tempstart += wordlen
                        elif slidingWindow[word] < summary[word]:
                            tempstart += wordlen
                        elif slidingWindow[word] > summary[word]:
                            slidingCount = -1
                    else:
                        slidingCount = -1
                if slidingCount == count:
                    res.append(start)
            start += 1

        return res
        

