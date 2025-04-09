def encode(text, look_back, look_ahead):
    # store encoded data
    result = []

    # current index
    i = 0

    while (i < len(text)):

        # start index for look back window
        look_back_idx = max(0, i - look_back)

        # end index for look ahead window
        look_ahead_idx = min(i + look_ahead, len(text))

        jump_back = 0 # keep track of # of jump backs for decoding
        matches = 0   # keep track of # of matches found for decoding

        for j in range(look_back_idx, i):

            start = j
            k = 0 # also used to keep track of current # of matches

            while (i + k < look_ahead_idx) and (text[start] == text[i + k]):

                # increment index
                start += 1
                k += 1

                # reset start
                if (start >= i):
                    start = j

            # record if matches found is more than previous
            if (k >= matches):
                jump_back = i - j
                matches = k


        if (matches > 0):
            # matches found
            if (i + matches < len(text)):
                next_char = text[i + matches]
            # end of text
            else:
                next_char = ""

            # add to result and increment current index
            result.append((jump_back, matches, next_char))
            i += matches + 1

        else:
            # no matches found
            # add to result and increment current index
            result.append((0, 0, text[i]))
            i += 1

    return result


def decode(encoded):
    # store decoded result
    text = []

    # iterate through encoded data
    for jump_back, matches, char in encoded:

        # match found
        if matches > 0:

            # starting index after jump back
            start = len(text) - jump_back

            # length of current text
            str_len = len(text)

            # copy and add the substring
            for i in range(matches):
                text.append(text[start + (i % str_len)])

        # add character to decoded text
        text.append(char)

    return "".join(text)


def LZ77(text, look_back = 16, look_ahead = 16):
    # encode the text
    encoded = encode(text, look_back, look_ahead)
    print(encoded)

    # decode the encoded data
    decoded = decode(encoded)
    print(decoded)

    # check that the decoded text equal the original text
    assert decoded == text

    return 0

if __name__ == "__main__":
    text = "ABABAABBCC"
    look_back  = 5
    look_ahead = 5
    LZ77(text, look_back, look_ahead)
