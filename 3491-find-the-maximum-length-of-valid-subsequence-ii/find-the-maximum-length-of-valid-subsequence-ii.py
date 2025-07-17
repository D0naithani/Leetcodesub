class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        overall_max_len = 0

        # Iterate through all possible values of R, where R is the constant value
        # of (sub[i] + sub[i+1]) % k for a valid subsequence.
        for R in range(k):
            # dp_for_R[rem_val] stores the maximum length of a valid subsequence
            # whose adjacent sum modulo k is R, and which ends with a number
            # whose modulo k value is rem_val.
            dp_for_R = [0] * k

            for num in nums:
                current_rem = num % k

                # max_len_ending_here represents the maximum length of a subsequence
                # that can be formed by including 'num' at the end, such that
                # its adjacent sum modulo k is 'R'.
                # It starts at 1, as 'num' itself can start a new subsequence of length 1.
                max_len_ending_here = 1

                # We need to find a 'prev_rem' such that (prev_rem + current_rem) % k == R.
                # This implies prev_rem = (R - current_rem + k) % k.
                needed_prev_rem = (R - current_rem + k) % k

                # If there's a valid subsequence ending with 'needed_prev_rem' (length > 0),
                # we can extend it by adding 'num'.
                if dp_for_R[needed_prev_rem] > 0:
                    max_len_ending_here = max(max_len_ending_here, dp_for_R[needed_prev_rem] + 1)
                
                # Update the DP table for the current 'num'.
                # We take the maximum of the current value in dp_for_R[current_rem]
                # and the 'max_len_ending_here' just calculated. This is important
                # because multiple paths could lead to the same 'current_rem'.
                dp_for_R[current_rem] = max(dp_for_R[current_rem], max_len_ending_here)
            
            # After processing all numbers for a fixed R, find the maximum length
            # achieved for this R.
            # We are interested in subsequences of length at least 2.
            # max(dp_for_R) will give the maximum length, and if it's 1 it means
            # only single-element subsequences were found.
            # Since nums.length >= 2, we are guaranteed to have at least two elements.
            # If for a given R, no length >= 2 subsequence exists, then max(dp_for_R) might be 1.
            # We just take max of all results, as max(dp_for_R) will be at least 1 if nums is not empty.
            # The problem guarantees nums.length >= 2, so the final answer will be at least 2 
            # if such a subsequence is possible.
            
            # The overall_max_len should ultimately store the maximum of all valid lengths.
            # Since any single number can technically start a sequence, dp values will be at least 1.
            # If a dp[x] value is >= 2, it means we have a valid subsequence of length >= 2.
            # If all dp values are 1, it means no valid subsequence of length >= 2 was found for this R.
            overall_max_len = max(overall_max_len, max(dp_for_R))
            
        return overall_max_len