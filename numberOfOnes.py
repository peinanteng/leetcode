class numberOfOnes():
        def __init__(self, nums):
            self.nums = nums
            self.guess = nums[:][:]
            if self.guess:
                self.makeGuess()
        def makeGuess(self):
            guess = self.guess
            m = len(guess)
            n = len(guess[0])
            for i in range(1, m):
                guess[i][0] += guess[i - 1][0]
            for j in range(1, n):
                guess[0][j] += guess[0][j - 1]
            for i in range(1, m):
                for j in range(1, n):
                    guess[i][j] = guess[i][j - 1] + guess[i - 1][j] - guess[i - 1][j - 1] + self.nums[i][j]
            
        def countOnes(self, x1, y1, x2, y2):
            guess = self.guess
            nums = self.nums
            return guess[x2][y2] - guess[x1][y2] - guess[x2][y1] + guess[x1][y1]

