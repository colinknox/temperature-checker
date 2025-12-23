#!/usr/bin/python3

def is_freezing(temp):
    return temp <= 32

def is_hot(temp):
    return temp >= 90

def is_comfortable(temp):
    return 65 <= temp <= 75

def needs_jacket(temp):
    return temp < 60

def is_boiling(temp):
    return temp >= 212

# # is_freezing TEST
# test1 = is_freezing(31)
# test2 = is_freezing(32)
# test3 = is_freezing(33)

# print(f"""
# TEST 1: {test1}
# TEST 2: {test2}
# TEST 3: {test3}
# """)

# # is_hot TEST
# test1 = is_hot(89)
# test2 = is_hot(90)
# test3 = is_hot(91)

# print(f"""
# TEST 1: {test1}
# TEST 2: {test2}
# TEST 3: {test3}
# """)

# # is_comfortable TEST
# test1 = is_comfortable(64)
# test2 = is_comfortable(65)
# test3 = is_comfortable(66)
# test4 = is_comfortable(74)
# test5 = is_comfortable(75)
# test6 = is_comfortable(76)

# print(f"""
# TEST 1: {test1}
# TEST 2: {test2}
# TEST 3: {test3}
# TEST 4: {test4}
# TEST 5: {test5}
# TEST 6: {test6}
# """)

# # needs_jacket TEST
# test1 = needs_jacket(59)
# test2 = needs_jacket(60)
# test3 = needs_jacket(61)

# print(f"""
# TEST 1: {test1}
# TEST 2: {test2}
# TEST 3: {test3}
# """)

# # is_boiling TEST
# test1 = is_boiling(211)
# test2 = is_boiling(212)
# test3 = is_boiling(213)

# print(f"""
# TEST 1: {test1}
# TEST 2: {test2}
# TEST 3: {test3}
# """)
