from bs4 import BeautifulSoup

class DataConverter:

    @staticmethod
    def clear_html(html):
        clean_text = []
        for item in html:
            item = BeautifulSoup(item, "html.parser").get_text()
            clean_text.append(item)
        return clean_text
