from flask import Flask, render_template
from selenium import webdriver

app = Flask(__name__)

@app.route('/',methods =["GET", "POST"])
def index():
    global name,profile_img
    return render_template('index.html',name=name,profile_img=profile_img)

driver = webdriver.Chrome("chromedriver.exe")
#Link to NFT
driver.get("https://opensea.io/assets/0x5283fc3a1aac4dac6b9581d3ab65f4ee2f3de7dc/765")
#Name of owner
nm=driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div/section[2]/div/div/a")
global name,profile_img,nftsc,nfts
name=str(nm.text)
nm.click()
#Logo
while True:
    try:
        lg=driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[1]/div[3]/div[1]/div/div/img")
        break
    except:
        continue
profile_img=lg.get_attribute("src")
app.run()
