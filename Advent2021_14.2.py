from collections import Counter, defaultdict

def main():

    # Read data and initialize counting dict
    starter, mapping_dict = load_data("/Users/Mateusz/Documents/Programowanie/Advent of Code/input14.txt")
    first_letter = starter[0]
    last_letter = starter[-1]
    letter_pairs_count = defaultdict(lambda: 0)

    # Read in the data into counting dictionary
    for two_letters in zip(starter[:-1], starter[1:]):
        two_letters_joined = ''.join(two_letters)
        letter_pairs_count[two_letters_joined] += 1

   
    # Update the counting dictionary
    for _ in range(40):
        letter_pairs_count = update_letter_pairs(letter_pairs_count, mapping_dict)

    # Pairs into letters
    letters_dict = defaultdict(lambda: 0)

    letters_dict[first_letter] = 1
    letters_dict[last_letter] = 1
    
    for pair, value in letter_pairs_count.items():
        for letter in pair:
            letters_dict[letter] += value

    max_count = max([v for i, v in letters_dict.items()])/2
    min_count = min([v for i, v in letters_dict.items()])/2

    print(int(max_count - min_count))
    

def update_letter_pairs(current_pairs_dict, update_mapping_dict):
    
    temporary_pairs_count = defaultdict(lambda: 0)

    for pair, occurance_number in current_pairs_dict.items():

        add = update_mapping_dict[pair]
        first_letter, second_letter = pair
        
        new_pair_1 = first_letter + add
        new_pair_2 = add + second_letter

        temporary_pairs_count[new_pair_1] += occurance_number
        temporary_pairs_count[new_pair_2] += occurance_number

    return temporary_pairs_count
        


def load_data(file):

    with open(file) as op:

        content = op.read().split("\n")

    starter = content[0]
    mapping = [element for element in content if '->' in element]
    mapping_dict = {element.split('->')[0].strip(): element.split('->')[1].strip() for element in mapping}

    return starter, mapping_dict


if __name__ == "__main__":
    main()