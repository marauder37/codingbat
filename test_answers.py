## generated code, don't edit, use make_answers.py to generate

from answers import *



# Logic-2

def test_make_bricks_0():
    assert make_bricks(2, 1000000, 100003) == False

def test_make_bricks_1():
    assert make_bricks(6, 0, 11) == False

def test_make_bricks_2():
    assert make_bricks(20, 4, 39) == True

def test_make_bricks_3():
    assert make_bricks(3, 1, 9) == False

def test_make_bricks_4():
    assert make_bricks(3, 1, 8) == True

def test_make_bricks_5():
    assert make_bricks(1, 1, 7) == False

def test_make_bricks_6():
    assert make_bricks(20, 0, 21) == False

def test_make_bricks_7():
    assert make_bricks(20, 4, 51) == False

def test_make_bricks_8():
    assert make_bricks(3, 1, 7) == True

def test_make_bricks_9():
    assert make_bricks(2, 1, 7) == True

def test_make_bricks_10():
    assert make_bricks(7, 1, 13) == False

def test_make_bricks_11():
    assert make_bricks(3, 2, 8) == True

def test_make_bricks_12():
    assert make_bricks(6, 1, 11) == True

def test_make_bricks_13():
    assert make_bricks(40, 1, 46) == False

def test_make_bricks_14():
    assert make_bricks(0, 3, 10) == True

def test_make_bricks_15():
    assert make_bricks(3, 2, 9) == False

def test_make_bricks_16():
    assert make_bricks(40, 2, 52) == False

def test_make_bricks_17():
    assert make_bricks(1, 4, 11) == True

def test_make_bricks_18():
    assert make_bricks(40, 2, 50) == True

def test_make_bricks_19():
    assert make_bricks(40, 2, 47) == True

def test_make_bricks_20():
    assert make_bricks(43, 1, 46) == True

def test_make_bricks_21():
    assert make_bricks(3, 2, 10) == True

def test_make_bricks_22():
    assert make_bricks(7, 1, 11) == True

def test_make_bricks_23():
    assert make_bricks(1, 4, 12) == False

def test_make_bricks_24():
    assert make_bricks(20, 0, 19) == True

def test_make_bricks_25():
    assert make_bricks(22, 2, 33) == False

def test_make_bricks_26():
    assert make_bricks(0, 2, 10) == True

def test_make_bricks_27():
    assert make_bricks(1000000, 1000, 1000100) == True

def test_make_bricks_28():
    assert make_bricks(7, 1, 8) == True

def test_lone_sum_0():
    assert lone_sum(1, 2, 3) == 6

def test_lone_sum_1():
    assert lone_sum(3, 3, 3) == 0

def test_lone_sum_2():
    assert lone_sum(2, 9, 3) == 14

def test_lone_sum_3():
    assert lone_sum(2, 9, 2) == 9

def test_lone_sum_4():
    assert lone_sum(2, 2, 9) == 9

def test_lone_sum_5():
    assert lone_sum(3, 2, 3) == 2

def test_lone_sum_6():
    assert lone_sum(9, 2, 2) == 9

def test_lone_sum_7():
    assert lone_sum(4, 2, 3) == 9

def test_lone_sum_8():
    assert lone_sum(1, 3, 1) == 3

def test_lucky_sum_0():
    assert lucky_sum(1, 13, 3) == 1

def test_lucky_sum_1():
    assert lucky_sum(1, 2, 3) == 6

def test_lucky_sum_2():
    assert lucky_sum(13, 13, 2) == 0

def test_lucky_sum_3():
    assert lucky_sum(13, 2, 13) == 0

def test_lucky_sum_4():
    assert lucky_sum(1, 2, 13) == 3

def test_lucky_sum_5():
    assert lucky_sum(6, 5, 2) == 13

def test_lucky_sum_6():
    assert lucky_sum(1, 13, 13) == 1

def test_lucky_sum_7():
    assert lucky_sum(13, 2, 3) == 0

def test_lucky_sum_8():
    assert lucky_sum(8, 13, 2) == 8

def test_lucky_sum_9():
    assert lucky_sum(7, 2, 1) == 10

def test_lucky_sum_10():
    assert lucky_sum(9, 4, 13) == 13

def test_lucky_sum_11():
    assert lucky_sum(3, 3, 13) == 6

def test_no_teen_sum_0():
    assert no_teen_sum(1, 2, 3) == 6

def test_no_teen_sum_1():
    assert no_teen_sum(17, 18, 16) == 16

def test_no_teen_sum_2():
    assert no_teen_sum(2, 1, 16) == 19

def test_no_teen_sum_3():
    assert no_teen_sum(15, 15, 19) == 30

def test_no_teen_sum_4():
    assert no_teen_sum(15, 19, 16) == 31

def test_no_teen_sum_5():
    assert no_teen_sum(17, 1, 2) == 3

def test_no_teen_sum_6():
    assert no_teen_sum(2, 15, 2) == 19

def test_no_teen_sum_7():
    assert no_teen_sum(2, 1, 17) == 3

def test_no_teen_sum_8():
    assert no_teen_sum(17, 19, 18) == 0

def test_no_teen_sum_9():
    assert no_teen_sum(2, 13, 1) == 3

def test_no_teen_sum_10():
    assert no_teen_sum(2, 1, 14) == 3

def test_no_teen_sum_11():
    assert no_teen_sum(5, 17, 18) == 5

def test_no_teen_sum_12():
    assert no_teen_sum(15, 16, 1) == 32

def test_no_teen_sum_13():
    assert no_teen_sum(16, 17, 18) == 16

def test_no_teen_sum_14():
    assert no_teen_sum(17, 18, 19) == 0

def test_no_teen_sum_15():
    assert no_teen_sum(2, 1, 15) == 18

def test_round_sum_0():
    assert round_sum(24, 36, 32) == 90

def test_round_sum_1():
    assert round_sum(11, 24, 36) == 70

def test_round_sum_2():
    assert round_sum(23, 11, 26) == 60

def test_round_sum_3():
    assert round_sum(0, 9, 0) == 10

def test_round_sum_4():
    assert round_sum(4, 4, 6) == 10

def test_round_sum_5():
    assert round_sum(20, 30, 40) == 90

def test_round_sum_6():
    assert round_sum(10, 10, 19) == 40

def test_round_sum_7():
    assert round_sum(12, 10, 24) == 40

def test_round_sum_8():
    assert round_sum(45, 21, 30) == 100

def test_round_sum_9():
    assert round_sum(23, 24, 29) == 70

def test_round_sum_10():
    assert round_sum(4, 6, 5) == 20

def test_round_sum_11():
    assert round_sum(6, 4, 4) == 10

def test_round_sum_12():
    assert round_sum(14, 12, 26) == 50

def test_round_sum_13():
    assert round_sum(12, 13, 14) == 30

def test_round_sum_14():
    assert round_sum(25, 24, 25) == 80

def test_round_sum_15():
    assert round_sum(0, 0, 1) == 0

def test_round_sum_16():
    assert round_sum(23, 24, 25) == 70

def test_round_sum_17():
    assert round_sum(16, 17, 18) == 60

def test_round_sum_18():
    assert round_sum(9, 4, 4) == 10

def test_close_far_0():
    assert close_far(4, 1, 3) == True

