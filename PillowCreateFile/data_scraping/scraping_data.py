# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time

# # # **Main Page URL**
# # MAIN_PAGE_URL = "https://mptc.gov.kh/officialdoc/#main"

# # # **Setup Chrome Driver**
# # options = Options()
# # options.add_argument("--headless")  # Run in headless mode
# # options.add_argument("--no-sandbox")
# # options.add_argument("--disable-dev-shm-usage")
# # options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # **Set the number of pages to scrape**
# # MAX_PAGES_TO_SCRAPE = 5  # Change this value to the number of pages you want to scrape

# # def get_document_links():
# #     """Extracts document links from the main page."""
# #     time.sleep(5)  # Wait for elements to load

# #     doc_links = []
# #     elements = driver.find_elements(By.XPATH, '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[3]/ul/li/div[2]/div/div[1]/div/a')

# #     for element in elements:
# #         text = element.text.strip()
# #         href = element.get_attribute("href")
        
# #         if href:
# #             doc_links.append((text, href))

# #     return doc_links

# # def extract_document_content(link):
# #     """Extracts the category, title, and main content from a document page."""
# #     driver.get(link)
# #     time.sleep(5)  # Ensure the page loads

# #     try:
# #         category_element = driver.find_element(By.XPATH, "//header/div[1]/span/a[2]")
# #         category = category_element.text.strip() if category_element else "N/A"
# #     except:
# #         category = "N/A"

# #     try:
# #         title_element = driver.find_element(By.XPATH, "//header/h1")
# #         title = title_element.text.strip() if title_element else "N/A"
# #     except:
# #         title = "N/A"

# #     try:
# #         content_element = driver.find_element(By.XPATH, '//*[@id="post-39270"]/div/div[2]')
# #         content = content_element.text.strip() if content_element else "N/A"
# #     except:
# #         content = "N/A"

# #     return category, title, content

# # def get_total_pages():
# #     """Finds the total number of pages dynamically."""
# #     driver.get(MAIN_PAGE_URL)
# #     time.sleep(5)  # Wait for page to load

# #     try:
# #         last_page_element = driver.find_elements(By.XPATH, '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div/a')
# #         if last_page_element:
# #             return int(last_page_element[-2].text)  # Second-last element is the last page number
# #     except:
# #         return 1  # Default to 1 if no pagination found

# #     return 1

# # # **Run the Scraper**
# # print("🔍 Extracting document links...")

# # total_pages = get_total_pages()
# # pages_to_scrape = min(total_pages, MAX_PAGES_TO_SCRAPE)  # Limit pages to scrape
# # print(f"\n📄 Found {total_pages} pages. Scraping up to {pages_to_scrape} pages.")

# # with open("extracted_documents.txt", "w", encoding="utf-8") as file:
# #     for page in range(1, pages_to_scrape + 1):
# #         print(f"\n📄 Scraping Page {page}/{pages_to_scrape}...")

# #         # **Go to Main Page before clicking pagination**
# #         driver.get(MAIN_PAGE_URL)
# #         time.sleep(5)

# #         # **Click on the correct page number button**
# #         if page > 1:
# #             try:
# #                 page_button_xpath = f'//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div/a[text()="{page}"]'
# #                 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, page_button_xpath))).click()
# #                 time.sleep(5)
# #             except:
# #                 print(f"🚫 Could not click on page {page}. Skipping...")
# #                 continue  # Skip to next page if click fails

# #         # **Get document links for this page**
# #         doc_links = get_document_links()

# #         if doc_links:
# #             print(f"✅ Extracted {len(doc_links)} links from Page {page}")

# #             for idx, (doc_title, doc_link) in enumerate(doc_links, 1):
# #                 print(f"Processing {idx}/{len(doc_links)}: {doc_title} -> {doc_link}")

# #                 category, title, content = extract_document_content(doc_link)

# #                 file.write(f"Category: {category}\n")
# #                 file.write(f"Title: {title}\n")
# #                 file.write(f"Content:\n{content}\n")
# #                 file.write("=" * 80 + "\n")  # Separator

