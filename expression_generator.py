print(".......Let's Implement Generator Expression:.......\n")
sequence_ = [12, 123, 11, 23, 56, "Done"]
gener_exp = (ge for ge in sequence_)

print("The Type Of gener_exp:", type(gener_exp))
for ge_demons in gener_exp:
    print(ge_demons)