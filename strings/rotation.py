def areRotations(s1, s2):
    # check length of both strings are equal or not
    s3 = s1 + s1
    if len(s1) != len(s2):
        return False
    else:
        if s2 in s3:
            return True
    return False


# Driver code
if __name__ == "__main__":
    string1 = "ABCD"
    string2 = "CDBA"
    # Function call
    if areRotations(string1, string2):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")