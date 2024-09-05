import time
from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import traceback
import sys
# from datetime import datetime
import os


class G2GListerBot:
    def __init__(self, profile: str):
        self.game_dict = {
            "Valorant": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_27301&sort=most_recent",
                "enter_details": self.enter_valorant_details,
                "check": self.check_valorant,
            },
            "Overwatch (Global)": {
                "delete_url" : "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_21555&sort=most_recent",
                "enter_details": self.enter_overwatch_global,
                "check": self.check_valorant
            },
            "Overwatch 2": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_30675&sort=most_recent",
                "enter_details": self.enter_overwatch2,
                "check": self.check_platform,
            },
            "League of Legends" : {
                "delete_url" : "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_22666&sort=most_recent",
                "enter_details" : self.enter_league_of_legends,
                "check" : self.check_Lol,
            },
            "Counter-Strike 2": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=22539&type=1",
                "enter_details": self.enter_cs2_details,
                "check": self.check_counter_strile,
            },
            "Tom Clancys Rainbow Six Siege": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_24713&sort=most_recent",
                "enter_details": self.enter_rainbow_six,
                "check": self.check_rocket_league,
            },
            "Call of Duty": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=4644&type=1",
                "enter_details": self.enter_cod_details,
                "check": self.check_valorant,
            },
            "COC": {"delete_url": "", "enter_details": "", "check": ""},
            "FN": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_24742&sort=most_recent",
                "enter_details": self.enter_FN,
                "check": self.check_rocket_league,
            },
            "GTA 5 Online": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_24309&sort=most_recent",
                "enter_details": self.enter_GTA_5,
                "check": self.check_gta_5_online,
            },
            "Genshin Impact": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=28151&type=1",
                "enter_details": self.enter_sea_of_thieves_details,
                "check": self.check_platform,
            },
            "Hay Day (Global)": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=20347&type=1",
                "enter_details": self.enter_sea_of_thieves_details,
                "check": self.check_platform,
            },
            "Honkai: Star Rail": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=32116&type=1",
                "enter_details": self.enter_honkai_details,
                "check": self.check_honkai,
            },
            "Mobile Legends": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=23957&type=1",
                "enter_details": self.enter_platform_details,
                "check": self.check_platform,
            },
            "One Piece Bounty Rush": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=25705&type=1",
                "enter_details": self.enter_platform_details,
                "check": self.check_rocket_league,
            },
            "Apex Legends": {
                "delete_url": "https://www.g2g.com/offers/list?cat_id=5830014a-b974-45c6-9672-b51e83112fb7&brand_id=lgc_game_25694&sort=most_recent",
                "enter_details": self.enter_apex_legends,
                "check": self.check_rocket_league,
            },
            "PUBG Mobile": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=24937&type=1",
                "enter_details": self.enter_platform_details,
                "check": self.check_rocket_league,
            },
            "Rocket League": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=23797&type=1",
                "enter_details": self.enter_sea_of_thieves_details,
                "check": self.check_rocket_league,
            },
            "Summoners War": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=22779&type=1",
                "enter_details": self.enter_summoners_war,
                "check": self.check_summoners_war,
            },
            "DayZ": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=26784&type=1",
                "enter_details": self.enter_platform_details,
                "check": self.check_rocket_league,
            },
            "Dota 2": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=22664&type=1",
                "enter_details": self.enter_dota2_details,
                "check": self.check_dota2,
            },
            "Sea of Thieves": {
                "delete_url": "https://www.g2g.com/sell/manage?service=5&game=24939&type=1",
                "enter_details": self.enter_sea_of_thieves_details,
                "check": self.check_rocket_league,
            },
        }

        self.game = ""
        self.game_details = []
        self.profile = profile
        self.file_path = f'C:\\Users\\BABAR\\Desktop\\g2g_all_games_listing_bot_modified\\{profile}.xlsx'
        self.wait = WebDriverWait(self, 30)

        self.df = pd.read_excel(self.file_path, na_filter=False, engine="openpyxl")
        self.df["Delete"] = self.df["Delete"].astype("bool")
        self.df["Done"] = self.df["Done"].astype("bool")
        self.options = Options()
        # self.options.add_argument("--headless=new")
        self.options.add_argument("start-maximized")
        self.options.add_argument("--dns-prefetch-disable")
        self.options.add_argument("enable-automation")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage") 
        self.options.add_argument("--disable-browser-side-navigation") 
        self.options.add_argument("--disable-gpu")
        self.options.add_argument('log-level=3')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.page_load_strategy = "none"
        self.options.add_argument(
            f"--user-data-dir=C:\\Users\\BABAR\\Desktop\\Profiles\\{self.profile} User Data"
        )
        self.options.add_argument(f"--profile-directory={self.profile}")

        # Chrome.__init__(self, service=Service(ChromeDriverManager().install()), options=options)
        self.driver = Chrome(service=Service(r"C:\Users\BABAR\Desktop\chromedriver-win64\chromedriver.exe"), options=self.options)
        self.driver.implicitly_wait(10)
        # self.last_start_time = time.time()
        # print(self.page_source)

    def check_gta_5_online(self,listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td//div[contains(@class,'products__main-info-right')]//span"
            ).text.strip()
            == game_details[0]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[1]/a"
            ).text.strip()
            == game_details[1]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )

    def check_summoners_war(self,listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td//div[contains(@class,'products__main-info-right')]//span"
            ).text.strip()
            == game_details[0]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[2]/a"
            ).text.strip()
            == game_details[1]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )

    
    def check_valorant(self, listing_elem, game_details, price):
        # if game_details[1] == "Rank Ready":
            # return (
                # listing_elem.find_element(
                #     By.XPATH, ".//td//div[@class='text-secondary']/../div"
                # )
                # .text.strip()
                # .split(">")[0]
                # .strip()
                # .lower()
                # == game_details[0].lower()
                # and listing_elem.find_element(
                #     By.XPATH, ".//td//div[@class='text-secondary']/../div"
                # )
                # .text.strip()
                # .split(">")[2]
                # .strip()
                # .lower()
                # == game_details[1].lower()
                # and 
        #         round(
        #             float(
        #                 listing_elem.find_element(
        #                     By.XPATH, ".//td[5]//span/span"
        #                 )
        #                 .text.strip()
        #                 .split()[0]
        #             ),
        #             2,
        #         )
        #         == price
        #     )

        # else:
        return (
            # listing_elem.find_element(
            #     By.XPATH, ".//td[2]//span"
            # )
            # .text.strip()
            # .split()[0]
            # .lower()
            # == game_details[0].lower()
            # and listing_elem.find_element(
            #     By.XPATH, ".//td[2]//span"
            # )
            # .text.strip()
            # .split()[1]
            # .lower()
            # == game_details[1].lower()
            # and 
            round(float(listing_elem.find_element(By.XPATH, ".//td[5]//span/span").text.strip()),2,) == price
        )

    def check_platform(self, listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[1]/a"
            ).text.strip()
            == game_details[0]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ), 2)
            == price
        )
    
    def check_rocket_league(self, listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td//div[contains(@class,'products__main-info-right')]//span"
            ).text.strip()
            == game_details[0]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )

    def check_honkai(self, listing_elem, game_details, price):
        return (
            round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )

    def check_dota2(self, listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[1]/a"
            ).text.strip()
            == game_details[1]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )
    

    def check_counter_strile(self, listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[1]/a"
            ).text.strip()
            == game_details[2]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[2]/a"
            ).text.strip() == game_details[0]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[3]/a"
            ).text.strip() == game_details[1]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )
    
    def check_Lol(self, listing_elem, game_details, price):
        return (
            listing_elem.find_element(
                By.XPATH, ".//td//span[@class='products__name']"
            ).text.strip()
            == game_details[0]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[6]/a"
            ).text.strip() == game_details[1]
            and listing_elem.find_element(
                By.XPATH, ".//td[@class='manage__table-item']//span[2]/a"
            ).text.strip() == game_details[2]
            and round(float(
                listing_elem.find_element(
                    By.XPATH, ".//td//a[contains(@class,'g2g_products_price')]"
                ).text.strip()
            ),2)
            == price
        )

    def delete_old_listings(self, game, game_details, price, gig_number):
        self.driver.get(self.game_dict[game]["delete_url"])
        time.sleep(2)
        count = 0
        should_break = False
        input_server_rank = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Search title or offer number']")
            )
        )
        input_server_rank.send_keys(''.join(' ' + detail for detail in game_details if detail))
        time.sleep(2)
        while True:
            print("starting deleting")
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//table//tbody//tr")))
            for listing_elem in self.driver.find_elements(By.XPATH, "//table//tbody//tr"):
                time.sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView();", listing_elem)
                if self.game_dict[game]["check"](listing_elem, game_details, price):
                    print("In condition for deleting gig")

                    WebDriverWait(listing_elem, 10).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                ".//div[contains(@class,'checkbox__inner')]/input",
                            )
                        )
                    )
                    select_btn = listing_elem.find_element(
                        By.XPATH,
                        ".//div[contains(@class,'checkbox__inner')]/input",
                    )
        
                    self.driver.execute_script("arguments[0].click();", select_btn)

                    should_break = True
                    count +=1
        # break

            if should_break:
                remove_btn = self.driver.find_element(By.XPATH, "//footer//button")
                self.driver.execute_script("arguments[0].click();", remove_btn)
                submit_btn = self.driver.find_elements(By.XPATH, "//div[@class='q-card']//button")[1]
                self.driver.execute_script("arguments[0].click();", submit_btn)
                print("gig remove successfully")
                print("number of gigs: ", count)
                time.sleep(2)
                return True

        # else:
        # return should_break

            try:
                next_btn =self.driver.wait.until(
                    EC.presence_of_element_located((By.XPATH, "///button//span//i[contains(text(),'keyboard_arrow_right')]"))
                )
                self.driver.execute_script("arguments[0].click();", next_btn)
            except:
                print("No more pages")
                return False

    def delete_listing_and_creating(self):
        for index, row in self.df.iterrows():
            if row["Done"] == True:
                continue

            game = str(row["Game"]).strip()
            game_details = [str(row["Field-1"]).strip(), str(row["Field-2"]).strip(), str(row["Field-3"]).strip()]
            price = round(float(row["price"]), 2)
            title = str(row["Title"]).strip()
            gig_number_file = row["Gig Number"]

            print(
                "index: " + str(index),
                "game: " + game,
                "game details" , game_details,
                " Title: " + title,
                " Price: " + str(price),
                "gig_number: " + str(gig_number_file)
            )
            # title = title.strip()
            if row["Delete"] == True:
                gig_number = self.upload_new_offer(game, game_details, title, price)
                self.df.loc[index, "Delete"] = False
                # self.df.loc[index, "Gig Number"] = "#"+ str(gig_number)
                # self.df.to_excel(self.file_path, index=False)
                # self.save_file()
            else:
                try:
                    should_update_del_col = self.delete_old_listings(
                    game, game_details, price, gig_number_file
                )
                except:
                    should_update_del_col = False

                if should_update_del_col:
                    self.df.loc[index, "Delete"] = True

                self.save_file()
                time.sleep(1)
                gig_number = self.upload_new_offer(game, game_details, title, price)
                self.df.loc[index, "Delete"] = False
                # self.df.loc[index, "Gig Number"] = "#"+ str(gig_number)

            self.df.loc[index, "Done"] = True
            self.save_file()

        self.df["Done"] = False
        self.save_file()

    def save_file(self):
        temp_file_path = f'C:\\Users\\BABAR\\Desktop\\g2g_all_games_listing_bot_modified\\{self.profile}_tmp.xlsx'
        self.df.to_excel(temp_file_path, index=False)
        os.replace(temp_file_path, self.file_path)

    def enter_valorant_details(self,game_details):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")))
        server_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", server_button)
        time.sleep(1)
        input_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_server.send_keys(game_details[0])
        time.sleep(1)
        select_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_server.click()
        time.sleep(1)
        account_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Account Type')]/../../..//button//div[contains(text(),'Please select')]")))
        self.driver.execute_script("arguments[0].click();", account_button)
        if game_details[1] in ['Rank Ready', 'Fresh New']:
            input_accounts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_accounts.send_keys('Smurf Accounts')
            time.sleep(1)
            select_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_account.click()
            time.sleep(1)
            # self.driver.execute_script("window.scrollBy(0, 100);")
            rank_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'UnRanked Smurf')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", rank_button)
            input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_rank.send_keys(game_details[1])
            select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_rank.click()

            
        else:
            input_accounts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_accounts.send_keys('Ranked Accounts')
            select_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_account.click()

            time.sleep(1)
            rank_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", rank_button)
            time.sleep(1)
            input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_rank.send_keys(game_details[1])
            select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_rank.click()

            time.sleep(1)
            agent_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Agents')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", agent_button)
            time.sleep(1)
            input_agent = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_agent.send_keys("5+")
            select_agent = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_agent.click()

            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, 100);")
            skin_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Skins')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", skin_button)
            input_skin = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_skin.send_keys("9 or below")
            select_skin = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_skin.click()


    def enter_overwatch2(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Tank Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        tank_rank_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Tank Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", tank_rank_button)
        time.sleep(1)
        input_tank_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_tank_rank.send_keys(game_details[0])
        time.sleep(1)
        select_tank_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_tank_rank.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Golden Weapons')]/../../..//button//div[contains(text(),'Please select')]")))
        golden_weapon_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Golden Weapons')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", golden_weapon_button)
        time.sleep(1)
        input_golden_weapon = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_golden_weapon.send_keys("4 or below")
        time.sleep(1)
        select_golden_weapon = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_golden_weapon.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Legendary Skins')]/../../..//button//div[contains(text(),'Please select')]")))
        lengend_skins_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Legendary Skins')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", lengend_skins_button)
        time.sleep(1)
        input_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_lengend_skins.send_keys("4 or below")
        time.sleep(1)
        select_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_lengend_skins.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Damage Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        lengend_skins_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Damage Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", lengend_skins_button)
        time.sleep(1)
        input_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_lengend_skins.send_keys(game_details[1])
        time.sleep(1)
        select_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_lengend_skins.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Support Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        lengend_skins_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Support Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", lengend_skins_button)
        time.sleep(1)
        input_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_lengend_skins.send_keys(game_details[2])
        time.sleep(1)
        select_lengend_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_lengend_skins.click()
        time.sleep(1)


    def enter_overwatch_global(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")))
        platform_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", platform_button)
        time.sleep(1)
        input_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_platform.send_keys(game_details[0])
        time.sleep(1)
        select_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_platform.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")))
        server_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", server_button)
        time.sleep(1)
        input_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_server.send_keys(game_details[1])
        time.sleep(1)
        select_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_server.click()
        time.sleep(1)


    def enter_apex_legends(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        rank_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", rank_button)
        time.sleep(1)
        input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_rank.send_keys(game_details[0])
        time.sleep(1)
        select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_rank.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Level')]/../../..//button//div[contains(text(),'Please select')]")))
        level_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Level')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", level_button)
        time.sleep(1)
        input_level = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_level.send_keys(game_details[1])
        time.sleep(1)
        select_level = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_level.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Legendary Skins')]/../../..//button//div[contains(text(),'Please select')]")))
        legendary_skins_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Legendary Skins')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", legendary_skins_button)
        time.sleep(1)
        input_legendary_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_legendary_skins.send_keys("9 or below")
        time.sleep(1)
        select_legendary_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_legendary_skins.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Mythic Skins')]/../../..//button//div[contains(text(),'Please select')]")))
        mythic_skins_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Mythic Skins')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", mythic_skins_button)
        time.sleep(1)
        input_mythic_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_mythic_skins.send_keys("9 or below")
        time.sleep(1)
        select_mythic_skins = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_mythic_skins.click()
        time.sleep(1)
    

    def enter_FN(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        rank_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", rank_button)
        time.sleep(1)
        input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_rank.send_keys(game_details[0])
        time.sleep(1)
        select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_rank.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Outfits')]/../../..//button//div[contains(text(),'Please select')]")))
        outfits_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Outfits')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", outfits_button)
        time.sleep(1)
        input_outfits = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_outfits.send_keys(game_details[1])
        time.sleep(1)
        select_outfits = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_outfits.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Pickaxes')]/../../..//button//div[contains(text(),'Please select')]")))
        pickaxes_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Pickaxes')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", pickaxes_button)
        time.sleep(1)
        input_pickaxes = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_pickaxes.send_keys(game_details[2])
        time.sleep(1)
        select_pickaxes = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_pickaxes.click()
        time.sleep(1)


    def enter_rainbow_six(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")))
        platform_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", platform_button)
        time.sleep(1)
        input_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_platform.send_keys(game_details[0])
        time.sleep(1)
        select_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_platform.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")))
        rank_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", rank_button)
        time.sleep(1)
        input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_rank.send_keys(game_details[1])
        time.sleep(1)
        select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_rank.click()
        time.sleep(1)


    def enter_GTA_5(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")))
        platform_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Platform')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", platform_button)
        time.sleep(1)
        input_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_platform.send_keys(game_details[0])
        time.sleep(1)
        select_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_platform.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Level')]/../../..//button//div[contains(text(),'Please select')]")))
        level_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Level')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", level_button)
        time.sleep(1)
        input_level = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_level.send_keys(game_details[1])
        time.sleep(1)
        select_level = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_level.click()
        time.sleep(1)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Money Owned')]/../../..//button//div[contains(text(),'Please select')]")))
        money_owned_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Money Owned')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", money_owned_button)
        time.sleep(1)
        input_money_owned = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_money_owned.send_keys(game_details[2])
        time.sleep(1)
        select_money_owned = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_money_owned.click()
        time.sleep(1)


    def enter_league_of_legends(self,game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")))
        server_button = self.driver.find_element(By.XPATH,"//div[contains(text(),'Server')]/../../..//button//div[contains(text(),'Please select')]")
        self.driver.execute_script("arguments[0].click();", server_button)
        time.sleep(1)
        input_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
        input_server.send_keys(game_details[0])
        time.sleep(1)
        select_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
        select_server.click()
        time.sleep(1)
        account_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Account Type')]/../../..//button//div[contains(text(),'Please select')]")))
        self.driver.execute_script("arguments[0].click();", account_button)
        if game_details[1] in ['Rank Ready', 'Fresh New']:
            input_accounts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_accounts.send_keys('Smurf Accounts')
            time.sleep(1)
            select_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_account.click()
            time.sleep(1)
            rank_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'UnRanked Smurf')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", rank_button)
            input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_rank.send_keys(game_details[1])
            select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_rank.click()

            
        else:
            input_accounts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_accounts.send_keys('Ranked Accounts')
            select_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_account.click()

            time.sleep(1)
            rank_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Rank')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", rank_button)
            time.sleep(1)
            input_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_rank.send_keys(game_details[1])
            select_rank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_rank.click()

            time.sleep(1)
            champions_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Champions')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", champions_button)
            time.sleep(1)
            input_champions = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_champions.send_keys("9 or below")
            select_champions = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_champions.click()

            time.sleep(1)
            skin_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Skins')]/../../..//button//div[contains(text(),'Please select')]")))
            self.driver.execute_script("arguments[0].click();", skin_button)
            input_skin = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_skin.send_keys("9 or below")
            select_skin = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'scroll q-list')]")))
            select_skin.click()

    def enter_platform_details(self, game_details):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.ID, "platform")))
        select_server = Select(self.find_element(By.ID, "platform"))
        select_server.select_by_visible_text(game_details[0])
        time.sleep(1)

    def enter_cod_details(self, game_details):
        select_server = Select(self.find_element(By.ID, "faction"))
        select_server.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_rank = Select(self.find_element(By.ID, "platform"))
        select_rank.select_by_visible_text(game_details[1])
        time.sleep(1)

    def enter_sea_of_thieves_details(self, game_details):
        select_server = Select(self.find_element(By.ID, "server"))
        select_server.select_by_visible_text(game_details[0])
        time.sleep(1)

    def enter_summoners_war(self, game_details):
        select_server = Select(self.find_element(By.ID, "country"))
        select_server.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_rank = Select(self.find_element(By.ID, "level"))
        select_rank.select_by_visible_text(game_details[1])
        time.sleep(1)

    def enter_gta5_details(self, game_details):
        select_rank = Select(self.find_element(By.ID, "platform"))
        select_rank.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_server = Select(self.find_element(By.ID, "country"))
        select_server.select_by_visible_text(game_details[1])
        time.sleep(1)

    def enter_overwatch_global_details(self, game_details):
        select_rank = Select(self.find_element(By.ID, "platform"))
        select_rank.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_server = Select(self.find_element(By.ID, "server"))
        select_server.select_by_visible_text(game_details[1])
        time.sleep(1)

    def enter_dota2_details(self, game_details):
        # self.find_element(By.ID, "textfield_1").send_keys(game_details[0])

        select_server = Select(self.find_element(By.ID, "class"))
        select_server.select_by_visible_text(game_details[1])
        time.sleep(1)

        # self.find_element(By.ID, "textfield_4").send_keys(game_details[2])

    def enter_cs2_details(self, game_details):
        select_rank = Select(self.find_element(By.ID, "level_8"))
        select_rank.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_server = Select(self.find_element(By.ID, "level_9"))
        select_server.select_by_visible_text(game_details[1])
        time.sleep(1)

        select_server = Select(self.find_element(By.ID, "heroes"))
        select_server.select_by_visible_text(game_details[2])
        time.sleep(1)

    def enter_LOL_details(self, game_details):
        select_rank = Select(self.find_element(By.ID, "server"))
        select_rank.select_by_visible_text(game_details[0])
        time.sleep(1)

        select_server = Select(self.find_element(By.ID, "tier"))
        select_server.select_by_visible_text(game_details[1])
        time.sleep(1)

        self.find_element(By.ID, "textfield_1").send_keys(game_details[2])
        time.sleep(1)

    def enter_honkai_details(self, game_details):
        ...

    def cleanup_and_exit(self):
        try:
            self.driver.quit()
        except:
            pass
        sys.exit(1)

    def upload_new_offer(self, game, game_details, title, price, count=0):
        count += 1
        try:
            self.driver.get("https://www.g2g.com/offers/sell?cat_id=5830014a-b974-45c6-9672-b51e83112fb7")
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//button//div[contains(text(),'Select brand')]")))
            game_button = self.driver.find_element(By.XPATH,"//button//div[contains(text(),'Select brand')]")
            self.driver.execute_script("arguments[0].click();", game_button)
            time.sleep(1)
            input_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type to filter']")))
            input_server.send_keys(game)
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, 100);")
            select_server = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@tabindex='0']")))
            select_server.click()
            time.sleep(1)
            continue_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Continue')]/..")))
            continue_btn.click()
            time.sleep(1)

            self.game_dict[game]["enter_details"](game_details)
            time.sleep(2)
            current_url = self.driver.current_url
            gig_number = current_url.split("/")[-2].strip()

            if game in ["Valorant", "League of Legends"] and game_details[1] in ['Rank Ready', 'Fresh New']:
                WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//div//textarea[contains(@placeholder,'description')]")))
                self.driver.find_element(By.XPATH, "//div//textarea[contains(@placeholder,'description')]").send_keys(title)
            else:
                WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Offer title']")))
                self.driver.find_element(By.XPATH, "//input[@placeholder='Offer title']").send_keys(title)
                self.driver.find_element(By.XPATH, "//div//textarea[contains(@placeholder,'description')]").send_keys(title)
            time.sleep(1)
            #price enter

            price_input = self.driver.find_element(By.XPATH, "//div[contains(text(),'price')]/../../..//div[@class='right col']//input")
            price_input.clear()
            price_input.send_keys(str(price))
            time.sleep(1)


            btn_manual = self.driver.find_element(By.XPATH, "//div[@aria-label='Manual delivery']/div")
            self.driver.execute_script("arguments[0].click();", btn_manual)

            minimun_purchase = self.driver.find_elements(By.XPATH, "//div[contains(text(),'Minimum purchase quantity')]/../../..//input")[1]
            minimun_purchase.send_keys("1")
            
            self.driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("1")
            
            min_button = self.driver.find_element(By.XPATH,"//button//div[contains(text(),'0 minute')]")
            self.driver.execute_script("arguments[0].click();", min_button)

            ten_min_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'10 minutes')]")))
            self.driver.execute_script("arguments[0].click();", ten_min_button)

            btn_publish = self.driver.find_element(By.XPATH, "//span[text()='Publish']/../../..")
            self.driver.execute_script("arguments[0].click();", btn_publish)


            time.sleep(5)
            # self.driver.close_other_tabs()
            # try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='q-card']//div[contains(text(),'Your offer has been published.')]")))
            self.driver.find_element(
                By.XPATH,
                "//div[@class='q-card']//div[contains(text(),'Your offer has been published.')]"
            )

            print(
                f"Message from {self.profile} bot:\nNew Offer created Succesfully :)\n"
                + "-" * 50
                )
            return gig_number

        except Exception as e:
            print(traceback.format_exc())
            print("error :", e)
            print(
                f"Message from {self.profile} bot:\nFailed to create new offer :(\n"
                + "-" * 50
            )
            if count > 3:
                # self.driver.quit()
                self.cleanup_and_exit()
                time.sleep(3)
            self.upload_new_offer(game, game_details, title, price, count)

    def run(self):
        # while True:
            # if time.time() - self.last_start_time >= 600
        try:
                # print(self.page_source)
                # self.last_start_time = None
            self.delete_listing_and_creating()
                # break
                # time.sleep(120)
        except Exception as e:
            print(traceback.format_exc())
            print("error :", e)
            self.cleanup_and_exit()
                # self.driver.quit()
                # self.driver = Chrome(
                #     service=Service(ChromeDriverManager().install()),
                #     options=self.options
                # )
                
            # time.sleep(5)
