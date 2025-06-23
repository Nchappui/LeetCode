class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senateL = list(senate)
        radiantBan = 0
        radiantCount = 0
        direBan = 0
        direCount = 0
        dead = 0
        turn = 0
        while True:
            for i in range(n):
                if senateL[i] == 'R':
                    if direBan:
                        direBan -= 1
                        senateL[i] = 'O'
                        dead += 1
                    else:    
                        radiantBan += 1
                        radiantCount += 1
                elif senateL[i] == "D":
                    if radiantBan:
                        senateL[i] = 'O'
                        dead += 1
                        radiantBan -= 1
                    else:
                        direBan += 1
                        direCount += 1
                else:
                    dead+= 1
            turn += 1           
            if direCount and not radiantCount:
                return 'Dire'
            elif radiantCount and not direCount:
                return 'Radiant'
            dead = direCount = radiantCount = 0
                    
print(Solution().predictPartyVictory("RRRRDDDDD"))
print(Solution().predictPartyVictory("RDRD"))
print(Solution().predictPartyVictory("RDD"))
print(Solution().predictPartyVictory("RDR"))
print(Solution().predictPartyVictory("DRD"))