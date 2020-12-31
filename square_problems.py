# Questions asked by Square
# 1 Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.
# Write a function to simulate an unbiased coin toss.

# Ref link: https://stackoverflow.com/questions/5429045/c-puzzle-make-a-fair-coin-from-a-biased-coin/5429219#5429219
# This can be viewed as a probablity problem where the observation is that if you have a biased coin that comes up heads with probability p, 
# and if you flip the coin twice, then:
#     The probability that it comes up heads twice is p^2
#     The probability that it comes up heads first and tails second is p(1-p)
#     The probability that it comes up tails first ands heads second is (1-p)p
#     The probability that it comes up tails twice is (1-p)^2

# if you keep flipping two coins until they come up with different values, then take the value of the first coin you flipped, you end up making a fair coin 
# from a biased coin

def toss_unbiased:
  coin1 = toss_biased(); coin2 = toss_biased()
  while coin1 = coin2:
      coin1 = toss_biased(); coin2 = toss_biased()
  return coin1


