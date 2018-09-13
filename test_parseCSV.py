import pytest
import parseCSV
import pandas as pd


@pytest.fixture
def data(cmdopt):
    pytest.parsed_data=parseCSV.parse_csv(cmdopt)
    pytest.parsed_data_without_null=parseCSV.drop_null_rows(pytest.parsed_data)


def test_csv_read_data_headers(data):
        result = pytest.parsed_data.columns
        expected = pd.DataFrame(columns=['datetime','Vancouver','Portland','San Francisco','Seattle','Los Angeles','San Diego','Las Vegas','Phoenix','Albuquerque','Denver','San Antonio','Dallas','Houston','Kansas City','Minneapolis','Saint Louis','Chicago','Nashville','Indianapolis','Atlanta','Detroit','Jacksonville','Charlotte','Miami','Pittsburgh','Toronto','Philadelphia','New York','Montreal','Boston','Beersheba','Tel Aviv District','Eilat','Haifa','Nahariyya','Jerusalem','ds','Year']).columns
        assert result.any()==expected.any()

def test_csv_read_random_data_points(data):
        print(pytest.parsed_data_without_null.iloc[0][1])
        assert pytest.parsed_data_without_null.iloc[0][1]== 284.63
