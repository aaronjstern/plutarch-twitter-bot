from tablescraper import TableScraper
from contesttext import ContestText
from tweetpollfunc import tweet_poll

CHROME_FILE_PATH = "/Users/aaronstern/PycharmProjects/twitterbot/chromedriver"
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Parallel_Lives"

parallel_lives_table = TableScraper(WIKIPEDIA_URL, ('Greek', 'Life'), ('Roman', 'Life'))

parallel_lives_list = parallel_lives_table.table_list

parallel_lives_info = ContestText(CHROME_FILE_PATH, WIKIPEDIA_URL, parallel_lives_list)

parallel_lives_dict = parallel_lives_info.contestants_dict

tweet_poll(CHROME_FILE_PATH, parallel_lives_list, parallel_lives_dict)
























