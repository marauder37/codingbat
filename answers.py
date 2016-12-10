## generated code, don't edit, use make_answers.py to generate



# Logic-2

def make_bricks(small, big, goal):
    big_used = min(goal / 5, big)
    small_needed = goal - (big_used * 5)
    return small_needed <= small

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b
    return a + b + c

def lucky_sum(a, b, c):
    sum = 0
    for n in [a, b, c]:
        if n == 13:
            return sum
        sum += n
    return sum

def no_teen_sum(a, b, c):
    return sum(fix_teen(n) for n in [a, b, c])
        
def fix_teen(n):
    if 13 <= n < 15 or 16 < n <= 19:
        return 0
    return n

def round_sum(a, b, c):
    return sum(round10(n) for n in [a, b, c])
        
def round10(n):
    rem = n % 10
    if rem >= 5:
        return n + (10 - rem)
    return n - rem

def close_far(a, b, c):
    c1 = abs(b-a) <= 1 and abs(c-a) > 1 and abs(c-b) > 1
    c2 = abs(c-a) <= 1 and abs(b-a) > 1 and abs(b-c) > 1
    return c1 or c2

def make_chocolate(small, big, goal):
    big_used = min(goal / 5, big)
    small_needed = goal - (big_used * 5)
    if small_needed <= small:
        return small_needed
    return -1



# Logic-1

def cigar_party(cigars, is_weekend):
    return 40 <= cigars <= 60 or is_weekend and 40 <= cigars

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90

def caught_speeding(speed, is_birthday):
    if speed <= 60 or is_birthday and speed <= 65:
        return 0
    if speed <= 80 or is_birthday and speed <= 85:
        return 1
    return 2

def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    return a + b

def alarm_clock(day, vacation):
    if day in [0, 6]:
        if vacation:
            return "off"
        return "10:00"
    if vacation:
        return "10:00"
    return "7:00"

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if outside_mode:
        return not 1 < n < 10
    return 1 <= n <= 10

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8



# List-1

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
    return [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + nums[:1]

def reverse3(nums):
    return nums[-1::-1]

def max_end3(nums):
    return [max(nums[0], nums[-1])] * 3

def sum2(nums):
    return sum(nums[0:2])

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums



# List-2

def count_evens(nums):
    return len([n for n in nums if not n % 2])

def big_diff(nums):
    nums.sort()
    return nums[-1] - nums[0]

def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) / len(nums[1:-1])

def sum13(nums):
    sum = 0
    skip = False
    for n in nums:
        if n == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        sum += n
    return sum

def sum67(nums):
    sum = 0
    skip = False
    for n in nums:
        if n == 6:
            skip = True
            continue
        if skip and n == 7:
            skip = False
            continue
        if skip:
            continue
        sum += n
    return sum

def has22(nums):
    return [nums[i:i+2] == [2, 2] for i in range(len(nums))].count(True) > 0



# String-1

def hello_name(name):
    return "Hello {}!".format(name)

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(str):
    return str[-2:] * 3

def first_two(str):
    return str[:2]

def first_half(str):
    return str[:len(str)/2]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    return b + a + b

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[:2]



# String-2

def double_char(str):
    return "".join([c * 2 for c in str])

def count_hi(str):
    return str.count("hi")

def cat_dog(str):
    return str.count("cat") == str.count("dog")

def count_code(str):
    return [True for i in range(len(str)) if str[i:i+2] == "co" and str[i+3:i+4] == "e"].count(True)

def end_other(a, b):
    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
    return len([True for i in range(-1, len(str)) if str[i:i+1] != "." and str[i+1:i+4] == "xyz"]) > 0



# Warmup-2

def string_times(str, n):
    return str * n

def front_times(str, n):
    return str[:3] * n

def string_bits(str):
    return str[0:len(str):2]

def string_splosion(str):
    splode = ""
    for i in range(len(str)):
        splode += str[:i+1]
    return splode

def last2(str):
    return sum(str[i:-1].startswith(str[-2:]) for i in range(len(str)))

def array_count9(nums):
    return len([i for i in nums if i == 9])

def array_front9(nums):
    return len([i for i in nums[:4] if i == 9]) > 0

def array123(nums):
    return len([True for i in range(len(nums)) if nums[i:i+3] == [1, 2, 3]]) > 0

def string_match(a, b):
    return [a[i:i+2] == b[i:i+2] for i in range(len(a)-1)].count(True)



# Warmup-1

def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile

def sum_double(a, b):
    if a == b:
        return 4 * a
    return a + b

def diff21(n):
    if n > 21:
        return abs(n - 21) * 2
    return abs(n - 21)

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return 90 <= n <= 110 or 190 <= n <= 210

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return a < 0 and b > 0 or a > 0 and b < 0

def not_string(str):
    if str.startswith("not"):
        return str
    return "not " + str

def missing_char(str, n):
    return str[:n] + str[n+1:]

def front_back(str):
    if len(str) == 1:
        return str
    return str[-1:-2:-1] + str[1:-1] + str[0:1]

def front3(str):
    return str[:3] * 3

