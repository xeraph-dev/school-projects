# line = input()
# line_split = line.split(" ")

# count = int(line_split[0])
# idx = int(line_split[1]) - 1

# line = input()
# scores = [int(score) for score in line.split(" ")]
# min_score = scores[idx]

# result = sum(1 for score in scores if 0 < score >= min_score)

# print(result)

idx = int(input().split(" ")[1]) - 1
scores = [int(score) for score in input().split(" ")]
print(sum(1 for score in scores if 0 < score >= scores[idx]))