# #         else:
# #             print(f"🚫 No documents found on Page {page}")

# # print("\n✅ Extraction completed! Check 'extracted_documents.txt'.")

# # # **Close the driver**
# # driver.quit()
# # print("\n✅ Debugging completed! Check the extracted data.")




# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time

# # # **Configurable Settings**
# # MAIN_PAGE_URL = "https://mptc.gov.kh/officialdoc/#main"
# # MAX_PAGES_TO_SCRAPE = 5  # Change this to control how many pages you want to scrape

# # # **Setup Chrome Driver**
# # options = Options()
# # #options.add_argument("--headless")  # Run in headless mode
# # options.add_argument("--no-sandbox")
# # options.add_argument("--disable-dev-shm-usage")
# # options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # def get_total_pages():
# #     """Finds the total number of pages dynamically."""
# #     driver.get(MAIN_PAGE_URL)
# #     time.sleep(5)  # Allow the page to load

# #     try:
# #         last_page_elements = driver.find_elements(By.XPATH, '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div/a')
# #         if last_page_elements:
# #             return int(last_page_elements[-2].text)  # Second-last element should be the last page number
# #     except:
# #         return 1  # Default to 1 if no pagination found

# #     return 1

# # def get_document_links():
# #     """Extract document links from the current page."""
# #     time.sleep(5)  # Allow page to load
# #     doc_links = []

# #     elements = driver.find_elements(By.XPATH, '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[3]/ul/li/div[2]/div/div[1]/div/a')
    
# #     for element in elements:
# #         text = element.text.strip()
# #         href = element.get_attribute("href")
# #         if href:
# #             doc_links.append((text, href))
    
# #     return doc_links

# # def extract_document_content(link):
# #     """Extracts the content dynamically from a document page."""
# #     driver.get(link)
# #     time.sleep(5)  # Ensure the page loads

# #     try:
# #         # **Extract Content Dynamically**
# #         content_element = driver.find_element(By.XPATH, "//article[contains(@id, 'post-')]//div[contains(@class, 'entry-content')]")
# #         content = content_element.text.strip() if content_element else "N/A"
# #     except:
# #         content = "N/A"

# #     return content

# # def go_to_page(page_num):
# #     """Clicks on the page number button to navigate."""
# #     try:
# #         page_xpath = f'//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div/a[text()="{page_num}"]'
# #         page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, page_xpath)))
# #         driver.execute_script("arguments[0].click();", page_button)
# #         time.sleep(5)  # Wait for the page to load
# #         return True
# #     except:
# #         print(f"🚫 Could not click on page {page_num}. Skipping...")
# #         return False

# # # **Run the Scraper**
# # print("🔍 Extracting document links...")

# # total_pages = get_total_pages()
# # pages_to_scrape = min(total_pages, MAX_PAGES_TO_SCRAPE)  # Limit pages to scrape
# # print(f"\n📄 Found {total_pages} pages. Scraping up to {pages_to_scrape} pages.")

# # with open("extracted_documents.txt", "w", encoding="utf-8") as file:
# #     for page in range(1, pages_to_scrape + 1):
# #         print(f"\n📄 Scraping Page {page}/{pages_to_scrape}...")

# #         # **Go to Main Page before clicking pagination**
# #         driver.get(MAIN_PAGE_URL)
# #         time.sleep(5)

# #         # **Click on the correct page number button**
# #         if page > 1:
# #             success = go_to_page(page)
# #             if not success:
# #                 break  # Stop if navigation fails

# #         # **Get document links for this page**
# #         doc_links = get_document_links()
# #         print(f"✅ Extracted {len(doc_links)} links from Page {page}")

# #         # **Add Page Break in the file**
# #         file.write(f"\n++++++++++Page {page}++++++++++\n\n")

# #         for idx, (doc_title, doc_link) in enumerate(doc_links, 1):
# #             print(f"Processing {idx}/{len(doc_links)}: {doc_title} -> {doc_link}")
# #             content = extract_document_content(doc_link)

