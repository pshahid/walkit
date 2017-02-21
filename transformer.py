import json
import csv


def load_json(fp):
    with open(fp, 'r') as f:
        return json.load(f)


def clean_single(sub):
    try:
        del sub['fields']['nsfw']
    except KeyError:
        pass  # isn't there, probably already deleted it so we don't care
    return sub['fields']


def clean(subreddits):
    for sub in subreddits:
        yield clean_single(sub)


def write_csv(new_csv, subreddits):
    with open(new_csv, 'w') as csvfile:
        # Errors if len(subreddits) < 1
        sub = clean_single(dict(subreddits[0])).keys()
        writer = csv.DictWriter(csvfile, list(sub))
        writer.writeheader()
        for row in clean(subreddits):
            writer.writerow(row)

if __name__ == '__main__':
    j = load_json('subreddits.json')
    write_csv('subreddits.csv', j)
