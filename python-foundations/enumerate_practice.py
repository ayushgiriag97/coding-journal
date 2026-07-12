# ==============================================================================
# PHASE: Python Foundations
# TOPIC: The Enumerate Function & Custom Offsets (Day #42)
# MANDATE: Use enumerate() explicitly. Do not declare manual tracking variables.
# ==============================================================================

# ------------------------------------------------------------------------------
# feat: implement human-readable ranking leaderboard
# ------------------------------------------------------------------------------
# EXERCISE 1: The Human-Readable Ranking
# Objective: Loop through the racers. Format the leaderboard so that the first 
#            person is rank 1, the second is rank 2, etc.

racers = ["Alice", "Bob", "Charlie", "Diana"]

for rank, name in enumerate(racers):
    print(f"rank: {rank+1}      racer name: {name}")

# ------------------------------------------------------------------------------
# feat: filter sensor logs using specific even index criteria
# ------------------------------------------------------------------------------
# EXERCISE 2: Even Index Filter
# Objective: Start counting at an offset of 10. Loop through the logs and print 
#            the log string *only* if its calculated index is an even number.

logs = ["Init", "Load_Data", "Process_1", "Process_2", "Save_Output", "Close"]

for index, value in enumerate(logs, start=10):
    if index %2 == 0:
        print(value)

# ------------------------------------------------------------------------------
# feat: correct the sequence unpacking structure in inventory loop
# ------------------------------------------------------------------------------
# EXERCISE 3: Spot the Sequence Unpacking Bug
# Objective: Correct the junior developer's code. Fix the unpacking sequence in 
#            the loop header so that the data maps to the correct variables.

inventory = ["GPU", "CPU", "RAM", "Motherboard"]

for index, value in enumerate(inventory ,start=1):
    print(f"{index} : {value}")

# ------------------------------------------------------------------------------
# feat: intercept data stream and bypass configuration header row
# ------------------------------------------------------------------------------
# EXERCISE 4: Skipping the Header Row
# Objective: Start counting from 1. If the calculated count is 1 (the header), 
#            skip execution using the 'continue' keyword. Print all other lines.

csv_lines = ["HEADER_CONF_8823", "data_point_A", "data_point_B", "data_point_C"]

for index,value in enumerate(csv_lines, start=1):
    if index == 1:
        continue
    else:
        print(value)

# ------------------------------------------------------------------------------
# feat: intercept raw tuple stream for targeted index evaluation
# ------------------------------------------------------------------------------
# EXERCISE 5: Targeted Tuple Extraction Challenge
# Objective: Use a single loop variable (no tuple unpacking in the header). 
#            Start at 100. Access elements via tuple indexing, and print the 
#            item *only* if the index is exactly 102.

models = ["ResNet", "VGG", "BERT", "GPT"]

for pack in enumerate(models, start=100):
    if pack[0] == 102:
        print(pack)
    else:
        continue