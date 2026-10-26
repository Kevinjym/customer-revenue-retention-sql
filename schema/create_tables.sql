
-- Customer Revenue & Retention Analytics
-- Database: retail_analytics
-- Schema: public

-- Raw transaction table
-- Preserves source records before data cleaning.

CREATE TABLE public.raw_transactions (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(30),
    description TEXT,
    quantity INTEGER,
    invoice_date TIMESTAMP,
    unit_price NUMERIC(12, 4),
    customer_id BIGINT,
    country VARCHAR(100)
);
