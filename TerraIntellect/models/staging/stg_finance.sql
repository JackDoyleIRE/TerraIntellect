-- models/staging/stg_sales.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw', 'finance') }}
)

SELECT
  finance_id,
  transaction_type,
  amount,
  transaction_date,
  transaction_category,
  transaction_description,
  related_id
FROM source