def test_close_far_1():
    assert close_far(0, -1, 10) == True

def test_close_far_2():
    assert close_far(8, 9, 7) == False

def test_close_far_3():
    assert close_far(10, 10, 8) == True

def test_close_far_4():
    assert close_far(10, 8, 9) == False

def test_close_far_5():
    assert close_far(-1, 10, 0) == True

def test_close_far_6():
    assert close_far(4, 5, 3) == False

def test_close_far_7():
    assert close_far(4, 3, 5) == False

def test_close_far_8():
    assert close_far(1, 2, 10) == True

def test_close_far_9():
    assert close_far(1, 2, 3) == False

def test_close_far_10():
    assert close_far(8, 9, 10) == False

def test_close_far_11():
    assert close_far(8, 6, 9) == True

def test_make_chocolate_0():
    assert make_chocolate(9, 3, 18) == 3

def test_make_chocolate_1():
    assert make_chocolate(4, 1, 10) == -1

def test_make_chocolate_2():
    assert make_chocolate(6, 2, 7) == 2

def test_make_chocolate_3():
    assert make_chocolate(7, 1, 12) == 7

def test_make_chocolate_4():
    assert make_chocolate(1, 2, 7) == -1

def test_make_chocolate_5():
    assert make_chocolate(4, 1, 9) == 4

def test_make_chocolate_6():
    assert make_chocolate(5, 4, 9) == 4

def test_make_chocolate_7():
    assert make_chocolate(1, 2, 6) == 1

def test_make_chocolate_8():
    assert make_chocolate(6, 1, 12) == -1

def test_make_chocolate_9():
    assert make_chocolate(6, 2, 11) == 1

def test_make_chocolate_10():
    assert make_chocolate(7, 2, 13) == 3

def test_make_chocolate_11():
    assert make_chocolate(6, 1, 13) == -1

def test_make_chocolate_12():
    assert make_chocolate(60, 100, 550) == 50

def test_make_chocolate_13():
    assert make_chocolate(6, 2, 10) == 0

def test_make_chocolate_14():
    assert make_chocolate(4, 1, 4) == 4

def test_make_chocolate_15():
    assert make_chocolate(6, 1, 11) == 6

def test_make_chocolate_16():
    assert make_chocolate(4, 1, 7) == 2

def test_make_chocolate_17():
    assert make_chocolate(1000, 1000000, 5000006) == 6

def test_make_chocolate_18():
    assert make_chocolate(7, 1, 13) == -1

def test_make_chocolate_19():
    assert make_chocolate(6, 1, 10) == 5

def test_make_chocolate_20():
    assert make_chocolate(6, 2, 12) == 2

def test_make_chocolate_21():
    assert make_chocolate(1, 2, 5) == 0

def test_make_chocolate_22():
    assert make_chocolate(3, 1, 9) == -1

def test_make_chocolate_23():
    assert make_chocolate(4, 1, 5) == 0



# Logic-1

def test_cigar_party_0():
    assert cigar_party(30, False) == False

def test_cigar_party_1():
    assert cigar_party(30, True) == False

def test_cigar_party_2():
    assert cigar_party(61, False) == False

def test_cigar_party_3():
    assert cigar_party(50, False) == True

def test_cigar_party_4():
    assert cigar_party(39, True) == False

def test_cigar_party_5():
    assert cigar_party(40, True) == True

def test_cigar_party_6():
    assert cigar_party(40, False) == True

def test_cigar_party_7():
    assert cigar_party(70, True) == True

def test_cigar_party_8():
    assert cigar_party(50, True) == True

def test_cigar_party_9():
    assert cigar_party(60, False) == True

def test_cigar_party_10():
    assert cigar_party(39, False) == False

def test_date_fashion_0():
    assert date_fashion(9, 9) == 2

def test_date_fashion_1():
    assert date_fashion(5, 2) == 0

def test_date_fashion_2():
    assert date_fashion(2, 2) == 0

def test_date_fashion_3():
    assert date_fashion(2, 9) == 0

def test_date_fashion_4():
    assert date_fashion(5, 5) == 1

def test_date_fashion_5():
    assert date_fashion(6, 2) == 0

def test_date_fashion_6():
    assert date_fashion(2, 7) == 0

def test_date_fashion_7():
    assert date_fashion(3, 3) == 1

def test_date_fashion_8():
    assert date_fashion(3, 7) == 1

def test_date_fashion_9():
    assert date_fashion(5, 10) == 2

def test_date_fashion_10():
    assert date_fashion(10, 5) == 2

def test_date_fashion_11():
    assert date_fashion(10, 2) == 0

def test_squirrel_play_0():
    assert squirrel_play(90, True) == True

def test_squirrel_play_1():
    assert squirrel_play(100, False) == False

def test_squirrel_play_2():
    assert squirrel_play(90, False) == True

def test_squirrel_play_3():
    assert squirrel_play(95, False) == False

def test_squirrel_play_4():
    assert squirrel_play(50, True) == False

def test_squirrel_play_5():
    assert squirrel_play(50, False) == False

def test_squirrel_play_6():
    assert squirrel_play(100, True) == True

def test_squirrel_play_7():
    assert squirrel_play(95, True) == True

def test_squirrel_play_8():
    assert squirrel_play(70, False) == True

def test_squirrel_play_9():
    assert squirrel_play(60, False) == True

def test_squirrel_play_10():
    assert squirrel_play(105, True) == False

def test_squirrel_play_11():
    assert squirrel_play(59, True) == False

def test_squirrel_play_12():
    assert squirrel_play(59, False) == False

def test_caught_speeding_0():
    assert caught_speeding(70, False) == 1

def test_caught_speeding_1():
    assert caught_speeding(65, True) == 0

def test_caught_speeding_2():
    assert caught_speeding(85, True) == 1

def test_caught_speeding_3():
    assert caught_speeding(60, False) == 0

def test_caught_speeding_4():
    assert caught_speeding(85, False) == 2

def test_caught_speeding_5():
    assert caught_speeding(90, False) == 2

def test_caught_speeding_6():
    assert caught_speeding(40, True) == 0

def test_caught_speeding_7():
    assert caught_speeding(75, True) == 1

def test_caught_speeding_8():
    assert caught_speeding(40, False) == 0

def test_caught_speeding_9():
    assert caught_speeding(75, False) == 1

def test_caught_speeding_10():
    assert caught_speeding(65, False) == 1

def test_caught_speeding_11():
    assert caught_speeding(80, False) == 1

def test_sorta_sum_0():
    assert sorta_sum(-3, 12) == 9

def test_sorta_sum_1():
    assert sorta_sum(14, 6) == 20

def test_sorta_sum_2():
    assert sorta_sum(3, 4) == 7

def test_sorta_sum_3():
    assert sorta_sum(4, 5) == 9

def test_sorta_sum_4():
    assert sorta_sum(4, 6) == 20

def test_sorta_sum_5():
    assert sorta_sum(9, 4) == 20

def test_sorta_sum_6():
    assert sorta_sum(14, 7) == 21

def test_sorta_sum_7():
    assert sorta_sum(12, -3) == 9

def test_sorta_sum_8():
    assert sorta_sum(10, 11) == 21

def test_alarm_clock_0():
    assert alarm_clock(1, True) == '10:00'

