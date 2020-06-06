

anagram_list = ['dog', 'fog', 'god', 'cat', 'big', 'tac']


def find_anagrams(str_list):
    anagram_pairs_dict = {}
    for anag_str in str_list:
        sorted_string = sort_string(anag_str)
        if sorted_string not in anagram_pairs_dict:
            # anagram_pairs_dict[sorted_string] = []
            anagram_pairs_dict.update({sorted_string: [anag_str]})
        else:
            anagram_pairs_dict[sorted_string].append(anag_str)

    for key in anagram_pairs_dict.keys():
        if len(anagram_pairs_dict[key]) > 1:
            print "Anagram Pair: " + " ".join(val for val in anagram_pairs_dict[key])


def sort_string(str_to_sort):
    return ''.join(sorted(str_to_sort))


find_anagrams(anagram_list)