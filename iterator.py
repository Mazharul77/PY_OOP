# iter(): 1 by 1 iteration,
# __iter__()
# iter().__next__(): immediate next items access,
# ... automatically stop iteration when iteration reaches to end

print("...... Iterator Concept : Like Software Release(after some update) .......")
# Dictionary iter() , 1 by 1 next key/val access:
dict_ = {"software": "CRM-management", "trend": "Python", "Key": "value", }
var_dict_ = iter(dict_.items())
print(var_dict_.__next__())
print(var_dict_.__next__())
print(var_dict_.__next__())
# print(var_dict_.__next__())  # StopIteration : Here-iteration will be stopped as it reaches to end

# Another List Iteration and next val access with loop:
lists_ = ['asd', 123, 'jkl', ';', 456, 0]
it_ = iter(lists_)
print("\nThe Type of it_:", type(it_))
for item in it_:
    print("The Iter Items:", item)

# Let's Check The Next Iteration (whether next iterable items ends or existed):
print("\n\t ... Iteration Ended ...")
print(it_.__next__())