def test_alarm_clock_1():
    assert alarm_clock(6, False) == '10:00'

def test_alarm_clock_2():
    assert alarm_clock(6, True) == 'off'

def test_alarm_clock_3():
    assert alarm_clock(0, True) == 'off'

def test_alarm_clock_4():
    assert alarm_clock(3, True) == '10:00'

def test_alarm_clock_5():
    assert alarm_clock(1, False) == '7:00'

def test_alarm_clock_6():
    assert alarm_clock(5, False) == '7:00'

def test_alarm_clock_7():
    assert alarm_clock(5, True) == '10:00'

def test_alarm_clock_8():
    assert alarm_clock(0, False) == '10:00'

def test_love6_0():
    assert love6(1, 7) == True

def test_love6_1():
    assert love6(1, 5) == True

def test_love6_2():
    assert love6(4, 5) == False

def test_love6_3():
    assert love6(-4, -10) == True

def test_love6_4():
    assert love6(8, 3) == False

def test_love6_5():
    assert love6(7, 1) == True

def test_love6_6():
    assert love6(-7, 1) == False

def test_love6_7():
    assert love6(7, 5) == False

def test_love6_8():
    assert love6(1, 6) == True

def test_love6_9():
    assert love6(-2, -4) == False

def test_love6_10():
    assert love6(6, 4) == True

def test_love6_11():
    assert love6(8, 2) == True

def test_love6_12():
    assert love6(7, -1) == True

def test_love6_13():
    assert love6(-6, 12) == True

def test_love6_14():
    assert love6(3, 4) == False

def test_love6_15():
    assert love6(1, 8) == False

def test_love6_16():
    assert love6(-6, 2) == False

def test_love6_17():
    assert love6(6, 6) == True

def test_love6_18():
    assert love6(0, 9) == False

def test_love6_19():
    assert love6(3, 3) == True

def test_in1to10_0():
    assert in1to10(0, False) == False

def test_in1to10_1():
    assert in1to10(1, False) == True

def test_in1to10_2():
    assert in1to10(10, True) == True

def test_in1to10_3():
    assert in1to10(11, True) == True

def test_in1to10_4():
    assert in1to10(9, True) == False

def test_in1to10_5():
    assert in1to10(0, True) == True

def test_in1to10_6():
    assert in1to10(1, True) == True

def test_in1to10_7():
    assert in1to10(5, False) == True

def test_in1to10_8():
    assert in1to10(-1, False) == False

def test_in1to10_9():
    assert in1to10(9, False) == True

def test_in1to10_10():
    assert in1to10(10, False) == True

def test_in1to10_11():
    assert in1to10(11, False) == False

def test_near_ten_0():
    assert near_ten(21) == True

def test_near_ten_1():
    assert near_ten(1) == True

def test_near_ten_2():
    assert near_ten(158) == True

def test_near_ten_3():
    assert near_ten(11) == True

def test_near_ten_4():
    assert near_ten(6) == False

def test_near_ten_5():
    assert near_ten(17) == False

def test_near_ten_6():
    assert near_ten(22) == True

def test_near_ten_7():
    assert near_ten(23) == False

def test_near_ten_8():
    assert near_ten(19) == True

def test_near_ten_9():
    assert near_ten(12) == True

def test_near_ten_10():
    assert near_ten(155) == False

def test_near_ten_11():
    assert near_ten(3) == False

def test_near_ten_12():
    assert near_ten(10) == True

def test_near_ten_13():
    assert near_ten(31) == True

def test_near_ten_14():
    assert near_ten(54) == False



# List-1

def test_first_last6_0():
    assert first_last6([3, 6]) == True

def test_first_last6_1():
    assert first_last6([3, 2, 1]) == False

def test_first_last6_2():
    assert first_last6([1, 2, 3, 4]) == False

def test_first_last6_3():
    assert first_last6([5, 6]) == True

def test_first_last6_4():
    assert first_last6([3, 6, 1]) == False

def test_first_last6_5():
    assert first_last6([5, 5]) == False

def test_first_last6_6():
    assert first_last6([6]) == True

def test_first_last6_7():
    assert first_last6([13, 6, 1, 2, 3]) == False

def test_first_last6_8():
    assert first_last6([6, 1, 2, 3]) == True

def test_first_last6_9():
    assert first_last6([1, 2, 3, 4, 6]) == True

def test_first_last6_10():
    assert first_last6([1, 2, 6]) == True

def test_first_last6_11():
    assert first_last6([13, 6, 1, 2, 6]) == True

def test_first_last6_12():
    assert first_last6([3]) == False

def test_same_first_last_0():
    assert same_first_last([]) == False

def test_same_first_last_1():
    assert same_first_last([1, 2, 3]) == False

def test_same_first_last_2():
    assert same_first_last([7]) == True

def test_same_first_last_3():
    assert same_first_last([1, 2, 3, 4, 5, 1]) == True

def test_same_first_last_4():
    assert same_first_last([1, 2, 3, 1]) == True

def test_same_first_last_5():
    assert same_first_last([13, 2, 3, 4, 5, 13]) == True

def test_same_first_last_6():
    assert same_first_last([1, 2, 1]) == True

def test_same_first_last_7():
    assert same_first_last([7, 7]) == True

def test_same_first_last_8():
    assert same_first_last([1, 2, 3, 4, 5, 13]) == False

def test_make_pi_0():
    assert make_pi() == [3, 1, 4]

def test_common_end_0():
    assert common_end([1, 2, 3], [7, 3]) == True

def test_common_end_1():
    assert common_end([1, 2, 3], [1]) == True

def test_common_end_2():
    assert common_end([1, 2, 3], [1, 3]) == True

def test_common_end_3():
    assert common_end([1, 2, 3], [2]) == False

def test_common_end_4():
    assert common_end([1, 2, 3], [7, 3, 2]) == False

def test_sum3_0():
    assert sum3([5, 11, 2]) == 18

def test_sum3_1():
    assert sum3([1, 2, 1]) == 4

def test_sum3_2():
    assert sum3([1, 2, 3]) == 6

def test_sum3_3():
    assert sum3([1, 1, 1]) == 3

def test_sum3_4():
    assert sum3([7, 0, 0]) == 7

def test_sum3_5():
    assert sum3([2, 7, 2]) == 11

def test_rotate_left3_0():
    assert rotate_left3([1, 2, 1]) == [2, 1, 1]

def test_rotate_left3_1():
    assert rotate_left3([7, 0, 0]) == [0, 0, 7]

def test_rotate_left3_2():
    assert rotate_left3([1, 2, 3]) == [2, 3, 1]

def test_rotate_left3_3():
    assert rotate_left3([0, 0, 1]) == [0, 1, 0]

def test_rotate_left3_4():
    assert rotate_left3([5, 11, 9]) == [11, 9, 5]

def test_reverse3_0():
    assert reverse3([7, 2, 3]) == [3, 2, 7]

def test_reverse3_1():
    assert reverse3([5, 11, 9]) == [9, 11, 5]

def test_reverse3_2():
    assert reverse3([7, 0, 0]) == [0, 0, 7]

def test_reverse3_3():
    assert reverse3([1, 2, 3]) == [3, 2, 1]

