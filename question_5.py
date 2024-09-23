# Question 5
# Let Y be a gamma random variable with a shape parameter s = 3 and rate parameter α = 4, and let X|Y=y follow a
# Poisson distribution with mean y.
s = 3
alpha = 4
# Find the unconditional mean E(X).
unconditional_mean = s / alpha
print("The unconditional mean E(X) is {}.".format(unconditional_mean))

# (b) Show that the conditional distribution of Y given X = x is gamma with parameters (s + x, α + 1).

# (c) Using the result from part (b), calculate the posterior mean of Y given that X = 4.
x = 4
s += x
alpha += 1
posterior_mean = s / alpha
print("The posterior mean of Y given that X = 4 is {}.".format(posterior_mean))
