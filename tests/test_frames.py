import pytest
import pandas as pd
from src.frames import create_dataframe

def test_frame():
    assert type(create_dataframe([1,2,3,4],[5,4,6,7], [1,4,3,2])) == pd.DataFrame
