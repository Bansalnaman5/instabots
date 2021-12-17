##CODE BY NAMAN BANSAL

from selenium import webdriver
import time

class insta:
    def __init__(self):
        self.user=""
        self.pas=""
        #ADD YOR OWN WEBDRIVER EXECUTABLE PATH ADDRESS
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\Naman\\Downloads\\chromedriver_win32\\chromedriver.exe')
    #Login to your Instagram Handle
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user=self.driver.find_elements_by_name('username')
        user[0].send_keys(self.user)
        pas=self.driver.find_element_by_name('password')
        pas.send_keys(self.pas)
        pas.submit()
        time.sleep(3)
        aw=self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW   HoLwm ')]")
        aw.click()
    #extracting usernames after typing food in search bar   
    def foo(self):
        print("usernames starting with food are :")
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(1)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        time.sleep(1)
        serch.send_keys("food")
        time.sleep(2)
        options=self.driver.find_elements_by_class_name('Ap253')
        i=0
        while i<len(options):
            k=options[i].text
            if k[0]!='#':
                print(k)
                
            i+=1
        time.sleep(2)
    #opening the profile of so delhi
    def prof(self):
        clo=self.driver.find_element_by_xpath("//*[contains(@class,'aIYm8 coreSpriteSearchClear')]")
        clo.click()
        time.sleep(1)
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(1)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        time.sleep(2)
        serch.send_keys("So Delhi")
        time.sleep(2)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        time.sleep(2)
    #following unfollowing profile of so delhi and printing appropiate message
    #according to sitiuation
    def follow_unfollow(self):
        try:
            ty=self.driver.find_element_by_xpath("//*[contains(@class,'_5f5mN       jIbKX  _6VtSN     yZn4P   ')]")
            ty.click()
        except:print("already following")
        time.sleep(2)
        try:
            ty=self.driver.find_element_by_xpath("//*[contains(@class,'_5f5mN    -fzfL     _6VtSN     yZn4P   ')]")
            ty.click()
            time.sleep(2)
            rt=self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW -Cab_   ')]")
            rt.click()
        except:print("already not following")
        time.sleep(2)
    #liking unliking the username dilsefoodie and printind message
    def liking_unliking(self):
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(1)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        time.sleep(2)
        serch.send_keys("dilsefoodie")
        time.sleep(2)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        time.sleep(2)
        de=self.driver.find_element_by_class_name("_9AhH0")
        de.click()
        time.sleep(2)
        for i in range(30):
            like=self.driver.find_element_by_class_name("fr66n")
            lp=like.get_attribute('outerHTML')
            if "Like" in lp:
                like=self.driver.find_element_by_class_name("fr66n")
                like.click()
                time.sleep(1)
                nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                nex.click()
                time.sleep(2)
            else:
                print("already liked post",i+1)
                nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                nex.click()
                time.sleep(2)
        close=self.driver.find_element_by_xpath("//*[contains(@class,'                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG')]")
        close.click()
        time.sleep(1)
        de=self.driver.find_element_by_class_name("_9AhH0")
        de.click()  
        for i in range(30):    
            like=self.driver.find_element_by_class_name("fr66n")
            lp=like.get_attribute('outerHTML')
            if "Unlike" in lp:    
                like=self.driver.find_element_by_class_name("fr66n")
                like.click()
                time.sleep(1)
                nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                nex.click()
                time.sleep(2)
            else:
                print("already unliked post",i+1)
                nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                nex.click()
                time.sleep(1)
        close=self.driver.find_element_by_xpath("//*[contains(@class,'                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG')]")
        close.click()
        
        time.sleep(2)
    #extracting list of followers
    def listfollowers(self):
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(1)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        time.sleep(2)
        serch.send_keys("foodtalkindia")
        time.sleep(2)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        time.sleep(2)
        ki=self.driver.find_elements_by_xpath("//*[contains(@class,'-nal3 ')]")
        ki[1].click()
        time.sleep(2)
        fb=self.driver.find_element_by_xpath("//*[contains(@class,'isgrP')]")
        lo=[]
        while len(lo)<501:
            self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollTop + 2000;',fb)
            lo=self.driver.find_elements_by_xpath("//*[contains(@class,'FPmhX notranslate  _0imsa ')]")
            time.sleep(1)
        time.sleep(2)
        print("usernames of foodtalkindia")
        for i in lo:
            print(i.text)
        cl=self.driver.find_elements_by_xpath("//*[contains(@class,'WaOAr')]")
        cl[1].click()
        time.sleep(2)
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(2)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        serch.send_keys("So delhi")
        time.sleep(2)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        time.sleep(2)
        ki=self.driver.find_elements_by_xpath("//*[contains(@class,'-nal3 ')]")
        ki[1].click()
        time.sleep(2)
        fb=self.driver.find_element_by_xpath("//*[contains(@class,'isgrP')]")
        lo=[]
        while len(lo)<501:
            self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollTop + 2000;',fb)
            lo=self.driver.find_elements_by_xpath("//*[contains(@class,'FPmhX notranslate  _0imsa ')]")
            time.sleep(1)
        time.sleep(2)
        print("usernames of so delhi")
        for i in lo:
            print(i.text)
        cl=self.driver.find_elements_by_xpath("//*[contains(@class,'WaOAr')]")
        cl[1].click()
        time.sleep(2)
    #extracting followers that operator is following
    def extract_followers(self):
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(2)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        serch.send_keys("foodtalkindia")
        time.sleep(2)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        time.sleep(2)
        print("the common followers are : ")
        try:
            rt=self.driver.find_elements_by_class_name("_32eiM")
            for i in rt[1:]:
                print(i.text)
        except:print("no follower")
        time.sleep(2)
        #checking the story of coding.ninjas and printing appropiate message
    def story_check(self):
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(2)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        serch.send_keys("coding.ninjas")
        time.sleep(1)
        w=self.driver.find_element_by_class_name("yCE8d  ")
        w.click()
        de=self.driver.find_elements_by_xpath("//*[contains(@class,'RR-M- h5uC0')]")
        if len(de)==0:
            print('user has no story')
        else:
            de[0].click()
                
  
#q=input("enter username")
#w=input("enter password")
obj=insta()
time.sleep(2)
obj.login()
time.sleep(2)
obj.foo()
time.sleep(2)
obj.prof()
time.sleep(2)
obj.follow_unfollow()
time.sleep(2)
obj.liking_unliking()
time.sleep(2)
obj.listfollowers()
time.sleep(2)
obj.extract_followers()
time.sleep(2)
obj.story_check()
time.sleep(200)