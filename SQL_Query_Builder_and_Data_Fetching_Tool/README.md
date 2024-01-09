# SQL Query Builder and Data Fetching Tool

> This code provides a Python script that integrates with OpenAI's language model and MySQL database to create SQL queries from natural language input and fetch data from the database. Below is an overview of the key components and functionalities of this code:

## Components

1. **OpenAI Integration**: This script uses OpenAI's GPT-4 model for natural language processing. An OpenAI API key is required for authentication.

2. **SQL Query Builder Tool**: The `MysqlQueryBuilderTool` is designed to generate SQL queries from natural language input. It takes a user's query in English and converts it into a SQL query based on predefined templates and database schema. The resulting SQL query is returned.

3. **Data Fetching Tool**: The `FetchMysqlDataTool` allows you to execute SQL queries on a MySQL database and retrieve data based on the provided SQL query. It establishes a database connection and returns the query results as a response.

4. **Database Connection**: The script establishes a MySQL database connection using the provided credentials (host, port, user, password, and database name).

## Usage

To use this tool:

- Set up your environment variables by providing your OpenAI API key and configuring the MySQL database connection parameters.

- Run the script, which demonstrates the usage of both tools:
  - The `MysqlQueryBuilderTool` converts a natural language query into a SQL query.
  - The `FetchMysqlDataTool` executes the SQL query and retrieves data from the MySQL database.
  - The results of the SQL query are displayed as a response.

