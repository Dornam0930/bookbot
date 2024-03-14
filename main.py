def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        letters_dict = letter_count(file_contents)
        #print(letters_dict)
        letters_list = dict_to_list(letters_dict)
        letters_list.sort(reverse=True, key=sort_by)
        #print(letters_list)

        for i in range(0,len(letters_list)):
            print(f"The '{list(letters_list[i].keys())[0]}' character was found {list(letters_list[i].values())[0]} times")
        
        print("--- End report ---")


def letter_count(input):
    lower = input.lower()
    letters = {}
    for l in lower:
        if l.isalpha():
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1

    return letters

def dict_to_list(dict):
    list_dict = []
    for key, value in dict.items():
        list_dict.append({key:value})
    return list_dict

def sort_by(input):
    return list(input.values())[0]

main()