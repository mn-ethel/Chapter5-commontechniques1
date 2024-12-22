scores = []

for i in range(10):
    score = int(input(f"Enter test score {i+1}: "))
    scores.append(score)

highest_score = max(scores)
lowest_score = min(scores)
print("The highest score is: ", highest_score)
print("The lowest score is: " ,lowest_score)


average_score = sum(scores) / len(scores)
print("The average score is: ",average_score)

sorted_scores = sorted(scores, reverse=True)
second_largest_score = sorted_scores[1]
print("The second largest score is: ", second_largest_score)


if any(score > 100 for score in scores):
    print("Warning: A value over 100 has been entered.")


sorted_scores = sorted(scores)
remaining_scores = sorted_scores[2:]
average_remaining_scores = sum(remaining_scores) / len(remaining_scores)
print(f"The average score after dropping the two lowest scores is: {average_remaining_scores:.2f}")
