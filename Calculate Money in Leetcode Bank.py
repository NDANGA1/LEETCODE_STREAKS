# Problem 1716: Calculate Money in Leetcode Bank
# Hercy deposits money in the bank every day following a weekly pattern:
# - On the first Monday, he deposits $1.
# - Each following day of the same week, he deposits $1 more than the previous day.
# - Each new Monday, the deposit starts $1 more than the previous Monday’s deposit.
# Given n days, the task is to calculate the total amount of money saved after n days.
# Examples:
# n = 4 → total = 1 + 2 + 3 + 4 = 10
# n = 10 → total = (1+2+3+4+5+6+7) + (2+3+4) = 37
# n = 20 → total = (1+2+3+4+5+6+7) + (2+3+4+5+6+7+8) + (3+4+5+6+7+8) = 96
# Constraints: 1 <= n <= 1000

#_________________________________SOLUTION_____________________________________

#update a day "c" after you update amount "i" and update "total"
#we start with day "c"=0 and amount "i"=0 inorder to give room for day 1 to have amount 1 deposited
#also it must be 0s cuz we havent entered into the days yet
i = 0
c = 0
total = i
while  c < n:#rem a day is incremented at the end of the block,so n must have already been reached
    #cheking at c on top of block and updating c below it(also starting with 0) means that c might have been already been visited in many codes other casestudies
    if c>0 and c % 7 == 0:#div by 7 must already been reached updated at end of block so this is next day after it,so we are in day 8 which will be updated lower the block
        #rem this update at end of block makes whenever you encounter c its the past day
        #so i mean since you are in day 8 then last day was Sunday day 7 and its Monday is day 1 (7-1=6) so its i-6 but plus 1 due to instructions
        i -= 5
        c += 1
        total += i
        continue
    i += 1
    c += 1
    total += i





