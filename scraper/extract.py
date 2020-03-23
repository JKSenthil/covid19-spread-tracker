import re

def extract_counties_and_cases(data, m):
    """Process data that could have a couple of different formats:

            'Dutchess', '+33', '82', '+1', '1', '1.2%',
            'Monroe', '+22', '68', '1', '1.5%',
            'Erie', '56', '0', '0%',

       ignoring the '+NN' increases, to:

            {
                'Dutchess': [82, 1],
                'Monroe': [68 1],
                'Erie': [56, 0],
            }
    """
    i = 0
    while i < len(data):
        if not re.match(r'[a-zA-Z]', data[i]):
            i+=1
            continue

        county = data[i]
        i+=1

        if '+' in data[i]:
            i+=1
        
        cases = int(data[i])
        i += 1

        if '+' in data[i]:
            i+=1
        
        deaths = int(data[i])
        
        m[county] = [cases, deaths]

    return m