def test_reverse3_4():
    assert reverse3([0, 6, 5]) == [5, 6, 0]

def test_reverse3_5():
    assert reverse3([2, 1, 2]) == [2, 1, 2]

def test_reverse3_6():
    assert reverse3([2, 11, 3]) == [3, 11, 2]

def test_reverse3_7():
    assert reverse3([1, 2, 1]) == [1, 2, 1]

def test_max_end3_0():
    assert max_end3([11, 3, 3]) == [11, 11, 11]

def test_max_end3_1():
    assert max_end3([2, 11, 3]) == [3, 3, 3]

def test_max_end3_2():
    assert max_end3([0, 0, 1]) == [1, 1, 1]

def test_max_end3_3():
    assert max_end3([1, 2, 3]) == [3, 3, 3]

def test_max_end3_4():
    assert max_end3([3, 11, 11]) == [11, 11, 11]

def test_max_end3_5():
    assert max_end3([11, 5, 9]) == [11, 11, 11]

def test_max_end3_6():
    assert max_end3([2, 11, 2]) == [2, 2, 2]

def test_max_end3_7():
    assert max_end3([2, 2, 2]) == [2, 2, 2]

def test_sum2_0():
    assert sum2([4, 5, 6]) == 9

def test_sum2_1():
    assert sum2([1, 2]) == 3

def test_sum2_2():
    assert sum2([]) == 0

def test_sum2_3():
    assert sum2([1]) == 1

def test_sum2_4():
    assert sum2([4]) == 4

def test_sum2_5():
    assert sum2([1, 1]) == 2

def test_sum2_6():
    assert sum2([1, 2, 3]) == 3

def test_sum2_7():
    assert sum2([1, 1, 1, 1]) == 2

def test_middle_way_0():
    assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]

def test_middle_way_1():
    assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]

def test_middle_way_2():
    assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]

def test_middle_way_3():
    assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]

def test_middle_way_4():
    assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]

def test_middle_way_5():
    assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]

def test_make_ends_0():
    assert make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3]

def test_make_ends_1():
    assert make_ends([7, 4, 6, 2]) == [7, 2]

def test_make_ends_2():
    assert make_ends([1, 2, 3, 4]) == [1, 4]

def test_make_ends_3():
    assert make_ends([5, 2, 9]) == [5, 9]

def test_make_ends_4():
    assert make_ends([1, 2, 3]) == [1, 3]

def test_make_ends_5():
    assert make_ends([7, 4]) == [7, 4]

def test_make_ends_6():
    assert make_ends([7]) == [7, 7]

def test_make_ends_7():
    assert make_ends([2, 3, 4, 1]) == [2, 1]

def test_has23_0():
    assert has23([9, 5]) == False

def test_has23_1():
    assert has23([2, 2]) == True

def test_has23_2():
    assert has23([3, 3]) == True

def test_has23_3():
    assert has23([3, 9]) == True

def test_has23_4():
    assert has23([2, 5]) == True

def test_has23_5():
    assert has23([4, 3]) == True

def test_has23_6():
    assert has23([7, 7]) == False

def test_has23_7():
    assert has23([3, 2]) == True

def test_has23_8():
    assert has23([4, 5]) == False



# List-2

def test_count_evens_0():
    assert count_evens([1, 3, 5]) == 0

def test_count_evens_1():
    assert count_evens([2, 2, 0]) == 3

def test_count_evens_2():
    assert count_evens([2, 11, 9, 0]) == 2

def test_count_evens_3():
    assert count_evens([2, 1, 2, 3, 4]) == 3

def test_count_evens_4():
    assert count_evens([]) == 0

def test_count_evens_5():
    assert count_evens([2, 5, 12]) == 2

def test_count_evens_6():
    assert count_evens([2]) == 1

def test_count_evens_7():
    assert count_evens([11, 9, 0, 1]) == 1

def test_big_diff_0():
    assert big_diff([10, 2]) == 8

def test_big_diff_1():
    assert big_diff([5, 1, 6, 1, 9, 9]) == 8

def test_big_diff_2():
    assert big_diff([2, 2]) == 0

def test_big_diff_3():
    assert big_diff([10, 3, 5, 6]) == 7

def test_big_diff_4():
    assert big_diff([7, 2, 10, 9]) == 8

def test_big_diff_5():
    assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3

def test_big_diff_6():
    assert big_diff([2]) == 0

def test_big_diff_7():
    assert big_diff([10, 0]) == 10

def test_big_diff_8():
    assert big_diff([2, 3]) == 1

def test_big_diff_9():
    assert big_diff([7, 6, 8, 5]) == 3

def test_big_diff_10():
    assert big_diff([2, 10, 7, 2]) == 8

def test_big_diff_11():
    assert big_diff([2, 10]) == 8

def test_centered_average_0():
    assert centered_average([0, 2, 3, 4, 100]) == 3

def test_centered_average_1():
    assert centered_average([1000, 0, 1, 99]) == 50

def test_centered_average_2():
    assert centered_average([4, 0, 100]) == 4

def test_centered_average_3():
    assert centered_average([1, 1, 99, 99]) == 50

def test_centered_average_4():
    assert centered_average([1, 2, 3, 4, 100]) == 3

def test_centered_average_5():
    assert centered_average([4, 4, 4, 1, 5]) == 4

def test_centered_average_6():
    assert centered_average([100, 0, 5, 3, 4]) == 4

def test_centered_average_7():
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3

def test_centered_average_8():
    assert centered_average([4, 4, 4, 4, 5]) == 4

def test_centered_average_9():
    assert centered_average([1, 1, 100]) == 1

def test_centered_average_10():
    assert centered_average([7, 7, 7]) == 7

def test_centered_average_11():
    assert centered_average([5, 3, 4, 0, 100]) == 4

def test_centered_average_12():
    assert centered_average([5, 3, 4, 6, 2]) == 4

def test_centered_average_13():
    assert centered_average([6, 4, 8, 12, 3]) == 6

def test_centered_average_14():
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5

def test_centered_average_15():
    assert centered_average([1, 7, 8]) == 7

def test_sum13_0():
    assert sum13([1, 2, 2, 1, 13]) == 6

def test_sum13_1():
    assert sum13([5, 7, 2]) == 14

def test_sum13_2():
    assert sum13([1, 1]) == 2

def test_sum13_3():
    assert sum13([13, 13]) == 0

def test_sum13_4():
    assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3

def test_sum13_5():
    assert sum13([1, 2, 2, 1]) == 6

def test_sum13_6():
    assert sum13([]) == 0

def test_sum13_7():
    assert sum13([13, 0]) == 0

def test_sum13_8():
    assert sum13([5, 13, 2]) == 5

def test_sum13_9():
    assert sum13([1, 2, 13, 2, 1, 13]) == 4

def test_sum13_10():
    assert sum13([0]) == 0

def test_sum13_11():
    assert sum13([13, 1, 13]) == 0

def test_sum13_12():
    assert sum13([13, 0, 13]) == 0

def test_sum13_13():
    assert sum13([13]) == 0

def test_sum67_0():
    assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5

def test_sum67_1():
    assert sum67([6, 7, 11]) == 11

def test_sum67_2():
    assert sum67([1, 6, 7, 7]) == 8

def test_sum67_3():
    assert sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2

