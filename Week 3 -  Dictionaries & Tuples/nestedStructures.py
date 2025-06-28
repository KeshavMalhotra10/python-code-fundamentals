#source: https://medium.com/theengineeringgecko/nested-data-structures-in-python-bbb3fb5f5748

universities = [
    {'name': "University of Waterloo", 'rank': 1},
    {'name': 'University of Toronto', 'rank': 2},
    {'name': "University of British Columbia", 'rank': 3}
]

##print(universities[2]['name'])


#iterate all universities using a for loop

for university in universities:
    name = university['name']
    rank = university['rank']
    print(f"{name} is ranked number {rank} in Canada.")