CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO transactions (user_id, amount, status)
SELECT 
    (random() * 9999 + 1)::INT AS user_id,
    round((random() * (50000000 - 1000) + 1000)::numeric, 2) AS amount,
    (ARRAY['pending', 'success', 'failed'])[floor(random() * 3) + 1] AS status
FROM generate_series(1, 3000);
CREATE UNIQUE INDEX IF NOT EXISTS transactions_idx ON transactions (id); 
ALTER TABLE transactions REPLICA IDENTITY USING INDEX transactions_idx;