def test_sum67_4():
    assert sum67([]) == 0

def test_sum67_5():
    assert sum67([6, 7, 1, 6, 7, 7]) == 8

def test_sum67_6():
    assert sum67([2, 2, 6, 7, 7]) == 11

def test_sum67_7():
    assert sum67([1, 2, 2]) == 5

def test_sum67_8():
    assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2

def test_sum67_9():
    assert sum67([1, 1, 6, 7, 2]) == 4

def test_sum67_10():
    assert sum67([2, 7, 6, 2, 6, 7, 2, 7]) == 18

def test_sum67_11():
    assert sum67([2, 7, 6, 2, 6, 2, 7]) == 9

def test_sum67_12():
    assert sum67([6, 8, 1, 6, 7]) == 0

def test_sum67_13():
    assert sum67([11, 6, 7, 11]) == 22

def test_has22_0():
    assert has22([1, 2, 2]) == True

def test_has22_1():
    assert has22([1, 2, 1, 2]) == False

def test_has22_2():
    assert has22([1, 2]) == False

def test_has22_3():
    assert has22([2, 1, 2]) == False

def test_has22_4():
    assert has22([2]) == False

def test_has22_5():
    assert has22([3, 3, 2, 2]) == True

def test_has22_6():
    assert has22([]) == False

def test_has22_7():
    assert has22([4, 2, 4, 2, 2, 5]) == True

def test_has22_8():
    assert has22([1, 3, 2, 2]) == True

def test_has22_9():
    assert has22([2, 2, 1, 2]) == True

def test_has22_10():
    assert has22([2, 3, 2, 2]) == True

def test_has22_11():
    assert has22([5, 2, 5, 2]) == False

def test_has22_12():
    assert has22([1, 3, 2]) == False

def test_has22_13():
    assert has22([2, 2]) == True



# String-1

def test_hello_name_0():
    assert hello_name('Omega') == 'Hello Omega!'

def test_hello_name_1():
    assert hello_name('X') == 'Hello X!'

def test_hello_name_2():
    assert hello_name('Alpha') == 'Hello Alpha!'

def test_hello_name_3():
    assert hello_name('Goodbye') == 'Hello Goodbye!'

def test_hello_name_4():
    assert hello_name('Bob') == 'Hello Bob!'

def test_hello_name_5():
    assert hello_name('Alice') == 'Hello Alice!'

def test_hello_name_6():
    assert hello_name('Hello') == 'Hello Hello!'

def test_hello_name_7():
    assert hello_name('xyz!') == 'Hello xyz!!'

def test_hello_name_8():
    assert hello_name('Dolly') == 'Hello Dolly!'

def test_hello_name_9():
    assert hello_name('ho ho ho') == 'Hello ho ho ho!'

def test_make_abba_0():
    assert make_abba('Bo', 'Ya') == 'BoYaYaBo'

def test_make_abba_1():
    assert make_abba('x', 'y') == 'xyyx'

def test_make_abba_2():
    assert make_abba('Ya', 'Ya') == 'YaYaYaYa'

def test_make_abba_3():
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'

def test_make_abba_4():
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi'

def test_make_abba_5():
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'

def test_make_abba_6():
    assert make_abba('', 'y') == 'yy'

def test_make_abba_7():
    assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'

def test_make_abba_8():
    assert make_abba('x', '') == 'xx'

def test_make_tags_0():
    assert make_tags('body', 'Heart') == '<body>Heart</body>'

def test_make_tags_1():
    assert make_tags('address', 'here') == '<address>here</address>'

def test_make_tags_2():
    assert make_tags('i', '') == '<i></i>'

def test_make_tags_3():
    assert make_tags('i', 'Hello') == '<i>Hello</i>'

def test_make_tags_4():
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'

def test_make_tags_5():
    assert make_tags('i', 'Yay') == '<i>Yay</i>'

def test_make_tags_6():
    assert make_tags('i', 'i') == '<i>i</i>'

def test_make_out_word_0():
    assert make_out_word('<<>>', 'Yay') == '<<Yay>>'

def test_make_out_word_1():
    assert make_out_word('[[]]', 'word') == '[[word]]'

def test_make_out_word_2():
    assert make_out_word('abyz', 'YAY') == 'abYAYyz'

def test_make_out_word_3():
    assert make_out_word('HHoo', 'Hello') == 'HHHellooo'

def test_make_out_word_4():
    assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'

def test_extra_end_0():
    assert extra_end('Hi') == 'HiHiHi'

def test_extra_end_1():
    assert extra_end('Hello') == 'lololo'

def test_extra_end_2():
    assert extra_end('Candy') == 'dydydy'

def test_extra_end_3():
    assert extra_end('Code') == 'dedede'

def test_extra_end_4():
    assert extra_end('ab') == 'ababab'

def test_first_two_0():
    assert first_two('ab') == 'ab'

def test_first_two_1():
    assert first_two('a') == 'a'

def test_first_two_2():
    assert first_two('') == ''

def test_first_two_3():
    assert first_two('hi') == 'hi'

def test_first_two_4():
    assert first_two('Hello') == 'He'

def test_first_two_5():
    assert first_two('abcdefg') == 'ab'

def test_first_two_6():
    assert first_two('hiya') == 'hi'

def test_first_two_7():
    assert first_two('Kitten') == 'Ki'

def test_first_half_0():
    assert first_half('WooHoo') == 'Woo'

def test_first_half_1():
    assert first_half('HelloThere') == 'Hello'

def test_first_half_2():
    assert first_half('kitten') == 'kit'

def test_first_half_3():
    assert first_half('ab') == 'a'

def test_first_half_4():
    assert first_half('') == ''

def test_first_half_5():
    assert first_half('0123456789') == '01234'

def test_first_half_6():
    assert first_half('abcdef') == 'abc'

def test_without_end_0():
    assert without_end('kitten') == 'itte'

def test_without_end_1():
    assert without_end('ab') == ''

def test_without_end_2():
    assert without_end('java') == 'av'

def test_without_end_3():
    assert without_end('coding') == 'odin'

def test_without_end_4():
    assert without_end('Chocolate!') == 'hocolate'

def test_without_end_5():
    assert without_end('code') == 'od'

def test_without_end_6():
    assert without_end('woohoo') == 'ooho'

def test_without_end_7():
    assert without_end('Hello') == 'ell'

def test_combo_string_0():
    assert combo_string('xyz', 'ab') == 'abxyzab'

def test_combo_string_1():
    assert combo_string('a', 'bb') == 'abba'

def test_combo_string_2():
    assert combo_string('bb', 'a') == 'abba'

def test_combo_string_3():
    assert combo_string('aaa', 'b') == 'baaab'

def test_combo_string_4():
    assert combo_string('hi', 'Hello') == 'hiHellohi'

def test_combo_string_5():
    assert combo_string('', 'bb') == 'bb'

def test_combo_string_6():
    assert combo_string('Hello', 'hi') == 'hiHellohi'

def test_combo_string_7():
    assert combo_string('aaa', '1234') == 'aaa1234aaa'

def test_combo_string_8():
    assert combo_string('aaa', '') == 'aaa'

def test_combo_string_9():
    assert combo_string('aaa', 'bb') == 'bbaaabb'

