from src.libs.OlxScrapper.OlxScrapper import OlxScrapper


def main() -> None:
    print('starting scrapper...')
    scrapper = OlxScrapper()
    scrapper.start()
    sections = scrapper.handle_test_post()
    items = scrapper.handle_imoveis_sections(sections=sections)
    for item in items:
        print(item)
    scrapper.end()
    print('scrapper finished.')

if __name__ == "__main__":
    main()