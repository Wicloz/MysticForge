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
    }

    with open('../config/jeresources/world-gen.json', 'r') as fp:
        profile = json.load(fp)

    for entry in profile:
        if entry['dim'].startswith('Dim '):
            did = int(entry['dim'].split()[1][:-1])
            entry['dim'] = dimensions[did]

    with open('../config/jeresources/world-gen.json', 'w') as fp:
        json.dump(profile, fp)
