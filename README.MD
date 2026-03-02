# Sales Analytics Pipeline – Supermarket Sales

This project implements an ETL (Extract, Transform, Load) pipeline and performs data analysis on supermarket sales using Python, Pandas, SQLite3, and SQL. The main goal is to demonstrate the process of extracting, transforming, and loading data into a relational database, followed by insightful sales analysis.

## About the Dataset

-Source: [Supermarket Sales - Kaggle](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

Columns:

-Invoice ID

-Branch

-City

-Customer type

-Gender

-Product line

-Unit price

-Quantity

-Tax 5%

-Sales

-Date

-Time

-Payment

-COGS

-Gross margin percentage

-Gross income

-Rating

## Functionalities
-ETL Pipeline

-Extract: Read CSV data

-Transform: Clean and rename columns

-Load: Model and populate tables in SQLite:

-city

-branch

-product_line

-sales

## Data Analysis
-Monthly revenue

-Performance by payment method

-Revenue by city

-Products sold by gender

-Revenue by customer membership type

-Sales distribution by time of day

-Revenue by product


Python – scripting and analysis

Pandas – data manipulation

SQLite3 & SQL – database modeling and querying

## Objective

The project demonstrates  a complete data pipeline, from raw CSV extraction to structured data loading and analytical insights, providing a practical example of sales analytics.

## Commands / How to use

|               |               |
| ------------- |:-------------:|
| Install dependencies      | `pip install -r requirements.txt`     |
| Run pipeline      | `python src/main.py`     |
| Open Jupyter Notebook      | `jupyter notebook notebooks/`    |
| Run with Docker      | `docker compose up`     |
| Run with Docker (pipeline only)      | `docker compose up pipeline`     |
| Run with Docker (Jupyter only)     | `docker compose up jupyter`     |
