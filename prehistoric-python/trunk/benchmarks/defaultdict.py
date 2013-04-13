def add_to_dict(data, key, value):
    """
    A helper function to add "value" to the set of values for "key", whether or
    not "key" already exists.
    """
    if key in data:
        data[key].add(value)
    else:
        data[key] = set([value])
        
def deferred_to_data(values):
    seen = {}

    add_to_dict(seen, 'model', 'field1')

    if 'model' in seen:
        seen['model'].update(values)
    else:
        # As we've passed through this model, but not explicitly
        # included any fields, we have to make sure it's mentioned
        # so that only the "must include" fields are pulled in.
        seen['model'] = values

    if 'model2' not in seen:
        seen['model2'] = set()
        
    return seen
        
from collections import defaultdict
def deferred_to_data_better(values):
    seen = defaultdict(set)

    seen['model'].add('field1')

    seen['model'].update(values)
    
    seen['model2']

    return seen


def deferred_to_data_setdefault(values):
    seen = {}

    value = seen.setdefault('model', set())
    value.add('field1')

    value = seen.setdefault('model', set())
    value.update(values)
    
    value = seen.setdefault('model2', set())

    return seen


if __name__ == '__main__':
    print deferred_to_data(('field2', 'field3'))
    print deferred_to_data_better(('field2', 'field3'))
    print deferred_to_data_setdefault(('field2', 'field3'))