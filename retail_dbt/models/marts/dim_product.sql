{{ config(materialized='table') }}

SELECT DISTINCT
    StockCode,
    Description,
    Price
FROM {{ ref('stg_retail') }}
WHERE StockCode IS NOT NULL