# #             file.write(f"Title: {doc_title}\n")
# #             file.write(f"Content:\n{content}\n")
# #             file.write("=" * 80 + "\n")  # Separator

# # print("\n✅ Extraction completed! Check 'extracted_documents.txt'.")
# # driver.quit()

# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # **Configurable Settings**
# MAIN_PAGE_URL = "https://mptc.gov.kh/officialdoc/#main"
# OUTPUT_FOLDER = r"C:\Users\Admin\Desktop\DatasetTemplateGen\Scrape-MPTC"  # Folder to save extracted files

# # **Ensure output folder exists**
# if not os.path.exists(OUTPUT_FOLDER):
#     os.makedirs(OUTPUT_FOLDER)

# # **Setup Chrome Driver**
# options = Options()
# options.add_argument("--headless")  # Uncomment for headless mode
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

# # Start Chrome Driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # **User-defined page range**
# start_page = int(input("Enter the start page: "))
# end_page = int(input("Enter the end page: "))

# # **XPath Locations**
# PAGE_NAV_XPATH = '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div'
# DOC_LINK_XPATH = '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[3]/ul/li/div[2]/div/div[1]/div/a'
# NEXT_BUTTON_XPATH = f"{PAGE_NAV_XPATH}/a[contains(text(),'Next') or contains(text(),'បន្ទាប់')]"

# CATEGORY_XPATH = "//header/div[1]/span/a[2]"
# TITLE_XPATH = "//header/h1"
# CONTENT_XPATH = "//article[contains(@id, 'post-')]//div[contains(@class, 'entry-content')]"

# # **Helper function to extract document links**
# def get_document_links():
#     """Extracts document links from the current page."""
#     print("🔍 Searching for document links on the page...")
#     time.sleep(5)  # Allow page to load
#     doc_links = []

#     elements = driver.find_elements(By.XPATH, DOC_LINK_XPATH)

#     if not elements:
#         print("⚠️ No document links found on this page!")

#     for element in elements:
#         text = element.text.strip()
#         href = element.get_attribute("href")
#         if href:
#             doc_links.append((text, href))

#     print(f"✅ Found {len(doc_links)} document links.")
#     return doc_links

# # **Extract content from a document page**
# def extract_document_content(link):
#     """Extracts the category, title, and main content from a document page."""
#     print(f"🔎 Opening document: {link}")
#     driver.get(link)
#     time.sleep(5)  # Ensure the page loads

#     try:
#         category = driver.find_element(By.XPATH, CATEGORY_XPATH).text.strip()
#     except:
#         category = "N/A"

#     try:
#         title = driver.find_element(By.XPATH, TITLE_XPATH).text.strip()
#     except:
#         title = "N/A"

#     try:
#         content = driver.find_element(By.XPATH, CONTENT_XPATH).text.strip()
#     except:
#         content = "N/A"

#     return category, title, content

# def go_to_page(target_page, current_page=None):
#     """
#     Navigates to the target page.
#     If switching from a specific page, reload that page first to ensure pagination buttons are visible.
#     If target page is missing, it tries to use "Next" to shift pagination.
#     """
#     try:
#         print(f"🔹 Attempting to navigate to Page {target_page}...")

#         # **Step 1: Navigate to the closest page first**
#         if current_page and current_page != target_page:
#             print(f"🔄 Reloading Page {current_page} to find the button for Page {target_page}...")
#             driver.get(f"{MAIN_PAGE_URL}/?page={current_page}")
#         else:
#             print(f"🌍 Navigating to the main page: {MAIN_PAGE_URL}")
#             driver.get(MAIN_PAGE_URL)

#         time.sleep(5)  # Ensure page reloads

#         # **Step 2: Wait for pagination to load**
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, PAGE_NAV_XPATH)))

#         # **Step 3: Find all visible page buttons**
#         page_buttons = driver.find_elements(By.XPATH, f"{PAGE_NAV_XPATH}/a")

#         # **Step 4: Check if target page exists**
#         for button in page_buttons:
#             btn_text = button.text.strip()
#             print(f"🔍 Found page button: {btn_text}")  # Debugging output

