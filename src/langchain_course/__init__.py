import os

from dotenv import load_dotenv

load_dotenv()  # load the environment variable


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("GROQ_API_KEY"))


if __name__ == "__main__":
    main()
