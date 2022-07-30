def count_duplicates(items):
    if items is None:
        raise ValueError('You must pass a non-null array')
    counts = {}
    for item in items:
        value = 1 if counts.get(item) is None else counts.get(item) + 1
        counts[item] = value
        # counts.update({item: value})
        # counts.update([(item, value)])
    return counts


if __name__ == "__main__":
    print(count_duplicates(['foo', 'bar', 'foo', 'bar', 'Foo', 'Bar']))
    print(count_duplicates([1, 2, 1, 2, 3, 0]))
    print(count_duplicates([True, False, True]))
    print(count_duplicates(['foo', 'bar', 'foo', 'bar', 'Foo', 'Bar', 1, 2, 1, 2, 3, 0]))
    print(count_duplicates([]))
    print(count_duplicates(['foo', None, 1]))
    print(count_duplicates(None))

