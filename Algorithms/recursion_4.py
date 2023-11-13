from typing import Dict, Any


def count_dict_depth(dictionary: Dict[str, Any], result: int = 1) -> int:
    dict_items = dictionary.values()
    for item in dict_items:
        if isinstance(item, dict):
            return count_dict_depth(item, result + 1)
    return result
