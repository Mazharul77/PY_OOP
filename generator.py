# Let's Implement The Generator In Python:
# 1-Time Use:
# Use Of Yield(Like Return(though it doesn't return back where it was ended
# and also returned back in generator when required...
# Ex: Generate Sequence without  memory Loading....1 by 1 item returns

print("Facilitate Generator(1-time Use) In Python:")


def fun_gen(size):
    traverse = 0
    while traverse < size:
        yield traverse  # like return along with returned back when called
        traverse += 1


n = 10  # we take input from user console also
gnr_obj = fun_gen(n)

print("\n")
for g in gnr_obj:
    print(g)

# lets check 1 time generator whether we can access / iterate again or not
print("\n\tTrying To access Generator Again: But Can't as it's 1-time(generator) Use...")
for g_call_2 in gnr_obj:
    print(g_call_2)

# StopIteration (If try to access the next item existence)
# it'll return error/nothing since already 1-time used
# print(gnr_obj.__next__())

