import bs4,requests
from selenium import webdriver
import pickle
from Study import study,studies,load_obj

def get_study_page(kw):
    chromedriver = ('C:\\Users\\Kaobe\\PycharmProjects\\School\\venv\\Include\\chromedriver.exe')
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://clinicaltrials.gov/ct2/results?cond=breast&Search=Apply&recrs=e&age_v=&gndr=&type=&rslt=")