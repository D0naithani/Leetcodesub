class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        N = len(startTime)
        
        # 1. Calculate all free time gaps (including before the first meeting and after the last meeting).
        # We define Gaps[i] as the free time between meeting i-1 and meeting i.
        # Gaps[0] is from time 0 to startTime[0].
        # Gaps[N] is from endTime[N-1] to eventTime.
        gaps = [0] * (N + 1)
        
        gaps[0] = startTime[0]
        for i in range(1, N):
            gaps[i] = startTime[i] - endTime[i-1]
        gaps[N] = eventTime - endTime[N-1]
        
        # 2. Precalculate Prefix Maximum Gaps (MaxLeftGaps) and Suffix Maximum Gaps (MaxRightGaps).
        # MaxLeftGaps[i] stores the maximum gap from gaps[0] to gaps[i].
        # MaxRightGaps[i] stores the maximum gap from gaps[i] to gaps[N].
        
        max_left_gaps = [0] * (N + 1)
        max_right_gaps = [0] * (N + 1)
        
        # Calculate MaxLeftGaps
        max_left_gaps[0] = gaps[0]
        for i in range(1, N + 1):
            max_left_gaps[i] = max(gaps[i], max_left_gaps[i-1])
            
        # Calculate MaxRightGaps
        max_right_gaps[N] = gaps[N]
        for i in range(N - 1, -1, -1):
            max_right_gaps[i] = max(gaps[i], max_right_gaps[i+1])
            
        # 3. Iterate through each meeting (from 0 to N-1) and consider rescheduling it.
        max_free_time = 0
        
        # We also need to consider the initial maximum free time if no meeting is moved.
        max_free_time = max(gaps)
        
        for i in range(N):
            # Duration of the current meeting i
            duration = endTime[i] - startTime[i]
            
            # Gaps adjacent to meeting i are gaps[i] (before) and gaps[i+1] (after).
            
            # We need to find the maximum gap available outside of the adjacent gaps 
            # (i.e., not gaps[i] and not gaps[i+1]).
            
            # This is the maximum of the gaps to the left of gaps[i] (indices 0 to i-1)
            # and the gaps to the right of gaps[i+1] (indices i+2 to N).

            G_max_other = 0

            # Max gap to the left (before gaps[i]): max_left_gaps[i-1]
            if i > 0:
                G_max_other = max(G_max_other, max_left_gaps[i-1])

            # Max gap to the right (after gaps[i+1]): max_right_gaps[i+2]
            # We check if i+2 is a valid index (up to N).
            if i + 2 <= N:
                G_max_other = max(G_max_other, max_right_gaps[i+2])
            
            
            # Calculate the free time if we remove meeting i, which is the combined gap
            # of the space before, the meeting duration, and the space after.
            # This is equivalent to (startTime[i+1] - endTime[i-1]) assuming the boundary conditions are handled by gaps[i] + duration + gaps[i+1] 
            
            # Wait, the combined length is simply the difference between the start of the next meeting 
            # and the end of the previous meeting, which is gaps[i] + duration + gaps[i+1]
            
            # The length of the combined free space if meeting i is removed: 
            # G_i_combined = (startTime[i] - endTime[i-1]) + duration + (startTime[i+1] - endTime[i]) 
            # G_i_combined = gaps[i] + duration + gaps[i+1]

            # We can simplify G_i_combined to: 
            # (endTime[i-1] + gaps[i]) + (duration) + (gaps[i+1]) = startTime[i] + duration + gaps[i+1] 
            # G_i_combined = (endTime[i] + gaps[i+1]) - endTime[i-1] = startTime[i+1] - endTime[i-1]

            # Since the input guarantees non-overlapping and sorted meetings, we can use the original indices.
            
            # We are interested in the free time if meeting i is removed, and we successfully place it somewhere else.
            
            # If we can fit the meeting (duration <= G_max_other), we move it to the largest non-adjacent gap.
            # This frees up the space occupied by meeting i. 
            
            if duration <= G_max_other:
                # We can move meeting i to G_max_other. The new longest free time 
                # will be the combined space created by removing meeting i.
                
                # We need to calculate the combined space: 
                # It's startTime[i+1] - endTime[i-1] (conceptually)
                # Using the gaps: gaps[i] + duration + gaps[i+1]
                
                combined_gap_size = gaps[i] + duration + gaps[i+1]
                max_free_time = max(max_free_time, combined_gap_size)

            else:
                # We cannot move meeting i into a larger non-adjacent gap. 
                # If we move it to a smaller gap, or if we don't move it, the longest free time 
                # we can achieve is the maximum of 
                # 1. The original gaps: gaps[i] and gaps[i+1]
                # 2. The combined gap if we remove i, minus the duration D_i: gaps[i] + gaps[i+1]
                
                # The free time is the sum of the adjacent gaps: gaps[i] + gaps[i+1]. 
                # If we can't move the meeting, the maximum continuous free time is defined by the existing gaps. 
                
                # However, if we move meeting i to a gap that is exactly equal to D_i, 
                # the free time in that gap becomes 0, and the free time in the original spot is gaps[i] + gaps[i+1] + duration. 
                
                # If D_i > G_max_other, we are forced to place meeting i in a location that is either in gaps[i] or gaps[i+1], 
                # or a gap smaller than D_i.
                
                # If we don't move it, the max free time is max(gaps).
                
                # If we move it to a gap smaller than D_i, the meetings overlap, which is not allowed.
                
                # If duration > G_max_other, we cannot move the meeting to a gap outside of the adjacent gaps without overlap.
                # If we choose to move it within the adjacent gaps, we reduce the free space there.
                
                # The logic should be: if we can fit meeting i in a non-adjacent gap, we gain the combined gap size.
                # If we cannot, the free time at this specific position remains only the gaps before and after.
                
                # If we cannot move it (duration > G_max_other), we can at least consider the original free time 
                # which we already tracked in `max_free_time`. We only gain if duration <= G_max_other.
                
                # The combined free time if we just squash the meetings together (no move to G_other) is gaps[i] + gaps[i+1].
                max_free_time = max(max_free_time, gaps[i] + gaps[i+1])


        return max_free_time