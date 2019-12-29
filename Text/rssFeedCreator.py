"""
Date: 2019-12-23
Purpose: Given a link to an RSS feed, program will get all posts and display them.
Author: Zach Archibald
"""


try:
    import feedparser
except ImportError:
    print("Error: please install feedparser -- 'pip install feedparser'")
    exit()


def main():
    rss_link = input("Please provide RSS link: ").split()[0]
    feed = feedparser.parse(rss_link)

    entries = feed.entries
    total_entries = len(entries)

    if total_entries == 0:
        print("No entries for this RSS feed.")
    else:
        print("Total Entries: " + str(total_entries))
        print("Entry Titles: ")

        for entry in entries:
            print(entry.title)


if __name__ == "__main__":
    main()
