import pandas as pd
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)

df = pd.read_excel('cik_list.xlsx')
df['SECFNAME_complete'] = 'https://www.sec.gov/Archives/' + df['SECFNAME'].astype(str)


def get_report(url):
    reports_list = []
    report_paragraphs = []
    driver.get(url)
    time.sleep(2)
    report = driver.find_elements_by_xpath('//pre')

    for paras in report:
        report_paragraphs.append(paras.text)

    reports_list.append(report_paragraphs)
    return reports_list


df['reports'] = df['SECFNAME_complete'].apply(lambda x: get_report(x))
driver.close()
#df.head()
df.to_excel('SEC_with_reports.xlsx')
#print(df.head())
