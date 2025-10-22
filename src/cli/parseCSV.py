from src.libs.OlxScrapper.OlxScrapper import OlxScrapper
import csv

def main() -> None:
    print('starting scrapper...')
    scrapper = OlxScrapper()
    scrapper.start()
    sections = scrapper.handle_pages(1)
    items = scrapper.handle_imoveis_sections(sections=sections)
    scrapper.end()
    print('scrapper finished.')
    with open('imoveis_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'City', 'District', 'Publish Date', 'Area', 'Parking Spaces', 'Bathrooms', 'Bedrooms'])
        for item in items:
            writer.writerow([
                item.title,
                item.price,
                item.city,
                item.district,
                item.publish_date,
                item.area,
                item.parking_spaces,
                item.bathrooms,
                item.bedrooms
            ])
if __name__ == "__main__":
    main()