{{ config(materialized='table') }}

SELECT DISTINCT
    Customer_ID,
    Country
FROM {{ ref('stg_retail') }}
WHERE Customer_ID IS NOT NULL