-- models/staging/stg_clients.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw', 'clients') }}
)

SELECT
    client_id,
    client_name,
    contact_email,
    contact_phone,
    address,
    country
FROM source
