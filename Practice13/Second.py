def find_line(ft, arg1, arg2):
    if arg1 == arg2:
        return [arg1]
    parents = ft.get(arg1, set())
    for parent in parents:
        lineage = find_line(ft, parent, arg2)
        if lineage:
            return [arg1] + lineage
    return []

familytree = {
    'Kalle': {'Teet', 'Maris'},
    'Maris': {'Konstantin', 'Mari'},
    'Rita': {'Teet', 'Maris'},
    'Siim': {'Teet', 'Maris'},
    'Mari': {'Karl', 'Leeni'},
    'Teet': {'Joosep', 'Adele'},
    'Adele': {'Johannes', 'Leida'},
    'Konstantin': {'Viktor', 'Jelena'},
    'Joosep': {'August', 'Emma'},
    'Viktor': {'Nikolai', 'Maria'}
}

result = find_line(familytree, 'Rita', 'Viktor')
print(result)  