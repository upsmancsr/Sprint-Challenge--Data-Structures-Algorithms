Add your answers to the Algorithms exercises here.

Exercise I:
a) 
While a < n^3, a = a + n^2. One question is how quickly does a + n^2 approach n^3? Also, as n increases the limit increases by n^3, which grows faster than a + n^2. Another note is that a + n^2 is basically dominated by n^2. An estimation of the time complexity would be that it is O(n^3) - something to account for a = n^2. Honestly I have no idea and I am just writing stuff down do provide "analysis."

b)
I think it would be O(4n) because there are 4 loops to run for each n.

c) 
O(n)

Exercise II:

You could start by dropping an egg from floor n = n/2. If it breaks, drop an egg from floor n = n/2, and so on, until an egg does not break. At that point, drop an egg from floor n = n*1.5, continuing with this back and forth splitting the difference until you converge on a floor where a dropped egg does not break, but going up one floor will break the egg.
