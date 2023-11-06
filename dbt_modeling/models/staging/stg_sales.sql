-- models/staging/stg_sales.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw_erp_data', 'sales') }}
)

SELECT
    sale_id,
    client_id,
    project_id,
    sale_amount,
    sale_date,
    payment_status
FROM source