import collections
import datetime
import json


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def treat_data(raw_data, column_names):
    rows = []
    for data in raw_data:
        flatten_data = flatten(data, parent_key='', sep='_')
        row = []
        for column in column_names:
            try:
                if isinstance(flatten_data[column], list):
                    row.append(json.dumps(flatten_data[column]))
                else:
                    try:
                        d = datetime.datetime.strptime(flatten_data[column], '%d/%m/%Y')
                        row.append(d.strftime("%Y-%m-%d"))
                    except:
                        row.append(flatten_data[column])
            except KeyError:
                row.append(None)
        rows.append(row)
    return rows