def test_combo_string_10():
    assert combo_string('b', 'aaa') == 'baaab'

def test_non_start_0():
    assert non_start('ab', 'x') == 'b'

def test_non_start_1():
    assert non_start('Hello', 'There') == 'ellohere'

def test_non_start_2():
    assert non_start('shotl', 'java') == 'hotlava'

def test_non_start_3():
    assert non_start('ab', 'xy') == 'by'

def test_non_start_4():
    assert non_start('x', 'ac') == 'c'

def test_non_start_5():
    assert non_start('kit', 'kat') == 'itat'

def test_non_start_6():
    assert non_start('java', 'code') == 'avaode'

def test_non_start_7():
    assert non_start('mart', 'dart') == 'artart'

def test_non_start_8():
    assert non_start('a', 'x') == ''

def test_left2_0():
    assert left2('Chocolate') == 'ocolateCh'

def test_left2_1():
    assert left2('java') == 'vaja'

def test_left2_2():
    assert left2('code') == 'deco'

def test_left2_3():
    assert left2('12345') == '34512'

def test_left2_4():
    assert left2('Hello') == 'lloHe'

def test_left2_5():
    assert left2('cat') == 'tca'

def test_left2_6():
    assert left2('Hi') == 'Hi'

def test_left2_7():
    assert left2('bricks') == 'icksbr'



# String-2

def test_double_char_0():
    assert double_char('.') == '..'

def test_double_char_1():
    assert double_char('Word!') == 'WWoorrdd!!'

def test_double_char_2():
    assert double_char('The') == 'TThhee'

def test_double_char_3():
    assert double_char('aa') == 'aaaa'

def test_double_char_4():
    assert double_char('a') == 'aa'

def test_double_char_5():
    assert double_char('') == ''

def test_double_char_6():
    assert double_char('AAbb') == 'AAAAbbbb'

def test_double_char_7():
    assert double_char('!!') == '!!!!'

def test_double_char_8():
    assert double_char('Hi-There') == 'HHii--TThheerree'

def test_count_hi_0():
    assert count_hi('hiho not HOHIhi') == 2

def test_count_hi_1():
    assert count_hi('h') == 0

def test_count_hi_2():
    assert count_hi('hi') == 1

def test_count_hi_3():
    assert count_hi('hiHIhi') == 2

def test_count_hi_4():
    assert count_hi('ABChi hi') == 2

def test_count_hi_5():
    assert count_hi('abc hi ho') == 1

def test_count_hi_6():
    assert count_hi('') == 0

def test_count_hi_7():
    assert count_hi('hihi') == 2

def test_count_hi_8():
    assert count_hi('Hi is no HI on ahI') == 0

def test_cat_dog_0():
    assert cat_dog('catdog') == True

def test_cat_dog_1():
    assert cat_dog('catxdogxdogxcat') == True

def test_cat_dog_2():
    assert cat_dog('dog') == False

def test_cat_dog_3():
    assert cat_dog('1cat1cadodog') == True

def test_cat_dog_4():
    assert cat_dog('catxxdogxxxdog') == False

def test_cat_dog_5():
    assert cat_dog('ca') == True

def test_cat_dog_6():
    assert cat_dog('c') == True

def test_cat_dog_7():
    assert cat_dog('catcat') == False

def test_cat_dog_8():
    assert cat_dog('catxdogxdogxca') == False

def test_cat_dog_9():
    assert cat_dog('dogdogcat') == False

def test_cat_dog_10():
    assert cat_dog('dogogcat') == True

def test_cat_dog_11():
    assert cat_dog('') == True

def test_cat_dog_12():
    assert cat_dog('cat') == False

def test_count_code_0():
    assert count_code('coAcodeBcoleccoreDD') == 3

def test_count_code_1():
    assert count_code('abcxyz') == 0

def test_count_code_2():
    assert count_code('cozcop') == 0

def test_count_code_3():
    assert count_code('code') == 1

def test_count_code_4():
    assert count_code('cozfxxcope') == 1

def test_count_code_5():
    assert count_code('AAcodeBBcoleCCccoreDD') == 3

def test_count_code_6():
    assert count_code('c') == 0

def test_count_code_7():
    assert count_code('codexxcode') == 2

def test_count_code_8():
    assert count_code('aaacodebbb') == 1

def test_count_code_9():
    assert count_code('ode') == 0

def test_count_code_10():
    assert count_code('cozexxcope') == 2

def test_count_code_11():
    assert count_code('') == 0

def test_count_code_12():
    assert count_code('xxcozeyycop') == 1

def test_count_code_13():
    assert count_code('AAcodeBBcoleCCccorfDD') == 2

def test_end_other_0():
    assert end_other('abc', 'abXabc') == True

def test_end_other_1():
    assert end_other('yz', '12xz') == False

def test_end_other_2():
    assert end_other('xyz', '12xyz') == True

def test_end_other_3():
    assert end_other('Hiabcx', 'bc') == False

def test_end_other_4():
    assert end_other('ab', 'ab12') == False

def test_end_other_5():
    assert end_other('Hiabc', 'abc') == True

def test_end_other_6():
    assert end_other('abc', 'abc') == True

def test_end_other_7():
    assert end_other('AbC', 'HiaBc') == True

def test_end_other_8():
    assert end_other('12', '12') == True

def test_end_other_9():
    assert end_other('Hiabc', 'bc') == True

def test_end_other_10():
    assert end_other('Z', '12xz') == True

def test_end_other_11():
    assert end_other('ab', '12ab') == True

def test_end_other_12():
    assert end_other('Hiabc', 'abcd') == False

def test_end_other_13():
    assert end_other('abcXYZ', 'abcDEF') == False

def test_xyz_there_0():
    assert xyz_there('abc.xxyz') == True

def test_xyz_there_1():
    assert xyz_there('12.xyz') == False

def test_xyz_there_2():
    assert xyz_there('abcxy') == False

def test_xyz_there_3():
    assert xyz_there('.xyz') == False

def test_xyz_there_4():
    assert xyz_there('xyz.abc') == True

def test_xyz_there_5():
    assert xyz_there('') == False

def test_xyz_there_6():
    assert xyz_there('xy') == False

def test_xyz_there_7():
    assert xyz_there('abc.xyzxyz') == True

def test_xyz_there_8():
    assert xyz_there('12xyz') == True

def test_xyz_there_9():
    assert xyz_there('xyz') == True

def test_xyz_there_10():
    assert xyz_there('1.xyz.xyz2.xyz') == False

def test_xyz_there_11():
    assert xyz_there('abcxyz') == True

def test_xyz_there_12():
    assert xyz_there('abc.xyz') == False

def test_xyz_there_13():
    assert xyz_there('x') == False



# Warmup-2

def test_string_times_0():
    assert string_times('Hi', 3) == 'HiHiHi'

def test_string_times_1():
    assert string_times('Hi', 1) == 'Hi'

def test_string_times_2():
    assert string_times('Hi', 2) == 'HiHi'

def test_string_times_3():
    assert string_times('', 4) == ''

def test_string_times_4():
    assert string_times('Hi', 5) == 'HiHiHiHiHi'

def test_string_times_5():
    assert string_times('Hi', 0) == ''

def test_string_times_6():
    assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'

