{{ config(materialized='table') }}

SELECT DISTINCT
    InvoiceDate,
    Year,
    Month,
    Quarter,
    Weekday
FROM {{ ref('stg_retail') }}