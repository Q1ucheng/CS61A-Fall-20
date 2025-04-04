"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    valid_paragraphs = []
    for element in paragraphs:
        if select(element):
            valid_paragraphs.append(element)
    return valid_paragraphs[k] if k < len(valid_paragraphs) else ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select_helper(paragraph):
        paragraph = split(remove_punctuation(lower(paragraph)))
        for element in paragraph:
            if element in topic:
                return True
        return False
    return select_helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    num, denum = 0, len(typed_words)
    if len(typed_words) == 0:
        return 0.0
    if len(reference_words) == 0:
        return 0.0
    for index in range(len(typed_words)):
        if index < len(reference_words):
            if typed_words[index] == reference_words[index]:
                num = num + 1
    return num / denum * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # def pack(x, y):
    #     return [x, y]
    
    # if user_word in valid_words:
    #     return user_word

    # word_list = []
    # for element in valid_words:
    #     difference = diff_function(user_word, element, limit)
    #     if difference > limit:
    #         continue
    #     else:
    #         word_list.append(pack(difference, element))
    
    # if word_list == []:
    #     return user_word
    # else:
    #     min_diff = word_list[0][0]
    #     return_word = word_list[0][1]
    #     for diff, word in word_list[1:]:
    #         if diff < min_diff:
    #             min_diff = diff
    #             return_word = word
    #     return return_word
    if user_word in valid_words:
        return user_word
    min_word = min(valid_words, key=lambda x: diff_function(user_word, x, limit))
    if diff_function(user_word, min_word, limit) <= limit:
        return min_word
    else:
        return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    # num_difference = abs(len(start) - len(goal))
    # if len(start) == 0:
    #     return str_difference + num_difference
    # def count(start, goal, difference, times):
    #     if len(start) == 0:
    #         total = difference + num_difference
    #         return total 
    #     if len(start) > len(goal):
    #         next_start = start[:len(start)-1]
    #         return count(next_start, goal, 0, times+1) if times <= limit+1 else limit + 1
    #     if start[len(start)-1] != goal[len(start)-1]:
    #         difference = difference + 1
    #     next_start = start[:len(start)-1]
    #     return count(next_start, goal, difference, times+1) if times <= limit+1 else limit + 1

    # num_difference = abs(len(start) - len(goal))
    # return count(start, goal, 0, 0)
    def count(start, goal, diff):
        if diff > limit:
            return limit+1
        if len(start) == 0:
            return diff + len(goal)
        if len(goal) == 0:
            return diff + len(start)
        else:
            if start[0] == goal[0]:
                return count(start[1:], goal[1:], diff)
            else:
                return count(start[1:], goal[1:], diff+1)
    return count(start, goal, 0)

    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return limit + 1
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) + len(goal)
        # END
    
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)

    else:
        add_diff = pawssible_patches(start, goal[1:], limit-1) + 1
        remove_diff = pawssible_patches(start[1:], goal, limit-1) + 1
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1) + 1
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff)
        # END
    
def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # def pack(user_id, point):
    #     return {'id': user_id, 'progress': point}
    # def helper(typed, prompt, user_id):
    #     if len(typed) == 0 and len(prompt) == 0:
    #         send(pack(user_id, 100.0))
    #         return 100.0
    #     if len(typed)*len(prompt) == 0 and len(typed)+len(prompt)!=0:
    #         send(pack(user_id, ori_num/denum))
    #         return ori_num/denum
    #     if typed[0] == prompt[0]:
    #         return helper(typed[1:], prompt[1:], user_id)
    #     else:
    #         send(pack(user_id, (ori_num - len(typed)) / denum))
    #         return (ori_num - len(typed)) / denum
    # denum = len(prompt)
    # ori_num = len(typed)
    # return helper(typed, prompt, user_id)
    index, correct_count = 0, 0
    while index < len(typed):
        if typed[index] != prompt[index]:
            break
        correct_count += 1
        index += 1
    result = correct_count / len(prompt)
    send({"id": user_id, "progress": result})
    return result
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_diff = [[times_per_player[i][j+1]-times_per_player[i][j] for j in range(len(times_per_player[i])-1)] for i in range(len(times_per_player))]
    return game(words, time_diff)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # create a list of lists, one for each player, representing the words each player typed fastest
    # loop through every single word
        # for the player that typed that word the fastest, append it to their respective list
        # remember to use word_at and#"word_index"!
    # return the list of fastest words
    result = []
    for _ in player_indices:
        result.append([])

    for word in word_indices:
        find_player_time_for_word = lambda player: time(game, player, word)
        fatest_player = min(player_indices, key=find_player_time_for_word)
        result[fatest_player].append(word_at(game, word))

    return result

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)