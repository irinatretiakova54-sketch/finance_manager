import pytest
import datetime
from main import write_transaction
from pathlib import Path


def test_write_transaction():
    """Test write transaction.
    Checking that Function 'write_transaction' writes transaction to the file.
    """

    # Define test values
    data_file = Path("database.txt")
    date = datetime.date(2025, 11, 24)
    amount = 100.25

    # Create empty data base file
    with data_file.open(mode="w"):
        pass

    # call the function
    write_transaction(data_file, date, amount)

    # check the result
    result = data_file.read_text()
    expected_result = "24.11.2025 100.25\n"
    assert expected_result == result
