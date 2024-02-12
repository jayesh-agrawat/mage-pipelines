import io
import pandas as pd
import ssl
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

ssl._create_default_https_context = ssl._create_unverified_context

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    dfs = []
    for i in range(1, 13):
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{i:02d}.parquet'
        df = pd.read_parquet(url,engine='pyarrow')
        dfs.append(df)

    return pd.concat(dfs)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
