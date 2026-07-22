{{ config(materialized='view') }}

SELECT *
FROM {{ source('retail', 'RAW_RETAIL') }}