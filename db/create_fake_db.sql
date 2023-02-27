CREATE TABLE IF NOT EXISTS users(
  id INT PRIMARY KEY,
  firstname TEXT NOT NULL,
  middlename TEXT NOT NULL,
  lastname TEXT,
  sex INT,
  snils TEXT NOT NULL,
  email TEXT NOT NULL
)
