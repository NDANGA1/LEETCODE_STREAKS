# Problem 2125: Number of Laser Beams in a Bank
# You are given a binary string array 'bank' representing the floor layout of a bank’s security system.
# Each string corresponds to a row, where '1' indicates a security device and '0' indicates an empty space.
#
# A laser beam exists between two devices if:
# 1. They are in different rows (r1 < r2)
# 2. All rows between r1 and r2 have no security devices.
#
# Thus, beams only form between consecutive non-empty rows.
# If one row has 'a' devices and the next non-empty row has 'b' devices,
# the number of beams formed between them is (a * b).
#
# The task is to return the total number of laser beams across the entire bank.
#
# Constraints:
# 1 <= m, n <= 500
# bank[i][j] is either '0' or '1'

# Solution Intuition:
# The main idea is to only consider consecutive non-empty rows (those having at least one '1').
# We keep track of the number of devices in the last non-empty row (prev).
# For every new row, if it has devices (curr > 0), multiply it by prev (beams between the two rows),
# add the result to the total, and then set prev = curr.
# This way, we skip all empty rows automatically and ensure beams are only formed between valid rows.

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0  # Total number of beams formed
        prev = 0  # Number of devices in the last non-empty row

        # Traverse each row in the bank
        for row in bank:
            curr = row.count('1')  # Count devices ('1') in the current row

            if curr > 0:
                # Beams form only between consecutive non-empty rows
                total += prev * curr
                # Update prev for the next comparison
                prev = curr

        return total  # Return the total beams count
