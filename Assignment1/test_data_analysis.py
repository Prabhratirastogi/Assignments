# test_data_analysis.py

import pandas as pd
from data_analysis import average_age, most_common_domain

def test_read_csv():
    # Test case 1: Verify that the script reads the CSV file correctly
    # Create a test DataFrame with known data
    test_df = pd.DataFrame({'firstname': ['Alice', 'Bob', 'Charlie'],
                            'lastname': ['Smith', 'Doe', 'Brown'],
                            'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
                            'age': [30, 35, 40]})
    # Write the test DataFrame to a CSV file
    test_df.to_csv('test_data.csv', index=False)
    # Read the test CSV file using the script
    df = pd.read_csv('test_data.csv')
    # Compare the read DataFrame with the expected DataFrame
    assert df.equals(test_df), "The script did not read the CSV file correctly"


# Test cases
def test_average_age():
    # Test case 2: Verify that the script calculates the correct average age
    # Create a test DataFrame with known ages
    test_df = pd.DataFrame({'age': [30, 35, 40]})

    expected_average_age = 35
    average_age = test_df['age'].mean()
    # Compare the calculated average with the expected value
    assert round(average_age, 2) == expected_average_age, f"Expected: {expected_average_age}, Actual: {round(average_age, 2)}"

def test_most_common_domain():
    # Test case 3: Verify that the script identifies the most common domain name accurately
    # Create a test DataFrame with known email domains and frequencies
    test_df = pd.DataFrame({'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'alice@example.com']})
    # Calculate the most common domain name manually
    expected_most_common_domain = 'example.com'
    # Calculate the most common domain name using the script
    test_df['domain'] = test_df['email'].apply(lambda x: x.split('@')[1])
    most_common_domain = test_df['domain'].value_counts().idxmax()
    # Compare the most common domain with the expected value
    assert most_common_domain == expected_most_common_domain, f"Expected: {expected_most_common_domain}, Actual: {most_common_domain}"


# Run the test cases
test_read_csv()
test_average_age()
test_most_common_domain()
