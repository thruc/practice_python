
def duplicate_dict_del(duplicate_dict: list) -> list:
    return [dict(s) for s in set(frozenset(dd.items()) for dd in duplicate_dict)]

if __name__ == "__main__":
    duplicate_list = [{'name': 'ga:dimension8'}, {'name': 'ga:dimension10'}]

    all_list  = [{'name': 'ga:dimension1'},
            {'name': 'ga:dimension2'},
            {'name': 'ga:dimension3'},
            {'name': 'ga:dimension4'},
            {'name': 'ga:dimension5'},
            {'name': 'ga:dimension6'},
            {'name': 'ga:dimension7'},
            {'name': 'ga:dimension8'},
            {'name': 'ga:dimension9'},
            {'name': 'ga:dimension10'},
            {'name': 'ga:dimension11'},
            {'name': 'ga:dimension12'},
            {'name': 'ga:dimension13'},
            {'name': 'ga:dimension14'},
            {'name': 'ga:dimension15'},
            {'name': 'ga:dimension16'},
            {'name': 'ga:dimension17'},
            {'name': 'ga:dimension18'},
            {'name': 'ga:dimension19'},
            {'name': 'ga:dimension20'}]
    duplicate_list.extend(all_list)

    print(duplicate_dict_del(duplicate_list))