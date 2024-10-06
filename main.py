import instaloader

# Function to get unfollowers
def get_unfollowers(username, password):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Log in to your Instagram account
    L.login(username, password)  # (username, password)

    # Get profile of the logged-in user
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the list of following and followers
    following = set(profile.get_followees())
    followers = set(profile.get_followers())

    # Find users who are following you but you don't follow back
    not_following_back = following - followers

    print("Users not following you back:")
    for user in not_following_back:
        print(user.username)

# Replace with your Instagram username and password
username = 'your_username'
password = 'your_pass'

get_unfollowers(username, password)

# # from selenium import webdriver
# # from time import sleep
# # from secrets import pw
# #
# #
# # class InstaBot:
# #     def __init__(self, username, pw):
# #         self.driver = webdriver.Chrome()
# #         self.username = username
# #         self.driver.get("https://instagram.com")
# #         sleep(2)
# #         self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
# #             .click()
# #         sleep(2)
# #         self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
# #             .send_keys(username)
# #         self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
# #             .send_keys(pw)
# #         self.driver.find_element_by_xpath('//button[@type="submit"]')\
# #             .click()
# #         sleep(4)
# #         self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
# #             .click()
# #         sleep(2)
# #
# #     def get_unfollowers(self):
# #         self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
# #             .click()
# #         sleep(2)
# #         self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
# #             .click()
# #         following = self._get_names()
# #         self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
# #             .click()
# #         followers = self._get_names()
# #         not_following_back = [user for user in following if user not in followers]
# #         print(not_following_back)
# #
# #     def _get_names(self):
# #         sleep(2)
# #         sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
# #         self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
# #         sleep(2)
# #         scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
# #         last_ht, ht = 0, 1
# #         while last_ht != ht:
# #             last_ht = ht
# #             sleep(1)
# #             ht = self.driver.execute_script("""
# #                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
# #                 return arguments[0].scrollHeight;
# #                 """, scroll_box)
# #         links = scroll_box.find_elements_by_tag_name('a')
# #         names = [name.text for name in links if name.text != '']
# #         # close button
# #         self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
# #             .click()
# #         return names
# #
# #
# # my_bot = InstaBot('nid.aaa_', pw)
# # my_bot.get_unfollowers()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from secrets import pw
#
# class InstaBot:
#     def __init__(self, username, pw):
#         # Specify the path to chromedriver here
#         service = Service(executable_path=r'C:\path\to\chromedriver.exe')  # Change this path
#         self.driver = webdriver.Chrome(service=service)
#         self.username = username
#         self.driver.get("https://instagram.com")
#         sleep(2)
#
#         # Updated to use By class for locating elements
#         self.driver.find_element(By.XPATH, "//a[contains(text(), 'Log in')]").click()
#         sleep(2)
#         self.driver.find_element(By.NAME, "username").send_keys(username)
#         self.driver.find_element(By.NAME, "password").send_keys(pw)
#         self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
#         sleep(4)
#         self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
#         sleep(2)
#
#     def get_unfollowers(self):
#         self.driver.find_element(By.XPATH, f"//a[contains(@href,'/{self.username}')]").click()
#         sleep(2)
#         self.driver.find_element(By.XPATH, "//a[contains(@href,'/following')]").click()
#         following = self._get_names()
#         self.driver.find_element(By.XPATH, "//a[contains(@href,'/followers')]").click()
#         followers = self._get_names()
#         not_following_back = [user for user in following if user not in followers]
#         print(not_following_back)
#
#     def _get_names(self):
#         sleep(2)
#         sugs = self.driver.find_element(By.XPATH, '//h4[contains(text(), "Suggestions")]')
#         self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
#         sleep(2)
#         scroll_box = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]")
#         last_ht, ht = 0, 1
#         while last_ht != ht:
#             last_ht = ht
#             sleep(1)
#             ht = self.driver.execute_script("""
#                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
#                 return arguments[0].scrollHeight;
#                 """, scroll_box)
#         links = scroll_box.find_elements(By.TAG_NAME, 'a')
#         names = [name.text for name in links if name.text != '']
#         # Close button
#         self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/button").click()
#         return names
#
# # Initialize the bot with your username and password
# my_bot = InstaBot('nid.aaa_', pw)
# my_bot.get_unfollowers()



