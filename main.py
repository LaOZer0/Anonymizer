from gen import Anonymize
from db import generate_fake_database

if __name__ == "__main__":
    generate_fake_database()
    Anonymize("result.csv")
