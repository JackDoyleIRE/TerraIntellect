-- models/staging/stg_partners.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw', 'partners') }}
)

SELECT
  partner_id,
  partner_name,
  contact_name,
  contact_email,
  contact_phone,
  address,
  country,
  partnership_type
FROM source