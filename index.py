def swap():
    """ Swapping values """
    num1, num2 = 10, 5
    num1, num2 = num2, num1
    print(num1, num2)


def make_single_string():
    """ Create a single string from all of elements in list """
    a = ["Python", "is", "awesome"]
    print(" ".join(a))


def compare_chains(num):
    """ Chained Comparison with all kind of operators """
    print(4 < num < 7)
    print(1 == num < 10)


from collections import Counter


def find_the_most_frequent_value():
    """ Find The Most Frequent Value In A List. """
    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 3, 4]
    print(max(set(a), key=a.count))
    cnt = Counter(a)
    print(cnt.most_common(3))


def is_anagrams(str1, str2):
    """ Checking if two words are anagrams """
    print(Counter(str1) == Counter(str2))


def transpose_array():
    """ Transpose 2d array """
    original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    transposed = zip(*original)
    print(list(transposed))


def reverse_string():
    """ reverse string with special case of slice step param """
    a = 'abcasjdaudsiosadjsnadasd'
    print(a[::-1])
    """ interacting over string contents in reverse efficiently """
    for char in reversed(a):
        print(char)
    """ reversing an integer through type conversion and slicing """
    num = 123456789
    print(int(str(num)[::-1]))


def product(a, b):
    return a * b


def add(a, b):
    return a + b


def chained_function_call():
    """ Call different functions with same arguments based on condition """
    b = True
    print((product if b else add)(5, 7))


def get_dictionary():
    """ Return None or default value, when key is not in dict """
    d = {
        'a': 1,
        'b': 2
    }
    print(d.get('c', 3))  # if c is not in d to return 3 ( 3 is default value)


from operator import itemgetter


def sort_dictionary():
    """ sort dictionary by its value with the built-in sorted() function and a 'key' argument """
    d = {
        'apple': 10,
        'orange': 12,
        'banana': 5,
        'mango': 25
    }
    print(sorted(d.items(), key=lambda x: x[1]))  # x[1] point to value in dic, so they're sorted by value
    """ sort using operator itemgetter instead of using lambda """
    """ Both key=lambda x: x[1]) and key=itemgetter(1) are same """
    print(sorted(d.items(), key=itemgetter(1)))


def for_else():
    """ else gets called when for loop does not reach break statement """
    a = [1, 2, 3, 4, 5]
    for el in a:
        if el == 0:
            break
    else:
        print('did not break out of for loop')

if __name__ == "__main__":
    # make_single_string()
    # find_the_most_frequent_value()
    # is_anagrams("ab", "cba")
    # reverse_string()
    # transpose_array()
    # compare_chains(6)
    # chained_function_call()
    # get_dictionary()
    sort_dictionary()