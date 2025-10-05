from src.libs.OlxScrapper.OlxScrapper import OlxScrapper


def main() -> None:
    print('starting scrapper...')
    scrapper = OlxScrapper()
    scrapper.start()
    print('scrapper finished.')


if __name__ == "__main__":
    main()