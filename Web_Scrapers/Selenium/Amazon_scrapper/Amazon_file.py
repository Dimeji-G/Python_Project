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

# the code has been removed for confidential reasons, message the creator here
# 
#
#or on whatsapp or Upwork for work details
#+2348078595543
#

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
  #
#Censored
 #                       #

                        3
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
