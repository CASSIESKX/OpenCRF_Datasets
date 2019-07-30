"""
Creating a file that contains edges in the graph.

Format: #edge userLine reviewLine UR
        #edge productLine reviewLine PR

Intuition:
Review Line Number: Starting from 1 (1 ~ 67395)
User line number: 67396 ~ 105458
Product: 105459 ~ 105659

User line number = userID + 67195 since the user starts from line 67396
and user id starts from 201.
Product line number = productID + 1054599 since the product starts from
line 105459 and product id starts from 0.
Review line number: always start from 1 and keeps incrementing.

"""

outfile = open("EdgesAndNodesZip.txt", "w")

# FIXED_NUM_UR = how many reviews
# FIXED_NUM_PR = the first line of products 

FIXED_NUM_UR = 145
FIXED_NUM_PR = 38209
starting_line = 1


with open("user_product_pairs.txt") as textFile:
    # 2-D list
    user_product_pairs = [line.split() for line in textFile]

for row in user_product_pairs:
    line_number = int(row[0], 10) + FIXED_NUM_UR
    outfile.write("#edge " + str(line_number) + " " + str(starting_line) + " UR\n")
    starting_line = starting_line + 1

starting_line = 1
for row in user_product_pairs:
    line_number = int(row[1], 10) + FIXED_NUM_PR
    outfile.write("#edge " + str(line_number) + " " + str(starting_line) + " PR\n")
    starting_line = starting_line + 1

outfile.close()



