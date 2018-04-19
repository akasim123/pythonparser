import sys
import time
from asst1_part_a import WordFrequencies

if __name__ == "__main__":
    start_time = time.time()
    file1 = WordFrequencies(sys.argv[1])
    file2 = WordFrequencies(sys.argv[2])
    file1.read_file_into_string()
    file2.read_file_into_string()
    file1.split_string_into_word_list()
    file2.split_string_into_word_list()
    file1.put_words_into_dictionary()
    file2.put_words_into_dictionary()
    print("\n")
    result = []
    print("--------RESULT----------")
    for i in file1.D.keys():
        for j in file2.D.keys():
            if i == j:
                result.append(i)

    print("# of common words: {}".format(len(result)))
    print("------------------------")
    print("\n")
    print("These words are: ")
    print("----------------")

    for x in result:
        print(x)

    print("\n")
   ## print("--- %s seconds ---" % (time.time() - start_time))


## Run time complexity:

## 1st time: --- 0.0105760097504 seconds ---
## 2nd time (with double the input): --- 0.0154500007629 seconds ---
## 3rd time (with quadruple the input): --- 0.153849840164 seconds ---

## Exponential
