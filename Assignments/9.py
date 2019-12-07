from prettytable import PrettyTable
parta_table = PrettyTable(['Code', 'x', 'Fitness', 'Probability', 'Cumulative Probability'])
partb_table = PrettyTable(['Code', 'x', 'Fitness', 'Rank', 'Probability', 'Cumulative Probability'])

from bisect import bisect

individuals = [
        0b100001,
        0b100011,
        0b011100,
        0b011000,
        0b010000,
        0b110010,
        0b001010,
        0b000101,
        0b111101,
        0b000010,
    ]

random_numbers = [
        0.2319,
        0.2393,
        0.0498,
        0.0784,
        0.6408,
        0.1909,
        0.8439,
        0.1739,
        0.1708,
        0.9943,
    ]

fitness_function = lambda x: 1/(1+ (x-32)**2)

data = [(f"{x:06b}", int(x), fitness_function(x)) for x in individuals]
data = sorted(data, key=lambda x: x[2])

fitness_sum = sum(f for (_, _, f) in data)

parta = [(*data[0], data[0][2]/fitness_sum, data[0][2]/fitness_sum)]
for i in range(1, 10):
    prob = data[i][2]/fitness_sum
    parta.append((*data[i], prob, prob + parta[i-1][4]))

for (code, x, fitness, prob, cum_prob) in parta:
    parta_table.add_row([code, x, fitness, prob, cum_prob])


cum_prob = [c[4] for c in parta]
chosen_ones = list()
for r in random_numbers:
    chosen_ones.append(parta[bisect(cum_prob, r)][0])

print("Part a) Fitness Proportional selection")
print(parta_table)
print()
print("Selected intermediate population using the random numbers")
print(chosen_ones)
print([int(i, 2) for i in chosen_ones])

print()
print()
rank_sum = sum(range(1, 11))
partb = [(*data[0], 1, 1/rank_sum, 1/rank_sum)]
for i in range(1,10):
    rank = i + 1
    partb.append((*data[i], rank, rank/rank_sum, partb[i-1][5] + rank/rank_sum))

for x in partb:
    partb_table.add_row([*x])

cum_prob = [c[5] for c in partb]
chosen_ones = list()
for r in random_numbers:
    chosen_ones.append(parta[bisect(cum_prob, r)][0])
print("Part b) Ranked Selection")
print(partb_table)
print()
print("Selected intermediate population using the random numbers")
print(chosen_ones)
print([int(i, 2) for i in chosen_ones])


