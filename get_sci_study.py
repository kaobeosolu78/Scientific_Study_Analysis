import bs4,requests
from selenium import webdriver
import pickle
from Study import study,studies,load_obj

def get_study_page(kw):
    chromedriver = ('C:\\Users\\Kaobe\\PycharmProjects\\School\\venv\\Include\\chromedriver.exe')
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.ncbi.nlm.nih.gov/pmc/?term={}".format(kw))
    # # driver.find_element_by_link_text("20 per page,").click()
    # # driver.find_element_by_id("ps100").click()
    links = [tlink.find_element_by_tag_name("a").get_attribute("href") for tlink in driver.find_elements_by_class_name("title")]
    content,header = studies(kw),{'User-Agent': 'Mozilla/5.0'}


    for link in links:
        rawstudy = requests.get(link,headers=header)
        studysoup = bs4.BeautifulSoup(rawstudy.text,"html.parser")
        temp = {}
        for item in studysoup.findAll("div",{"class":"tsec sec"}):
            title = item.find("h2").text
            temp[title] = item.text.lstrip(title)
        content.add_study(study(studysoup.find("h1",{"class":"content-title"}).text,temp))

    pick_out = open("{}.pkl".format(kw), "wb")
    pickle.dump(content, pick_out, pickle.HIGHEST_PROTOCOL)
    pick_out.close()
    return content
get_study_page("weed")

med = load_obj("tobacco")
print("")