import os
from slugify import slugify
from bs4 import BeautifulSoup
import re

class RawHtmlPipeline:
    def open_spider(self, spider):
        os.makedirs('raw_infoboxes', exist_ok=True)

    def process_item(self, item, spider):
        # Parse the HTML
        soup = BeautifulSoup(item['infobox_html'], 'lxml')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text and clean it
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # Remove empty lines
        text = re.sub(r'\n\s*\n', '\n', text)
        
        # Save the cleaned text
        base = slugify(item['url'])[:50]
        filename = f"raw_infoboxes/{base}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        return item