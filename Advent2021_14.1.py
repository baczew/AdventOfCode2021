from collections import Counter

def main():

    starter, mapping_dict = load_data("/Users/Mateusz/Documents/Programowanie/Advent of Code/input14.txt")
 
    for i in range(10):
        starter = fill_string(starter, mapping_dict, i)
    letter_count = dict(Counter(starter))
    counts = [v for k, v in letter_count.items()]

    print(max(counts) - min(counts))
    

def fill_string(input_string, fill_mapping, n):
    
    result_string = input_string[0]

    for two_letters in zip(input_string[:-1], input_string[1:]):
        
        two_letters_str = ''.join(two_letters)
        added_letter = fill_mapping.get(two_letters_str, '')
        second_letter = two_letters[1]

        result_string += added_letter + second_letter

    return result_string


def load_data(file):

    with open(file) as op:

        content = op.read().split("\n")

    starter = content[0]
    mapping = [element for element in content if '->' in element]
    mapping_dict = {element.split('->')[0].strip(): element.split('->')[1].strip() for element in mapping}

    return starter, mapping_dict


if __name__ == "__main__":
    main()