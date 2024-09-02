import sys
import logging


"""
# Set up logging
logging.basicConfig(
    filename='logs/app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
"""


def main(movie_title):
    """
    Main function to scrape movie reviews and perform sentiment analysis.
    """


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <movie_title>")
        sys.exit(1)

    movie_title = sys.argv[1]
    main(movie_title)