#             if btn_text == str(target_page):  # Check if it's the target page
#                 driver.execute_script("arguments[0].scrollIntoView();", button)
#                 driver.execute_script("arguments[0].click();", button)
#                 time.sleep(5)  # Allow time for page to load
#                 print(f"✅ Successfully navigated to Page {target_page}\n")
#                 return True

#         # **Step 5: If the target page is missing, try clicking "Next" to reveal it**
#         print(f"🚫 Page {target_page} not found. Trying to click 'Next' to shift pagination...")

#         try:
#             next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
#             driver.execute_script("arguments[0].scrollIntoView();", next_button)
#             driver.execute_script("arguments[0].click();", next_button)
#             time.sleep(5)  # Allow pagination to shift

#             # **Re-check if the target page button is now visible**
#             page_buttons = driver.find_elements(By.XPATH, f"{PAGE_NAV_XPATH}/a")
#             for button in page_buttons:
#                 if button.text.strip() == str(target_page):
#                     driver.execute_script("arguments[0].scrollIntoView();", button)
#                     driver.execute_script("arguments[0].click();", button)
#                     time.sleep(5)
#                     print(f"✅ Successfully navigated to Page {target_page}\n")
#                     return True

#         except:
#             print(f"🚫 Page {target_page} still not found after clicking 'Next'. Skipping...\n")
#             return False

#         return False

#     except Exception as e:
#         print(f"🚫 Could not click on page {target_page}. Error: {str(e)}\n")
#         return False


# # **Run the Scraper**
# print("\n🔍 Extracting document links...\n")

# # **Go to the start page first**
# print(f"🌍 Navigating to the start page: {start_page}")
# go_to_page(start_page)

# for page in range(start_page, end_page + 1):
#     print(f"\n📄 Scraping Page {page}/{end_page}...")

#     # **Click on the correct page number button**
#     success = go_to_page(page, current_page=page - 1)  # Reload previous page before finding new button
#     if not success:
#         continue  # Skip if navigation fails

#     # **Get document links for this page**
#     doc_links = get_document_links()

#     if not doc_links:
#         print(f"⚠️ No documents found on Page {page}. Moving to the next page...\n")
#         continue  # Skip if no documents found

#     print(f"✅ Extracted {len(doc_links)} links from Page {page}")

#     # **Save each page result separately in the folder**
#     filename = os.path.join(OUTPUT_FOLDER, f"page_{page}_documents.txt")
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(f"\n++++++++++ Page {page} ++++++++++\n\n")

#         for idx, (doc_title, doc_link) in enumerate(doc_links, 1):
#             print(f"📜 Processing {idx}/{len(doc_links)}: {doc_title} -> {doc_link}")
#             category, title, content = extract_document_content(doc_link)

#             file.write(f"Category: {category}\n")
#             file.write(f"Title: {title}\n")
#             file.write(f"Content:\n{content}\n")
#             file.write("=" * 80 + "\n")  # Separator

#         print(f"✅ Finished scraping Page {page}. Data saved in {filename}.\n")

# print("\n✅ Extraction completed! Check the 'extracted_documents' folder for extracted data.")
# driver.quit()



#lastVersion
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# **Configurable Settings**
MAIN_PAGE_URL = "https://mptc.gov.kh/officialdoc/#main"
OUTPUT_FOLDER = r"C:\Users\Sreylen\Desktop\Intern_I5\CreateFile\Txt"

# **Ensure output folder exists**
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# **Setup Chrome Driver**
options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# **User-defined page range**
start_page = int(input("Enter the start page: "))
end_page = int(input("Enter the end page: "))

# **XPath Locations**
PAGE_NAV_XPATH = '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[4]/nav/div'
DOC_LINK_XPATH = '//*[@id="post-34256"]/div/div/div/div/div/div/div/div[3]/ul/li/div[2]/div/div[1]/div/a'
NEXT_BUTTON_XPATH = f"{PAGE_NAV_XPATH}/a[contains(text(),'Next') or contains(text(),'បន្ទាប់')]"

