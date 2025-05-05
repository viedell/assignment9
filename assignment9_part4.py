import statistics

input_stats = input("Enter atleast 5 numbers, seperated by spaces!")
stats_list = list(map(float, input_stats.split()))

if len(stats_list) < 5:
    print("Error! 5 numbers please")
else:
    print("Sorted list: ", sorted(stats_list))
    print("Minimum: ", min(stats_list))
    print("Maximum: ", max(stats_list))
    print("Average: ", sum(stats_list) / len(stats_list))
    print("Median: ", statistics.median(stats_list))