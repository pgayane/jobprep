
def word_permutations(word, result):

    results = []

    if word == []:
        results.append(result)
        return results

    for i in range(0, len(word)):
        list = word_permutations(word[0:i] + word[i+1:], result + word[i])

        results.extend(list)

    return results


def word_all_permutations(word, result, list):
    
    if word == []:
        return
 
    for i in range(0, len(word)):
        list.append(result + word[i])
        word_all_permutations(word[0:i] + word[i+1:], result + word[i], list)

# def only_word_permutations(word) TODO

if __name__ == '__main__':
    word = ['c', 'o', 'w', 'l']
    # print word_permutations(word, '')

    list = []
    word_all_permutations(word, '', list) 
    print len(list), list

