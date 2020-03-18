import requests

def get_code_and_name():
    url = 'https://cdn.jsdelivr.net/gh/highcharts/highcharts@c116b6fa6948448/samples/data/us-counties-unemployment.json'

    r = requests.get(url)
    j = r.json()

    code = []
    name = []

    for row in j:
        if "PR" in row["name"]:
            break
        code.append(row["code"])
        name.append(row["name"])
    return code, name

def get_json():
    url = 'https://cdn.jsdelivr.net/gh/highcharts/highcharts@c116b6fa6948448/samples/data/us-counties-unemployment.json'
    r = requests.get(url)
    return r.json()
