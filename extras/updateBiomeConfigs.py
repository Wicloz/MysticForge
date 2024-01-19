from pathlib import Path
import json


BIOMESCONFIG = Path('config/biomesoplenty/biomes/')


if __name__ == '__main__':
    for default in (BIOMESCONFIG / 'defaults').glob('*/*.json'):
        with open(default, 'r') as fp:
            biome = json.load(fp)
            changed = False

            if 'amber' in biome['generators']:
                del biome['generators']['amber']
                changed = True
            if 'sapphire' in biome['generators']:
                del biome['generators']['sapphire']
                changed = True

            if changed:
                with open(BIOMESCONFIG / default.name, 'w') as fp:
                    json.dump(biome, fp, indent=2)
