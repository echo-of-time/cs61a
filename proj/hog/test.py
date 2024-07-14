import hog
always_three = hog.make_test_dice(3)
always = hog.always_roll
#
# Extra turn from swine align
s0, s1 = hog.play(always(5), always(5), goal=25, dice=always_three)