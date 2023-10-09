"""
assignment1.py
Name: Wong Chee Hao
Student ID: 32734751
E-mail: cwon0112@student.monash.edu
"""

def counting_sort_number(new_list,base,column_1,column_2):
    """
    This function sort the inpuut list in descending order by new_list[column_1][column_2].(without comparison, stable)

    Input:
        new_list: A list of N elements
        base: Range of the digits we are sorting by
        column_1: The column of the list elements to sort by(Ex. score)
        column_2: The place of the number(Ex. right-significant digit)
    Return:
        new_list: A list of N elements sorted in descending order by new_list[column_1][column_2].

    Time complexity: 
        Best: O(N + base) = O(N)
        Worst: O(N + base) = O(N)
    Space complexity: 
        Input: O(N + base) = O(N)
        Aux: O(N + base) = O(N)

    """
    if len(new_list) != 0:

        # find maximum
        max_item = (new_list[0][column_1] // pow(base,column_2)) % base
        for item in new_list:
            item = (item[column_1] // pow(base,column_2)) % base
            if item > max_item:
                max_item = item

        # initialise count_array
        count_array = [None] * (max_item + 1)
        for i in range(len(count_array)):
            count_array[i] = []

        # update count_array
        for item in new_list:
            item_index = (item[column_1] // pow(base,column_2)) % base
            count_array[item_index].append(item)

        # update input array
        index = 0 
        for i in range(len(count_array)-1,-1,-1):
            frequency = len(count_array[i])
            for j in range(frequency):
                new_list[index] = count_array[i][j]
                index = index + 1

    return new_list

def counting_sort_list(new_list, column_1, column_2):
    """
    This function sort the input list in ascending order by new_list[column_1][column_2].(without comparison, stable)

    Input:
        new_list: A list of N elements
        column_1: The column of the list elements to sort by(Ex. team1, team2)
        column_2: The place of the string(Ex. right-significant alphabets)
    Return:
        new_list: A list of N elements sorted in ascending order by new_list[column_1][column_2].

    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N)
        Aux: O(N)

    """
    if len(new_list) != 0:

        # find maximum
        max_item = ord(new_list[0][column_1][column_2]) - 65
        for item in new_list:
            item = ord(item[column_1][column_2]) - 65
            if item > max_item:
                max_item = item

        # initialise count_array
        count_array = [None] * (max_item + 1)
        for i in range(len(count_array)):
            count_array[i] = []

        # update count_array
        for item in new_list:
            item_index = ord(item[column_1][column_2]) - 65
            count_array[item_index].append(item)

        # update input array
        index = 0
        for i in range(len(count_array)):
            frequency = len(count_array[i])
            for j in range(frequency):
                # print(new_list)
                new_list[index] = count_array[i][j]
                index = index + 1

    return new_list

def counting_sort_string(new_string):
    """
    This function sort the input string in ascending lexicographical order.(without comparison, stable)

    Input:
        new_string: String of length M (only uppercase english letter - A-Z)
    Return:
        new_string: String of length M (only uppercase english letter - A-Z) sorted by ascending lexicographical order

    Time complexity: 
        Best: O(M)
        Worst: O(M)
    Space complexity: 
        Input: O(M)
        Aux: O(M)

    """
    if len(new_string) != 0:

        # find maximum
        max_item = ord(new_string[0]) - 65
        for item in new_string:
            item = ord(item) - 65
            if item > max_item:
                max_item = item

        # initialise count_array
        count_array = [None] * (max_item + 1)
        for i in range(len(count_array)):
            count_array[i] = []

        # update count_array
        for item in new_string:
            item_index = ord(item) - 65
            count_array[item_index].append(item)
    
        # update input array
        new_string = ""
        for i in range(len(count_array)):
            frequency = len(count_array[i])
            for j in range(frequency):
                new_string += count_array[i][j]
 
    return new_string

def double_list(new_list):
    """
    This function loop through the matches to add their equivalent matches to list.(swap team1 with team2, newscore = 100 - score)

    Input:
        new_list: A list of N matches
    Return:
        new_list: A list of 2N matches

    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N)
        Aux: O(N)

    """
    for i in range(len(new_list)):
        new_list.append([new_list[i][1],new_list[i][0],100 - new_list[i][-1]])
    
    return new_list

def arrange_input(lst):
    """
    This function arrange the input list: lst[:j+1] is the unique elements, lst[j+1:] is the duplicate elements.

    Input:
        lst: A list of N elements
    Return:
        j: lst[:j+1] is the unique elements

    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(1)
        Aux: O(1)

    """   
    i = 0
    j = 0
    
    while i < len(lst) - 1:
        if lst[j] == lst[i+1]:
            i += 1
        else:
            lst[j+1], lst[i+1] = lst[i+1], lst[j+1]
            j += 1
            i += 1

    return j

def search_match(results, score, j):
    """
    This function search the matches with the same score as input score in results[:j+1].

    Input:
        results: A list of N matches
        score: Score obtained by team1 in a match against team2. (An integer within the range of 0 to 100 inclusive.)
        j: results[:j+1] are the unique matches
    Return:
        lst: A list of matches with the same score as input score.

    Time complexity: 
        Best: O(1)
        Worst: O(N)
    Space complexity: 
        Input: O(N)
        Aux: O(1)

    """   

    lst = []

    for i in range(j+1):
        if score == results[i][-1]:
            if i == 0 or results[i][-1] != lst[0][-1]:
                lst = [results[i]]
            elif results[i][-1] == lst[0][-1]:
                lst += [results[i]]
        elif score != results[i][-1]: 
            if score > results[i][-1]:
                break
            elif score < results[i][-1]:
                if i == 0 or results[i][-1] != lst[0][-1]:
                    lst = [results[i]]
                elif results[i][-1] == lst[0][-1]:
                    lst += [results[i]]

    return lst

def analyze(results, roster, score):
    """
    This function does magic
    Written by l337coderblazeIT

    Input:
        results: A list of N matches
        roster: Indicate the character set of team1 and team2, roster=5 indicates a character set of {A, B, C, D,E}.(An integer within the range of 1 to 26 inclusive.)
        score: Score obtained by team1 in a match against team2. (An integer within the range of 0 to 100 inclusive.)
    Return:
        [top10matches, searchedmatches]
        top10matches: A list of 10 matches with the highest score.(Or the maximum number of matches possible if less than 10 matches in results.)
        searchedmatches: A list of matches with the same score as input score.
        The returned matches are sorted rstly in descending order by their scores, followed by 
        ascending lexicographical order for team1 (where scores are equal), and nally by
        ascending lexicographical order for team2 (where scores and team1 are equal).
    Time complexity: 
        Best:O(NM)
        Worst:O(NM)
    Space complexity: 
        Input:O(N)
        Aux:O(NM)

    """
    # Sort team1 & team2 in lexicographical order
    for i in range(len(results)):
        for j in range(2):
            results[i].insert(j,counting_sort_string(results[i][j]))
            results[i].pop(j+1)

    # complete the list
    results = double_list(results)

    # Sort matches in lexicographical order by team2, then team1
    for i in range(1,-1,-1):
        for j in range(len(results[0][0]) - 1,-1,-1):
            counting_sort_list(results,i,j)

    # Sort matches in descending order by their scores(base 10)
    for i in range(3):  # Score is 0 - 100 inclusive
        counting_sort_number(results,10,-1,i)  

    # Arrange matches to avoid duplicate matches.
    j = arrange_input(results)

    # If >= 10 matches, top10Matches contains 10 matches with the highest score.
    if j >= 9:
        top10Matches = [results[:10]]
    # If < 10 matches, top10Matches contains the maximum number of matches possible.
    else:
        top10Matches = [results[:j+1]]

    # A list of matches with the same score as score.
    searchedmatches = [search_match(results, score, j)]

    # Return [top10matches, searchedmatches]    
    return top10Matches + searchedmatches

if __name__ == "__main__":
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
        ]
    # looking for a score of 64
    score = 64