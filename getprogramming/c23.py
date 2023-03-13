#!/usr/bin/env python3


def read_file(file):
    """
    file, a file object
    Starting from the first line, it reads every 2 lines and stores in a tuple.
    Starting from the swcond line, it reads every 2 lines and stores in a tuple.
    Return a tuple of the two tuples.
    """
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n", "")
        if line_count % 2 == 0:
            first_every_2 += (stripped_line,)
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line,)
        line_count += 1
    return (first_every_2, second_every_2)


def sanitize(phones):
    """
    phones, a tuple of strings
    Removes all spaces, dashes, and open/close parentheses.
    Returns a tuple with cleaned up elements.
    """
    clean_string = ()
    for st in phones:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        clean_string += (st,)
    return clean_string


def analyze_friends(names, phones, areacodes, places):
    """
    names, a tuple of names
    phones, a tuple of phones associartes with the names
    areacodes, a tuple of strings for the area_codes
    places, a tuple of strings for the US States
    Prints out how many names we hace and every unique state that is
    represented by their area codes
    """

    def get_unique_area_codes():
        """
        Returns a tuple of all unique area_codes in phones
        """
        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:
                area_codes += (ph[0:3],)
        return area_codes

    def get_states(some_areacodes):
        """
        some_area_codes, a tuple of area codes
        Returns a tuple of states associated with those area codes
        """
        states = ()
        for ac in some_areacodes:
            if ac not in areacodes:
                states += ("BAD AREACODE",)
            else:
                index = areacodes.index(ac)
                if places[index] not in states:
                    states += (places[index],)
        return states

    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)
    print("You have", num_friends, "friends.")
    print("They live in", unique_states)


friends_file = open("phonedata.txt")
(names, phones) = read_file(friends_file)
areacodes_file = open("area_codes.txt")
(areacodes, states) = read_file(areacodes_file)
clean_phones = sanitize(phones)

analyze_friends(names, clean_phones, areacodes, states)

friends_file.close()
areacodes_file.close()