def test_string_times_7():
    assert string_times('code', 3) == 'codecodecode'

def test_string_times_8():
    assert string_times('code', 2) == 'codecode'

def test_string_times_9():
    assert string_times('x', 4) == 'xxxx'

def test_front_times_0():
    assert front_times('Abc', 3) == 'AbcAbcAbc'

def test_front_times_1():
    assert front_times('Abc', 0) == ''

def test_front_times_2():
    assert front_times('Chocolate', 2) == 'ChoCho'

def test_front_times_3():
    assert front_times('', 4) == ''

def test_front_times_4():
    assert front_times('Chocolate', 3) == 'ChoChoCho'

def test_front_times_5():
    assert front_times('Ab', 4) == 'AbAbAbAb'

def test_front_times_6():
    assert front_times('A', 4) == 'AAAA'

def test_string_bits_0():
    assert string_bits('Heeololeo') == 'Hello'

def test_string_bits_1():
    assert string_bits('pi') == 'p'

def test_string_bits_2():
    assert string_bits('Greetings') == 'Getns'

def test_string_bits_3():
    assert string_bits('HiHiHi') == 'HHH'

def test_string_bits_4():
    assert string_bits('Hello Kitten') == 'HloKte'

def test_string_bits_5():
    assert string_bits('Hi') == 'H'

def test_string_bits_6():
    assert string_bits('') == ''

def test_string_bits_7():
    assert string_bits('Chocoate') == 'Coot'

def test_string_bits_8():
    assert string_bits('Hello') == 'Hlo'

def test_string_bits_9():
    assert string_bits('hxaxpxpxy') == 'happy'

def test_string_splosion_0():
    assert string_splosion('x') == 'x'

def test_string_splosion_1():
    assert string_splosion('fade') == 'ffafadfade'

def test_string_splosion_2():
    assert string_splosion('There') == 'TThTheTherThere'

def test_string_splosion_3():
    assert string_splosion('Bad') == 'BBaBad'

def test_string_splosion_4():
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'

def test_string_splosion_5():
    assert string_splosion('Bye') == 'BByBye'

def test_string_splosion_6():
    assert string_splosion('abc') == 'aababc'

def test_string_splosion_7():
    assert string_splosion('Good') == 'GGoGooGood'

def test_string_splosion_8():
    assert string_splosion('Code') == 'CCoCodCode'

def test_string_splosion_9():
    assert string_splosion('ab') == 'aab'

def test_last2_0():
    assert last2('h') == 0

def test_last2_1():
    assert last2('axxxaaxx') == 2

def test_last2_2():
    assert last2('13121312') == 1

def test_last2_3():
    assert last2('13121311') == 0

def test_last2_4():
    assert last2('1717171') == 2

def test_last2_5():
    assert last2('hi') == 0

def test_last2_6():
    assert last2('xxaxxaxxaxx') == 3

def test_last2_7():
    assert last2('xaxxaxaxx') == 1

def test_last2_8():
    assert last2('hixxhi') == 1

def test_last2_9():
    assert last2('') == 0

def test_last2_10():
    assert last2('xxxx') == 2

def test_last2_11():
    assert last2('11212') == 1

def test_last2_12():
    assert last2('xaxaxaxx') == 0

def test_array_count9_0():
    assert array_count9([9, 2, 4, 3, 1]) == 1

def test_array_count9_1():
    assert array_count9([1, 2, 9]) == 1

def test_array_count9_2():
    assert array_count9([1, 9, 9]) == 2

def test_array_count9_3():
    assert array_count9([1, 9, 9, 3, 9]) == 3

def test_array_count9_4():
    assert array_count9([1, 2, 3]) == 0

def test_array_count9_5():
    assert array_count9([4, 2, 4, 3, 1]) == 0

def test_array_count9_6():
    assert array_count9([]) == 0

def test_array_front9_0():
    assert array_front9([1, 2, 3, 4, 9]) == False

def test_array_front9_1():
    assert array_front9([]) == False

def test_array_front9_2():
    assert array_front9([1, 9]) == True

def test_array_front9_3():
    assert array_front9([9, 2, 3]) == True

def test_array_front9_4():
    assert array_front9([1, 2, 9, 3, 4]) == True

def test_array_front9_5():
    assert array_front9([2]) == False

def test_array_front9_6():
    assert array_front9([1, 9, 9]) == True

def test_array_front9_7():
    assert array_front9([1, 2, 3, 4, 5]) == False

def test_array_front9_8():
    assert array_front9([3, 9, 2, 3, 3]) == True

def test_array_front9_9():
    assert array_front9([9]) == True

def test_array_front9_10():
    assert array_front9([5, 5]) == False

def test_array_front9_11():
    assert array_front9([1, 2, 3]) == False

def test_array123_0():
    assert array123([1, 1, 2, 3, 1]) == True

def test_array123_1():
    assert array123([1, 1, 2, 1, 2, 1]) == False

def test_array123_2():
    assert array123([1, 2, 3]) == True

def test_array123_3():
    assert array123([]) == False

def test_array123_4():
    assert array123([1, 1, 1]) == False

def test_array123_5():
    assert array123([1, 1, 2, 1, 2, 3]) == True

def test_array123_6():
    assert array123([1, 2]) == False

def test_array123_7():
    assert array123([1, 1, 2, 4, 1]) == False

def test_array123_8():
    assert array123([1, 2, 3, 1, 2, 3]) == True

def test_array123_9():
    assert array123([1]) == False

def test_string_match_0():
    assert string_match('iaxxai', 'aaxxaaxx') == 3

def test_string_match_1():
    assert string_match('aaxxaaxx', 'iaxxai') == 3

def test_string_match_2():
    assert string_match('he', 'hello') == 1

def test_string_match_3():
    assert string_match('h', 'hello') == 0

def test_string_match_4():
    assert string_match('hello', 'he') == 1

def test_string_match_5():
    assert string_match('abc', 'abc') == 2

def test_string_match_6():
    assert string_match('abc', 'axc') == 0

def test_string_match_7():
    assert string_match('xxcaazz', 'xxbaaz') == 3

def test_string_match_8():
    assert string_match('aabbccdd', 'abbbxxd') == 1

def test_string_match_9():
    assert string_match('', 'hello') == 0



# Warmup-1

def test_sleep_in_0():
    assert sleep_in(False, True) == True

def test_sleep_in_1():
    assert sleep_in(True, False) == False

def test_sleep_in_2():
    assert sleep_in(False, False) == True

def test_sleep_in_3():
    assert sleep_in(True, True) == True

def test_monkey_trouble_0():
    assert monkey_trouble(False, True) == False

def test_monkey_trouble_1():
    assert monkey_trouble(True, False) == False

def test_monkey_trouble_2():
    assert monkey_trouble(True, True) == True

def test_monkey_trouble_3():
    assert monkey_trouble(False, False) == True

def test_sum_double_0():
    assert sum_double(0, 0) == 0

def test_sum_double_1():
    assert sum_double(-1, 0) == -1

def test_sum_double_2():
    assert sum_double(3, 2) == 5

def test_sum_double_3():
    assert sum_double(3, 3) == 12

def test_sum_double_4():
    assert sum_double(1, 2) == 3

def test_sum_double_5():
    assert sum_double(2, 2) == 8

