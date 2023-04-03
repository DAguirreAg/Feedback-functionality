-- Create Feedback Database
CREATE DATABASE db_feedback_app;

-- Create tables
--- Feedback table
CREATE TABLE feedback (
	id SERIAL PRIMARY KEY,
	email VARCHAR,
	created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    feedback VARCHAR NOT NULL
);
