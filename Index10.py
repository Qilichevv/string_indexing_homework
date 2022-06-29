def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s=int(s)
    s1=0%10
    s//=10

    s2=0%10
    s//=10

    s3=0%10
    s//=10

    s4 =0%10
    s//=10

    s5 =0%10
    s//=10

    return s1+s2+s3+s4+s5