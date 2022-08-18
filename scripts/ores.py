with open('ores.txt', 'w') as out:
    with open('blocks_2022-01-14_21.57.17.txt', 'r') as inp:
        for line in inp:
            if '|' in line and line.split('|')[7].strip().endswith(' Ore'):
                out.write(line)

with open('coins.txt', 'w') as out:
    with open('items_2022-01-14_21.57.21.txt', 'r') as inp:
        for line in inp:
            if ' Coin ' in line or ' Stamp ' in line:
                out.write(line)
