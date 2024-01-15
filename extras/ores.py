with open('ores.txt', 'w') as out:
    with open('../config/tellme/blocks_2023-06-07_16.45.30.txt', 'r') as inp:
        for line in inp:
            if '|' in line and line.split('|')[7].strip().endswith(' Ore'):
                out.write(line)

with open('coins.txt', 'w') as out:
    with open('../config/tellme/items_2023-06-07_16.45.35.txt', 'r') as inp:
        for line in inp:
            if ' Coin ' in line or ' Stamp ' in line or ' Experience ' in line:
                out.write(line)
