from bs4 import BeautifulSoup
import collections
import math


def duplicate_id_check(page_text, url):
    '''
    Checking if same ID is used on more than one element.
    Priority 1 - A (https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of duplicate ids.
    '''
    error_text = "Duplicate id - the same ID is used on more than one element."
    guideline = "WCAG 2.0 A 4.1.1"
    guideline_link = "https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses"

    soup = BeautifulSoup(page_text, "html.parser")

    ids = [a.attrs['id'] for a in soup.find_all(attrs={'id': True})]
    ids = collections.Counter(ids)

    duplicate_ids = [key for key, value in ids.items() if value > 1]

    if duplicate_ids:
        #xreturn [error_text, url, guideline, guideline_link, duplicate_ids]
        return [error_text, url, guideline, duplicate_ids]

    else:
        return None


def alt_in_img_elements_check(page_text):
    '''
    Checking if alt attribute is present on all img tags.
    (https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H37)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of image src without alt.
    '''
    soup = BeautifulSoup(page_text.text, "html.parser")

    img_tags = soup.find_all('img')
    empty_alt = []
    for img_tag in img_tags:
        if not img_tag.find('alt') or img_tag.find('alt') == "":
            empty_alt.append(img_tag['src'])

    return empty_alt


def open_in_new_window_src_check(page_text):
    '''
    Checking <a> tags that open in new window/tab.
    (https://www.w3.org/TR/WCAG20-TECHS/F22.html)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of <a> tags with target='_blank'.
    Check for buttons as well.
    '''
    soup = BeautifulSoup(page_text.text, "html.parser")

    a_tags = soup.find_all('a')
    a_new_window = []
    for a_tag in a_tags:
        if a_tag.find('target') == '_blank':
            a_new_window.append(a_tag['src'])

    return a_new_window


def calculate_v(r, g, b):
    for v in [r, g, b]:
        v /= 255
        if (v <= 0.03928):
            return v / 12.92
        else:
            return math.pow((v + 0.055 / 1.055, 2.4))


def luminance(r, g, b):
    a = calculate_v(r, g, b)
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722

def contrast(rgb1, rgb2):
    lum1 = luminance(rgb1[0], rgb1[1], rgb1[2])
    lum2 = luminance(rgb2[0], rgb2[1], rgb2[2])
    brightest = math.max(lum1, lum2)
    darkest = math.min(lum1, lum2)
    return (brightest + 0.05) / (darkest + 0.05)
