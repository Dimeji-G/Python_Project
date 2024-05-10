#================================================Imported Modules=================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
import pyshorteners
import time
import pandas as pd
import math
#===========================================Headers=============================================
option = Options()
option.add_argument("start-maximized")
#option.add_argument("--headless")
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_argument('log-level=3')
driver = webdriver.Chrome(options=option)
s = pyshorteners.Shortener()
review_data = []
total_time_next_page_was_clicked = 0
df_reviews = pd.DataFrame(columns=['Asin', 'Product Link', 'Shortened URL', 'Reviewer', 'rating', 'Review Title', 'Review', 'Reviewed In', 'Review Date', 'People Found This Useful', 'Verified Purchaser'])
url_link = "https://www.amazon.sa/-/en/gp/bestsellers/electronics/?ie=UTF8&ref_=sv_sv_elec_all_1"
sleep_timer = 2
#sleep_timer = input("How long do you want the timer to sleep: ")
#===========================================Main_Code=============================================
while True:
    for category_selector in range(1,52):    
        try:
            driver.get(url_link)
            if category_selector == 7:
                continue
            #time.sleep(5000)
            test1 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[{category_selector}]')
            test1.click()
        except:
            print('[+] invalid link type')

        try:
            #Front_List_Item_Page
            asin_tag = driver.find_element(By.ID, "title_feature_div")
            asin = asin_tag.get_attribute("data-csa-c-asin")
            product_link = driver.current_url
            try:
                shortened_url = s.tinyurl.short(product_link)
            except:
                shortened_url = product_link
            product_title_tag = driver.find_element(By.ID, 'productTitle')
            product_title = product_title_tag.text
            try:
                In_Stock = driver.find_element(By.ID, 'availability').text
            except:
                In_Stock = 'Out_Of_Stock'
            average_product_rating_number = driver.find_element(By.XPATH, '//*[@id="cm_cr_dp_d_rating_histogram"]/div[2]/div/div[2]/div/span/span').text.split('out')[0]
            buying_history = driver.find_element(By.ID, 'social-proofing-faceout-title-tk_bought').text
            total_ratings_with_comment = driver.find_element(By.XPATH, '//*[@id="cm_cr_dp_d_rating_histogram"]/div[3]/span').text.split('global')[0]
            five_star_rating = driver.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a').text
            four_star_rating = driver.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a').text    
            three_star_rating = driver.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a').text
            two_star_rating = driver.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a').text    
            one_star_rating = driver.find_element(By.XPATH, '//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a').text  
            try:
                full_list_price = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[10]/div[17]/div/div/div[3]/div[2]/span/span[1]/span[2]').text.replace('\n', " ")
            except:
                full_list_price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]').text
            try:
                discounted_price = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[7]/div[8]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[1]/div/div').text.replace('\n', '.')
            except:
                discounted_price = 0
            try:
                discount_percentage = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[10]/div[17]/div/div/div[3]/div[1]/span[2]').text
            except:
                discount_percentage = 0
            try:
                free_delivery = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[7]/div[8]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[3]/div[10]/div[1]/div/div/div/span/a').text
            except:
                free_delivery = 'No'
            try:
                free_return = driver.find_element(By.ID, 'freeReturns_feature_div').text
            except:
                free_return = 'No'
            try:
                ships_from = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[7]/div[8]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[20]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/span').text
            except:
                ships_from = 'n/a'
            try:
                sold_by = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[7]/div[8]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[20]/div[1]/div/div[1]/div[1]/div[3]/div[2]/div/span').text
            except:
                sold_by = 'n/a'
            try:
                payment = driver.find_element(By.XPATH, '//*[@id="dynamicSecureTransactionFeature_feature_div"]/div[2]/span/a/span').text
            except:
                payment = 'n/a'
            try:
                brand = driver.find_element(By.XPATH, '//*[@id="poExpander"]/div[1]/div/table/tbody/tr[1]/td[2]/span').text
            except:
                brand = 'n/a'
            get_it_b_tomorrow = 'n/a' 
            main_category = 'n/a'
            sub_category = 'n/a'
            product_description = 'n/a'
            weight = 'n/a'
            condition = 'n/a'
            product_dimension = 'n/a'

            #ITEMS PRINTING
            # Create an empty DataFrame to store product details
            item_product = pd.DataFrame(columns=['ASIN', 'Product Link', 'Shortened URL', 'Product Title', 'In Stock', 'Average Product Rating', 
                                                'Buying History', 'Total Ratings with Comments', 'Five Star Rating', 'Four Star Rating', 
                                                'Three Star Rating', 'Two Star Rating', 'One Star Rating', 'Full List Price', 
                                                'Discounted Price', 'Discount Percentage', 'Free Delivery', 'Free Return', 
                                                'Ships From', 'Sold By', 'Payment', 'Brand', 'Get It By Tomorrow', 
                                                'Main Category', 'Sub Category', 'Product Description', 'Weight', 'Condition', 
                                                'Product Dimension'])

            # Append product details to the DataFrame
            item_product = item_product._append({
                'ASIN': asin,
                'Product Link': product_link,
                'Shortened URL': shortened_url,
                'Product Title': product_title,
                'In Stock': In_Stock,
                'Average Product Rating': average_product_rating_number,
                'Buying History': buying_history,
                'Total Ratings with Comments': total_ratings_with_comment,
                'Five Star Rating': five_star_rating,
                'Four Star Rating': four_star_rating,
                'Three Star Rating': three_star_rating,
                'Two Star Rating': two_star_rating,
                'One Star Rating': one_star_rating,
                'Full List Price': full_list_price,
                'Discounted Price': discounted_price,
                'Discount Percentage': discount_percentage,
                'Free Delivery': free_delivery,
                'Free Return': free_return,
                'Ships From': ships_from,
                'Sold By': sold_by,
                'Payment': payment,
                'Brand': brand,
                'Get It By Tomorrow': get_it_b_tomorrow,
                'Main Category': main_category,
                'Sub Category': sub_category,
                'Product Description': product_description,
                'Weight': weight,
                'Condition': condition,
                'Product Dimension': product_dimension
            }, ignore_index=True)

            # Save the DataFrame to a file
            item_product.to_excel(f'{product_title} Item.xlsx', index=False)
            print("[+] Product details saved to item.xlsx")

            # Clear the df_reviews DataFrame before scraping reviews for a new product
            df_reviews = pd.DataFrame(columns=['Asin', 'Product Link', 'Shortened URL', 'Reviewer', 'rating', 'Review Title', 'Review', 'Reviewed In', 'Review Date', 'People Found This Useful', 'Verified Purchaser'])

            #Review_page_click()
            try:
                review_see_all = driver.find_element(By.XPATH, '//*[@id="cr-pagination-footer-0"]/a')
                review_see_all.click()
                # time.sleep(sleep_timer)

                #total number of comments then divide it by 10 to determine how many times to click the page
                try:
                    total_comment = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[4]/div').text.split(' ')[-3].replace(',', '')
                    click_count = math.ceil(int(total_comment) / 10)
                except:
                    click_count = 1000000000
                #Review_page
                ASIN = asin
                for _ in range(1, click_count):
                    for x in range(2,12):
                        try:
                            try:
                                PRODUCT_LINK = product_link
                                REVIEWER = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/div[1]/a/div[2]').text
                                CUSTOMER_RATING_TO_CLIENT = 'n/a'
                                REVIEW_TITLE = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/div[2]/a/span[2]').text
                                REVIEW = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/div[4]/span').text
                                REVIEWED_IN =  driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/span').text.split('on')[0][12:]
                                REVIEW_DATE = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/span').text.split('on')[1]
                                PEOPLE_F_T_USEFUL = 'n/a'
                                try:
                                    VERIFIED_PURCHASER = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/div[3]/span/a/span').text
                                except:
                                    VERIFIED_PURCHASER = 'n/a'                        
                                review_data.append({
                                        'Asin': [asin],
                                        'Product Link': [product_link],
                                        'Shortened URL': [shortened_url],
                                        'Reviewer': REVIEWER,
                                        'rating': CUSTOMER_RATING_TO_CLIENT ,
                                        'Review Title': REVIEW_TITLE,
                                        'Review': REVIEW,
                                        'Reviewed In': REVIEWED_IN,
                                        'Review Date': REVIEW_DATE,
                                        'People Found This Useful': PEOPLE_F_T_USEFUL,
                                        'Verified Purchaser': VERIFIED_PURCHASER
                                        })
                            except:
                                continue  
                        except Exception as e:
                            print(e)
                            continue
                    time.sleep(sleep_timer)
                    total_time_next_page_was_clicked += 10
                    df_reviews = df_reviews._append(pd.DataFrame(review_data), ignore_index=True)
                    #df_reviews = df_reviews(pd.DataFrame(review_data), ignore_index=True)
                    review_data = []
                    try:
                        NEXT_PAGE_BUTTON = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[12]/span/div/ul/li[2]/a').click()
                        time.sleep(sleep_timer)
                    except Exception as e:
#                        print("[+] All the reviews has been scraped successfuly] \n")
                        print(f"[+] Done scrapping all the reviews for {product_title}\n")
                        pass
                        break
                    

                df_reviews.to_excel(f'{product_title} review_data.xlsx', index=False)
                
                
            except:
                print('No comment available')
        except Exception as e:
            print("[+] Link cotains ads preventing scrapping \n", e)

    try:
        driver.get(url_link)
        print('\n[+] Successfully Scapped the first 50 items on the first page')
        full_page_next_button = driver.find_element(By.CLASS_NAME, 'a-last')
        full_page_next_button.click()
        url_link = driver.current_url
    except:
        break