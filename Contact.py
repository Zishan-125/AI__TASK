from bs4 import BeautifulSoup
import re

html_doc = """<html><body>Contact: zishan@gmail.com, Phone: 123-456-7890</body></html>"""
soup = BeautifulSoup(html_doc, 'html.parser')
text = soup.get_text()

emails = re.findall(r'\S+@\S+', text)
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)

print("Emails:", emails)
print("Phones:", phones)
