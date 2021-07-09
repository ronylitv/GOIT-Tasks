import re

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if not reverse:
        result = re.search(fr'{start_letter}\w+', riddle, )
        return result.group()[:word_length]
    else:
        pos = riddle.find(start_letter)
        result = riddle[pos-word_length+1:pos+1]
        return result[::-1]






print(solve_riddle('mi1powperet', 3, 'r', True))