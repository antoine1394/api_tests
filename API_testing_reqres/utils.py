def extract_data_by_property_name(data: [], property_name: str) -> []:
    result = []

    for item in data:
        value = item[property_name]
        result.append(value)

    return result


def assert_array_by_value(left_array: [], right_array: []):
    assert left_array.sort() == right_array.sort()




