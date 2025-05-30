import pandas as pd


def create_dataframe(list_1, list_2, list_3) -> pd.DataFrame:

    df = pd.DataFrame({'Col_D': list_1, 'Col_B': list_2, 'Col_C': list_3})

    return df


print(create_dataframe([1, 2, 3, 4], [5, 4, 6, 7], [1, 4, 3, 2]))
