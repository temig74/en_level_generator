from random import choice

def mutator(s1, s2, change1, change2):
    s1_len = len(s1)
    s2_len = len(s2)
    if abs(s1_len - s2_len) != abs(change1 - change2):
        return False

    cnt = 0
    for s1_elem, s2_elem in zip(s1, s2):
        if s1_elem == s2_elem:
            cnt += 1
        else:
            break

    for s1_elem, s2_elem in zip(s1[::-1][:min(s1_len, s2_len)-cnt], s2[::-1]):
        if s1_elem == s2_elem:
            cnt += 1
        else:
            break
    return True if cnt == min(s1_len, s2_len) - min(change1, change2) else False


def gen_random_format(format_type, my_dict):
    result_list = []
    match format_type:
        case 'meta':
            while True:
                word1 = choice(my_dict)
                for word2 in my_dict:
                    if mutator(word1, word2, 1, 1):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'meta2':
            while True:
                word1 = choice(my_dict)
                for word2 in my_dict:
                    if mutator(word1, word2, 2, 2):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'logo':
            while True:
                word1 = choice(my_dict)
                for word2 in my_dict:
                    if mutator(word1, word2, 1, 0):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'logo2':
            while True:
                word1 = choice(my_dict)
                for word2 in my_dict:
                    if mutator(word1, word2, 2, 0):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'brukva':
            while True:
                word1 = choice(my_dict)
                for word2 in my_dict:
                    if mutator(word1, word2, 2, 1):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'gib3':
            while True:
                word1 = choice(my_dict)
                if len(word1) > 3:
                    for word2 in my_dict:
                        if len(word2) > 3:
                            if word1[-3:] == word2[:3]:
                                result_list.append(word2)
                    if result_list:
                        break
            return word1, choice(result_list)

        case 'gib4':
            while True:
                word1 = choice(my_dict)
                if len(word1) > 4:
                    for word2 in my_dict:
                        if len(word2) > 4:
                            if word1[-4:] == word2[:4]:
                                result_list.append(word2)
                    if result_list:
                        break
            return word1, choice(result_list)

        case 'plus':
            while True:
                word1 = choice(my_dict)
                word1_sorted = sorted(word1)
                for word2 in my_dict:
                    if mutator(word1_sorted, sorted(word2), 1, 0) and not mutator(word1, word2, 1, 0):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'anag':
            while True:
                word1 = choice(my_dict)
                word1_sorted = sorted(word1)
                for word2 in my_dict:
                    if word1 != word2 and word1_sorted == sorted(word2):
                        result_list.append(word2)
                if result_list:
                    break
            return word1, choice(result_list)

        case 'shar':
            min_len = 3
            words_set = set(my_dict)
            while True:
                word1 = choice(my_dict)
                if len(word1) >= min_len:
                    for word2 in my_dict:
                        if len(word2) >= min_len and word1+word2 in words_set:
                            result_list.append(word2)
                    if result_list:
                        break
            return word1, choice(result_list)
