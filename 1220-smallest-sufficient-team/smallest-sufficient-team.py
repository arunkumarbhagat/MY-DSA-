class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        # Step 1: Map skills to bits
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)
        
        # Step 2: Convert people skills to bitmask
        people_masks = []
        for person in people:
            mask = 0
            for skill in person:
                if skill in skill_index:
                    mask |= (1 << skill_index[skill])
            people_masks.append(mask)
        
        # Step 3: DP (mask → team)
        dp = {0: []}
        
        for i, person_mask in enumerate(people_masks):
            if person_mask == 0:
                continue
            
            for prev_mask, team in list(dp.items()):
                new_mask = prev_mask | person_mask
                
                if new_mask == prev_mask:
                    continue
                
                # update if smaller team
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]
        
        full_mask = (1 << n) - 1
        return dp[full_mask] 