import os
from slugify import slugify

class RawHtmlPipeline:
    def open_spider(self, spider):
        os.makedirs('raw_infoboxes', exist_ok=True)

    def process_item(self, item, spider):
        base = slugify(item['url'])[:50]
        filename = f"raw_infoboxes/{base}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(item['infobox_html'])
        return item