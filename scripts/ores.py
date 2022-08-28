with open('ores.txt', 'w') as out:
    with open('../config/tellme/blocks_2022-08-18_17.08.35.txt', 'r') as inp:
        for line in inp:
            if '|' in line and line.split('|')[7].strip().endswith(' Ore'):
                out.write(line)

with open('coins.txt', 'w') as out:
    with open('../config/tellme/items_2022-08-18_17.08.40.txt', 'r') as inp:
        for line in inp:
            if ' Coin ' in line or ' Stamp ' in line:
                out.write(line)
