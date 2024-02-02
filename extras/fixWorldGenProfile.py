import json

if __name__ == '__main__':
    dimensions = {
        0: 'Overworld',
        -1: 'The Nether',
        1: 'The End',
        33: 'Under World',
        -6: 'Mining Dimension',
        7: 'The Twilight Forest',
        684: 'Limbo',
        111: 'Lost Cities',
        50: 'The Abyssal Wasteland',
        51: 'The Dreadlands',
        52: 'Omothol',
        20: 'The Betweenlands',
        14676: 'Emptiness',
        53: 'The Dark Realm',
        28885: 'Hunting Dimension',
        4598: 'Nuclear Wastelands',
        -11325: 'Deep Dark',
        -2: 'Outer Space',
    }

    with open('config/jeresources/world-gen.json', 'r') as fp:
        profile = json.load(fp)

    for entry in profile:
        entry['block'] = ':'.join(entry['block'].split(':')[:3])

        did = int(entry['dim'].split()[1][:-1])
        entry['dim'] = dimensions[did] if did in dimensions else f'Planet {did}'

        if 'dropsList' not in entry:
            entry['dropsList'] = [{
                'itemStack': entry['block'],
                'fortunes': {0: 1, 1: 1, 2: 1, 3: 1},
            }]

    with open('config/jeresources/world-gen.json', 'w') as fp:
        json.dump(profile, fp)
