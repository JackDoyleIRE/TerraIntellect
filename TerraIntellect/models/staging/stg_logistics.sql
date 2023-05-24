-- models/staging/stg_logistics.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw', 'logistics') }}
)

SELECT
    logistics_id,
    project_id,
    drone_id,
    sensor_id,
    location,
    data_collection_start,
    data_collection_end,
    data_size,
    transport_method
FROM source