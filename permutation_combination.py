# Itertools uses: permutation, combination...........
from itertools import permutations, combinations, combinations_with_replacement
print("Let's Facilitate Itertools")
print("\n\t ===== Permutations - Combinations ====:")
n = int(input("Enter The The No. of Initial Elements(n):"))
r = int(input("Enter how many elem/items want to pick(r):"))

# items_n = [1, 2, 3, 4]
items_n = []
for elem in range(n):
    items_n.append(input("Now Enter The %dth Elements/Items: " % elem))

print("\n\tPress 1 To Perform Permutation:")
print("\tPress 2 To Perform Combinations:")
print("\tPress 3 To Perform combinations_with_replacement:")

try:
    press_ = int(input("Enter Your Pressing Choice:"))
    if press_ == 1:
        perm_li = list(permutations(items_n, r))
        print("The Permutation of the Items_: ", perm_li)
        print("The Result(len_value-Permutation_Value) Of Permutation: nPr(4P2): ",
              len(perm_li))  # from itertools automatically formula: (n!)/(n-r)!
    elif press_ == 2:
        # nCr = (n!/(n-r)!*r!)
        # all combinations are uniquely defined in combinations
        print("\n\t Combination:")
        comb_li = list(combinations(items_n, r))
        print("The Combinations of the Items_: ", comb_li)
        print("The Result(len_value-Combinations_Value) Of Combinations: nCr(4C2): ", len(comb_li))  # from itertools automatically formula: (n!)/(n-r)!

    elif press_ == 3:
        # combinations_wit_replacement
        # allows us to sample elements/items twice or again
        # what can't be performed in combinations
        print("Combination With Replacement:")
        comb_replace_li = list(combinations_with_replacement(items_n, r))
        print("The Combinations_with_replacement of the Items_: ", comb_replace_li)
        print("The Result(len_value-comb_replace_li) Of Combinations: nCr(4C2): ",
              len(comb_replace_li))  # from itertools automatically formula: comb_little bit different


    else:
        print("Sorry! Your Choice is out of Option. Try Again Please.")

except ValueError:
    print("Enter Your Choice Properly in Number Format!")



# print("{2} - {0} and finally {1}".format("idea", "implementation", "maintained"))

