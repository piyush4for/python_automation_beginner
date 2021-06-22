#get flipkart price
import bs4, requests

# def getFlipkartPrice(productUrls):
#     res=requests.get(productUrls)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     productName =   soup.select('.B_NuCI')[0].text
#     mrp = soup.select('._30jeq3')[0].text
#     return (productName +'. \n\n\nPrice:'+ mrp)

def getAmazonPrice(productURL):
    res = requests.get(productURL, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })
 
    res.raise_for_status()
 
    soup1 = bs4.BeautifulSoup(res.text, 'html.parser')
    soup2 = bs4.BeautifulSoup(soup1.prettify(), "html.parser")
 
    elems = soup2.find(id='priceblock_ourprice').get_text()
 
    return elems.strip()

# price = getFlipkartPrice('https://www.flipkart.com/lenovo-legion-core-i5-9th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-y540-15irh-pg0-laptop/p/itma9b76ed1e879a?pid=COMG26R93HDJYBT5&lid=LSTCOMG26R93HDJYBT5CJXNFC&marketplace=FLIPKART&q=lenovo+legion+y540+9th+i5+laptop&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&fm=SEARCH&iid=9a68097b-df76-4dca-ab16-5c9d5a1797c7.COMG26R93HDJYBT5.SEARCH&ppt=sp&ppn=sp&ssid=s2fej8hx9c5vvbpc1624294558661&qH=478227e97e4e4197')
price = getAmazonPrice('https://www.amazon.in/Lenovo-Legion-Windows-Graphics-81SY00SNIN/dp/B087D4X9JG/ref=sr_1_1?dchild=1&qid=1624344928&refinements=p_89%3ALenovo&s=computers&sr=1-1&th=1')
print('The price  \n'+ price)  

