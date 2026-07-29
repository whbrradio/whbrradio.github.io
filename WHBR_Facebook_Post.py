import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


# ==========================
# WHBR SETTINGS
# ==========================

NOWPLAYING = r"C:\Users\braed\OneDrive\Desktop\whbr website\nowplaying.txt"

FACEBOOK_PAGE = "https://www.facebook.com/people/WHBR-RADIO/61592787113071/"

WEBSITE = "https://whbrroanoke.netlify.app"


# ==========================
# SAVED FACEBOOK PROFILE
# ==========================

PROFILE = r"C:\Users\braed\Desktop\WHBR_Facebook_Profile"


# ==========================
# OPEN CHROME
# ==========================

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

options.add_argument(
    f"--user-data-dir={PROFILE}"
)


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


wait = WebDriverWait(driver, 15)


print("Opening Facebook...")

driver.get("https://www.facebook.com")

time.sleep(5)


last_song = ""


# ==========================
# MAIN LOOP
# ==========================

while True:

    try:

        with open(
            NOWPLAYING,
            "r",
            encoding="utf-8"
        ) as file:

            song = file.read().strip()


        if song and song != last_song:


            print("")
            print("NEW SONG FOUND:")
            print(song)


            last_song = song


            post_text = f"""🎵 NOW PLAYING:
{song}

🔴 Listen Live:
{WEBSITE}

WHBR Radio - Playing the best music 24/7!"""


            print("Opening WHBR page...")

            driver.get(FACEBOOK_PAGE)

            time.sleep(4)



            # ==========================
            # OPEN COMPOSER
            # ==========================

            print("Opening composer...")


            composer = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[contains(text(),\"What's on your mind?\")]"
                    )
                )
            )


            driver.execute_script(
                "arguments[0].click();",
                composer
            )


            print("Composer opened")


            time.sleep(2)



            # ==========================
            # TYPE POST
            # ==========================

            print("Finding textbox...")


            boxes = driver.find_elements(
                By.XPATH,
                "//div[@contenteditable='true']"
            )


            print(
                "Textboxes found:",
                len(boxes)
            )


            if len(boxes) == 0:
                raise Exception("No textbox found")


            textbox = boxes[-1]


            driver.execute_script(
                "arguments[0].click();",
                textbox
            )


            pyperclip.copy(post_text)


            textbox.send_keys(
                Keys.CONTROL,
                "v"
            )


            print("Text entered")


            time.sleep(2)



            # ==========================
            # CLICK NEXT
            # ==========================

            print("Looking for Next...")


            next_clicked = False


            buttons = driver.find_elements(
                By.XPATH,
                "//div[@role='button']"
            )


            for button in buttons:

                try:

                    if button.text.strip() == "Next":

                        driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        next_clicked = True

                        print("Next clicked")

                        break

                except:

                    pass



            if not next_clicked:

                print("Next button not found")

                driver.save_screenshot(
                    "next_failed.png"
                )

                continue



            time.sleep(2)



            # ==========================
            # CLICK POST
            # ==========================

            print("Looking for Post...")


            post_clicked = False


            buttons = driver.find_elements(
                By.XPATH,
                "//div[@role='button']"
            )


            for button in buttons:

                try:

                    if button.text.strip() == "Post":

                        driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        post_clicked = True

                        print("POSTED SUCCESSFULLY!")

                        break

                except:

                    pass



            if not post_clicked:

                print("Post button not found")

                driver.save_screenshot(
                    "post_failed.png"
                )



            time.sleep(5)



        time.sleep(5)



    except Exception as e:

        print("")
        print("ERROR:")
        print(e)

        time.sleep(10)