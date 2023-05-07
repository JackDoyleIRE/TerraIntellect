-- models/staging/stg_projects.sql

{{
  config(
    materialized = 'view'
  )
}}

WITH source AS (
    SELECT * FROM {{ source('raw', 'projects') }}
)

SELECT
    project_id,
    client_id,
    project_name,
    project_description,
    start_date,
    end_date,
    status
FROM source