CATEGORY_XPATH = "//header/div[1]/span/a[2]"
TITLE_XPATH = "//header/h1"
CONTENT_XPATH = "//article[contains(@id, 'post-')]//div[contains(@class, 'entry-content')]"


def get_document_links():
    """Extracts document links from the current page."""
    print("🔍 Searching for document links on the page...")
    time.sleep(5)  # Allow page to load
    doc_links = []

    elements = driver.find_elements(By.XPATH, DOC_LINK_XPATH)

    if not elements:
        print("⚠️ No document links found on this page!")

    for element in elements:
        text = element.text.strip()
        href = element.get_attribute("href")
        if href:
            doc_links.append((text, href))

    print(f"✅ Found {len(doc_links)} document links.")
    return doc_links


def extract_document_content(link):
    """Extracts the category, title, and main content from a document page."""
    print(f"🔎 Opening document: {link}")
    driver.get(link)
    time.sleep(5)  # Ensure the page loads

    try:
        category = driver.find_element(By.XPATH, CATEGORY_XPATH).text.strip()
    except:
        category = "N/A"

    try:
        title = driver.find_element(By.XPATH, TITLE_XPATH).text.strip()
    except:
        title = "N/A"

    try:
        content = driver.find_element(By.XPATH, CONTENT_XPATH).text.strip()
    except:
        content = "N/A"

    return category, title, content


# def go_to_page(target_page, current_page=None):
    """Navigates to the target page efficiently, without unnecessary resets."""

    if current_page == target_page:
        print(f"✅ Already on Page {target_page}, no need to navigate.")
        return True

    print(f"🔹 Attempting to navigate to Page {target_page}...")

    # ✅ Go to the main page **only if not already close to the target page**
    if not current_page or abs(current_page - target_page) > 5:
        print(f"🌍 Going to main page first to reset pagination...")
        driver.get(MAIN_PAGE_URL)
        time.sleep(5)  # Ensure page loads fully

    # ✅ Ensure pagination is present
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, PAGE_NAV_XPATH)))
    except:
        print("⚠️ Pagination not found. Refreshing page and retrying...")
        driver.refresh()
        time.sleep(5)
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, PAGE_NAV_XPATH)))
        except:
            print("🚫 Failed to load pagination even after refresh. Stopping navigation.")
            return False

    while True:
        # Get all visible page buttons
        page_buttons = driver.find_elements(By.XPATH, f"{PAGE_NAV_XPATH}/a")
        available_pages = []

        for button in page_buttons:
            btn_text = button.text.strip()
            if btn_text.isdigit():
                available_pages.append(int(btn_text))

        if target_page in available_pages:
            # ✅ Click the exact target page
            for button in page_buttons:
                if button.text.strip() == str(target_page):
                    driver.execute_script("arguments[0].scrollIntoView();", button)
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(5)
                    print(f"✅ Successfully navigated to Page {target_page}")
                    return True
        else:
            # ✅ Find the closest available page **less than** or **equal to** the target page
            closest_available = max([p for p in available_pages if p <= target_page], default=None)

            if closest_available:
                print(f"➡️ Navigating to closest available page {closest_available} before trying {target_page} again...")
                for button in page_buttons:
                    if button.text.strip() == str(closest_available):
                        driver.execute_script("arguments[0].scrollIntoView();", button)
                        driver.execute_script("arguments[0].click();", button)
                        time.sleep(5)
                        break  # ✅ Break out and retry checking for the target page
            else:
                # ✅ If no closer page is found, try using the 'Next' button **ONLY IF NEEDED**
                print(f"🚫 Page {target_page} not found. Trying 'Next' to shift pagination...")
                try:
                    next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(5)
                except:
                    print(f"🚫 Could not find next button. Stopping navigation.")
                    return False

