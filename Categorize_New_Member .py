def openOrSenior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result


def betteropenOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open"
            for (age, handicap) in data]