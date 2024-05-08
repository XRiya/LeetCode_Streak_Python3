class Solution(object):
    def findRelativeRanks(self, score):
        # Step 1: Initializations
        N = len(score)
        max_score = max(score)
        rank = [None] * N
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        score_to_index = [0] * (max_score + 1)

        # Step 2: Creating Map Array
        for i, s in enumerate(score):
            score_to_index[s] = i + 1

        # Step 3: Assigning Rank
        place = 1
        for i in range(max_score, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place <= 3:
                    rank[original_index] = medals[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1

        return rank