def test_sum_double_6():
    assert sum_double(0, 1) == 1

def test_sum_double_7():
    assert sum_double(3, 4) == 7

def test_diff21_0():
    assert diff21(10) == 11

def test_diff21_1():
    assert diff21(21) == 0

def test_diff21_2():
    assert diff21(19) == 2

def test_diff21_3():
    assert diff21(2) == 19

def test_diff21_4():
    assert diff21(-1) == 22

def test_diff21_5():
    assert diff21(50) == 58

def test_diff21_6():
    assert diff21(-2) == 23

def test_diff21_7():
    assert diff21(30) == 18

def test_diff21_8():
    assert diff21(0) == 21

def test_diff21_9():
    assert diff21(25) == 8

def test_diff21_10():
    assert diff21(1) == 20

def test_diff21_11():
    assert diff21(22) == 2

def test_parrot_trouble_0():
    assert parrot_trouble(False, 23) == False

def test_parrot_trouble_1():
    assert parrot_trouble(True, 23) == True

def test_parrot_trouble_2():
    assert parrot_trouble(True, 21) == True

def test_parrot_trouble_3():
    assert parrot_trouble(False, 6) == False

def test_parrot_trouble_4():
    assert parrot_trouble(True, 7) == False

def test_parrot_trouble_5():
    assert parrot_trouble(False, 21) == False

def test_parrot_trouble_6():
    assert parrot_trouble(False, 20) == False

def test_parrot_trouble_7():
    assert parrot_trouble(False, 12) == False

def test_parrot_trouble_8():
    assert parrot_trouble(True, 20) == False

def test_parrot_trouble_9():
    assert parrot_trouble(True, 6) == True

def test_makes10_0():
    assert makes10(10, 42) == True

def test_makes10_1():
    assert makes10(9, 9) == False

def test_makes10_2():
    assert makes10(12, -2) == True

def test_makes10_3():
    assert makes10(9, 10) == True

def test_makes10_4():
    assert makes10(1, 9) == True

def test_makes10_5():
    assert makes10(10, 1) == True

def test_makes10_6():
    assert makes10(10, 10) == True

def test_makes10_7():
    assert makes10(8, 3) == False

def test_makes10_8():
    assert makes10(8, 2) == True

def test_near_hundred_0():
    assert near_hundred(111) == False

def test_near_hundred_1():
    assert near_hundred(121) == False

def test_near_hundred_2():
    assert near_hundred(211) == False

def test_near_hundred_3():
    assert near_hundred(89) == False

def test_near_hundred_4():
    assert near_hundred(5) == False

def test_near_hundred_5():
    assert near_hundred(0) == False

def test_near_hundred_6():
    assert near_hundred(-209) == False

def test_near_hundred_7():
    assert near_hundred(90) == True

def test_near_hundred_8():
    assert near_hundred(189) == False

def test_near_hundred_9():
    assert near_hundred(290) == False

def test_near_hundred_10():
    assert near_hundred(191) == True

def test_near_hundred_11():
    assert near_hundred(-101) == False

def test_near_hundred_12():
    assert near_hundred(210) == True

def test_near_hundred_13():
    assert near_hundred(-50) == False

def test_near_hundred_14():
    assert near_hundred(200) == True

def test_near_hundred_15():
    assert near_hundred(190) == True

def test_near_hundred_16():
    assert near_hundred(93) == True

def test_near_hundred_17():
    assert near_hundred(110) == True

def test_near_hundred_18():
    assert near_hundred(209) == True

def test_pos_neg_0():
    assert pos_neg(-4, 5, True) == False

def test_pos_neg_1():
    assert pos_neg(-1, -1, True) == True

def test_pos_neg_2():
    assert pos_neg(1, 1, True) == False

def test_pos_neg_3():
    assert pos_neg(1, -1, True) == False

def test_pos_neg_4():
    assert pos_neg(-5, 6, True) == False

def test_pos_neg_5():
    assert pos_neg(1, -1, False) == True

def test_pos_neg_6():
    assert pos_neg(1, 2, False) == False

def test_pos_neg_7():
    assert pos_neg(5, -5, False) == True

def test_pos_neg_8():
    assert pos_neg(-2, -1, False) == False

def test_pos_neg_9():
    assert pos_neg(-1, 1, True) == False

def test_pos_neg_10():
    assert pos_neg(-1, 1, False) == True

def test_pos_neg_11():
    assert pos_neg(-1, -1, False) == False

def test_pos_neg_12():
    assert pos_neg(-6, 6, False) == True

def test_pos_neg_13():
    assert pos_neg(-4, 5, False) == True

def test_pos_neg_14():
    assert pos_neg(-4, -5, True) == True

def test_pos_neg_15():
    assert pos_neg(1, 1, False) == False

def test_pos_neg_16():
    assert pos_neg(-4, -5, False) == False

def test_pos_neg_17():
    assert pos_neg(-5, -5, True) == True

def test_pos_neg_18():
    assert pos_neg(-5, -6, False) == False

def test_not_string_0():
    assert not_string('not bad') == 'not bad'

def test_not_string_1():
    assert not_string('no') == 'not no'

def test_not_string_2():
    assert not_string('x') == 'not x'

def test_not_string_3():
    assert not_string('is not') == 'not is not'

def test_not_string_4():
    assert not_string('bad') == 'not bad'

def test_not_string_5():
    assert not_string('candy') == 'not candy'

def test_not_string_6():
    assert not_string('not') == 'not'

def test_missing_char_0():
    assert missing_char('code', 0) == 'ode'

def test_missing_char_1():
    assert missing_char('code', 2) == 'coe'

def test_missing_char_2():
    assert missing_char('kitten', 1) == 'ktten'

def test_missing_char_3():
    assert missing_char('Hi', 0) == 'i'

def test_missing_char_4():
    assert missing_char('kitten', 0) == 'itten'

def test_missing_char_5():
    assert missing_char('kitten', 4) == 'kittn'

def test_missing_char_6():
    assert missing_char('code', 3) == 'cod'

def test_missing_char_7():
    assert missing_char('Hi', 1) == 'H'

def test_missing_char_8():
    assert missing_char('chocolate', 8) == 'chocolat'

def test_missing_char_9():
    assert missing_char('code', 1) == 'cde'

def test_front_back_0():
    assert front_back('ab') == 'ba'

def test_front_back_1():
    assert front_back('abc') == 'cba'

def test_front_back_2():
    assert front_back('a') == 'a'

def test_front_back_3():
    assert front_back('') == ''

def test_front_back_4():
    assert front_back('code') == 'eodc'

def test_front_back_5():
    assert front_back('hello') == 'oellh'

def test_front_back_6():
    assert front_back('Chocolate') == 'ehocolatC'

def test_front_back_7():
    assert front_back('aavJ') == 'Java'

def test_front3_0():
    assert front3('Chocolate') == 'ChoChoCho'

def test_front3_1():
    assert front3('a') == 'aaa'

def test_front3_2():
    assert front3('') == ''

def test_front3_3():
    assert front3('abcXYZ') == 'abcabcabc'

def test_front3_4():
    assert front3('ab') == 'ababab'

def test_front3_5():
    assert front3('Java') == 'JavJavJav'

def test_front3_6():
    assert front3('abc') == 'abcabcabc'

