from pathlib import Path

with open('extras/ores.txt', 'w') as out:
    with open(next(Path('config/tellme/').glob('blocks_*_*.txt')), 'r') as inp:
        for line in inp:
            if '|' in line and line.split('|')[7].strip().endswith(' Ore'):
                out.write(line)

with open('extras/coins.txt', 'w') as out:
    with open(next(Path('config/tellme/').glob('items_*_*.txt')), 'r') as inp:
        for line in inp:
            if ' Coin ' in line or ' Stamp ' in line or ' Experience ' in line:
                out.write(line)