def go_to_page(target_page, current_page=None):
    """Navigates to the target page efficiently, ensuring pagination is correctly loaded before proceeding."""
    print(f"🔹 Attempting to navigate to Page {target_page}...")

    # ✅ Ensure the script resets to the main page if necessary
    if not current_page or abs(current_page - target_page) > 5:
        print(f"🌍 Going to the main page first to reset pagination...")
        driver.get(MAIN_PAGE_URL)
        time.sleep(5)  # Allow the page to load

    # ✅ Reload the main page of the target page first before checking pagination
    print(f"🔄 Ensuring we are on the correct main list page for Page {target_page}...")
    driver.get(f"{MAIN_PAGE_URL}?page={target_page}")  # Force navigation to page list
    time.sleep(5)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, PAGE_NAV_XPATH)))
    except:
        print(f"⚠️ Pagination not found on Page {target_page}. Refreshing page and retrying...")
        driver.refresh()
        time.sleep(5)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, PAGE_NAV_XPATH)))
        except:
            print(f"🚫 Failed to load pagination even after refresh. Stopping navigation.")
            return False

    while True:
        # Get all visible page buttons
        page_buttons = driver.find_elements(By.XPATH, f"{PAGE_NAV_XPATH}/a")
        available_pages = []

        for button in page_buttons:
            btn_text = button.text.strip()
            if btn_text.isdigit():
                available_pages.append(int(btn_text))

        if target_page in available_pages:
            # ✅ Click the exact target page
            for button in page_buttons:
                if button.text.strip() == str(target_page):
                    driver.execute_script("arguments[0].scrollIntoView();", button)
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(5)
                    print(f"✅ Successfully navigated to Page {target_page}")
                    return True
        else:
            # ✅ Find the closest available page **less than** or **equal to** the target page
            closest_available = max([p for p in available_pages if p <= target_page], default=None)

            if closest_available:
                print(f"➡️ Navigating to closest available page {closest_available} before trying {target_page} again...")
                for button in page_buttons:
                    if button.text.strip() == str(closest_available):
                        driver.execute_script("arguments[0].scrollIntoView();", button)
                        driver.execute_script("arguments[0].click();", button)
                        time.sleep(5)
                        break  # ✅ Break out and retry checking for the target page
            else:
                # ✅ If no closer page is found, try using the 'Next' button **ONLY IF NEEDED**
                print(f"🚫 Page {target_page} not found. Trying 'Next' to shift pagination...")
                try:
                    next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(5)
                except:
                    print(f"🚫 Could not find next button. Stopping navigation.")
                    return False

# **Track the current page**
current_page = None

print("\n🔍 Extracting document links...\n")

# ✅ Navigate to the start page **only ONCE**
if go_to_page(start_page, current_page):
    current_page = start_page  # Update tracker

# ✅ Scrape pages without reloading the main page unnecessarily
for page in range(start_page, end_page + 1):
    print(f"\n📄 Scraping Page {page}/{end_page}...")

    # ✅ Only navigate if we are not already on the correct page
    if page != current_page and go_to_page(page, current_page):
        current_page = page  # Update tracker

    # ✅ Get document links for this page
    doc_links = get_document_links()
    if not doc_links:
        print(f"⚠️ No documents found on Page {page}. Moving to the next page...\n")
        continue

    print(f"✅ Extracted {len(doc_links)} links from Page {page}")

    # ✅ Save results
    filename = os.path.join(OUTPUT_FOLDER, f"page_{page}_documents.txt")
    with open(filename, "w", encoding="utf-8") as file:
        for idx, (doc_title, doc_link) in enumerate(doc_links, 1):
            print(f"📜 Processing {idx}/{len(doc_links)}: {doc_title} -> {doc_link}")
            category, title, content = extract_document_content(doc_link)

            file.write(f"Category: {category}\nTitle: {title}\nContent:\n{content}\n")
            file.write("=" * 80 + "\n")  # Separator

    print(f"✅ Finished scraping Page {page}. Data saved in {filename}.\n")

    # ✅ Return to the main page of the current page before going to the next one
    if page < end_page:
        print(f"🔄 Returning to Page {page} before navigating to the next one...")
        go_to_page(page, current_page)

print("\n✅ Extraction completed! Check the 'Scrape-MPTC' folder for extracted data.")
driver.quit()

