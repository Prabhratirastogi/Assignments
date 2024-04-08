# Python Assignments

This repository contains Python scripts for various assignments covering data manipulation, algorithm implementation, file handling, RESTful API design, and web scraping.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Prabhratirastogi/Assignments
   ```

2. Install the required dependencies:

   ```sh
   pip install pandas beautifulsoup4 django djangorestframework
   ```

## Assignment 1: Data Manipulation and Analysis

- **Script**: `data_analysis.py`
- **Description**: Reads data from a CSV file, calculates the average age of customers, and finds the most common domain name in email addresses.
- **Input**: `data.csv` (CSV file with columns: firstname, lastname, email, age)
- **Output**: Average age of customers and most common domain name in email addresses.

## Assignment 2: Algorithm Implementation and Optimization

- **Script**: `algorithm_implementation.py`
- **Description**: Implements a function to calculate the maximum profit that can be achieved by buying and selling a stock once.
- **Input**: List of integers representing stock prices on consecutive days.
- **Output**: Maximum profit that can be achieved by buying and selling the stock once.

## Assignment 3: File Handling and Text Processing

- **Script**: `file_handling.py`
- **Description**: Reads a text file with a list of words, finds anagrams, and groups them together.
- **Input**: `words.txt` (Text file with one word per line)
- **Output**: `anagrams.txt` (Text file with grouped anagrams)

## Assignment 4: Web Scraping and Data Analysis

- **Script**: `web_scraping.py`
- **Description**: Scrapes data from a website to retrieve information about top-rated movies and stores it in a CSV file.
- **Input**: Website URL (`https://www.imdb.com/chart/top/`)
- **Output**: `top_movies.csv` (CSV file with information about top-rated movies)

## Assignment 5: Design and Implement a RESTful API

- **Description**: Design and implement a RESTful API using Flask or Django for managing users and products with CRUD operations.
- **Files**: `api.py`, `models.py`, `serializers.py`



## Testing

- Use `pytest` to run the test cases for each assignment.
