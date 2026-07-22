{{ config(materialized='table') }}

SELECT
    Invoice,
    Customer_ID,
    StockCode,
    Description,
    Quantity,
    Price,
    TotalPrice,
    InvoiceDate,
    Country,
    Year,
    Month,
    Quarter,
    Weekday
FROM {{ ref('stg_retail') }}