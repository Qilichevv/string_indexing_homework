def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
     
    a=0
    if s[0].isdigts():
        a += 1
    else:
        a+=0
    if s[1].isdigts():
        a +=1
    else:
        a+=0
    if s[2].isdigts():
        a +=1
    else:
        a+=0
    if s[3].isdigts():
        a += 1
    else:
        a+=0
    if s[4].isdigts():
        a +=1
    else:
        a+=0
    if s[5].isdigts():
        a +=1
    else:
        a+=0
    return a
