{{
  config(
    materialized = 'view'
  )
}}

SELECT
    sales.sale_id,
    sales.client_id,
    sales.project_id,
    sales.sale_amount,
    sales.sale_date,
    sales.payment_status
FROM {{ ref('stg_sales') }} sales

LEFT JOIN {{ ref('stg_clients') }} clients

ON clients.client_id = sales.client_id



