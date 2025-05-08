from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import schedule
import datetime

# Hàm khởi tạo driver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver

# Hàm lấy dữ liệu từ một trang
def get_data_from_page(driver, page):
    url = f"https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/3/da-nang/trang--{page}.html"
    print(f"Đang crawl trang {page}...")
    driver.get(url)
    time.sleep(2)

    titles = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[1]/div[1]/a')
    summaries = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[1]')
    dientich = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[3]/div[1]')
    addresses = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[2]')
    prices = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[1]')

    data = []
    # Lấy tất cả dữ liệu (Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá)
    for i in range(len(titles)):
        title = titles[i].text.strip() if i < len(titles) else ""
        summary = summaries[i].text.strip() if i < len(summaries) else ""
        price = prices[i].text.strip() if i < len(prices) else ""
        address = addresses[i].text.strip() if i < len(addresses) else ""
        dientich1 = dientich[i].text.strip() if i < len(dientich) else ""
        data.append([title, summary, dientich1, price, address])

    return data

# Lưu dữ liệu vào excel
def save_to_excel(data):
    today = datetime.datetime.now().strftime("%Y%m%d")
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Diện tích", "Giá", "Địa chỉ"])
    output_file = f"alonhadat_da_nang_{today}.xlsx"
    df.to_excel(output_file, index=False)
    print(f"✅ Đã lưu {len(data)} tin vào {output_file}")

# Crawl dữ liệu từ nhiều trang
def crawl_alonhadat():
    driver = init_driver()
    data = []
    page = 1

    while True:
        page_data = get_data_from_page(driver, page)
        if len(page_data) == 0:
            print(f"✅ Hết dữ liệu ở trang {page}. Dừng crawl.")
            break
        data.extend(page_data)
        page += 1

    driver.quit()
    save_to_excel(data)

# Chạy vào lúc 6h sáng mỗi ngày
def set_schedule():
    schedule.every().day.at("06:00").do(crawl_alonhadat)
    print("⏳ Đã lên lịch chạy lúc 6:00 sáng mỗi ngày. Ấn Ctrl+C để thoát.")
    while True:
        schedule.run_pending()
        time.sleep(60)

# Gọi hàm set lịch
set_schedule()
