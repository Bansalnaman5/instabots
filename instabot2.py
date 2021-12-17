
##CODE BY NAMAN BANSAL

###IMPPORTANT: THE GRAPHS WERE OVERLAPPING THATS WHY THE 
#SHOW FUNCTION HAS BEEN COMMENTED
#ADD YOUR OWN FILE NAME IF WANT TO IN LINE 172

from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
import time

class instabot:
    def __init__(self):
        self.username='SAMPLE USERNAME'
        self.pas='SAMPLE PASSWORD'
        ##ADD WEBDRIVER CREDENTIALS ACCORDING TO YOR PC CONFIG
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\Naman\\Downloads\\chromedriver_win32\\chromedriver.exe')
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        user=self.driver.find_elements_by_name('username')
        user[0].send_keys(self.username)
        pas=self.driver.find_element_by_name('password')
        pas.send_keys(self.pas)
        pas.submit()
        time.sleep(3)
        aw=self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW   HoLwm ')]")
        aw.click()
        time.sleep(2)
    def past_three_days_posts(self):
        search=self.driver.find_element_by_class_name('TqC_a')
        search.click()
        time.sleep(1)
        serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
        time.sleep(1)
        serch.send_keys("food")
        time.sleep(2)
        options=self.driver.find_elements_by_class_name('Ap253')
        i=0
        foodliist=[]
        while i<len(options) and len(foodliist)<10:
            k=options[i].text
            if k[0]!='#' and k!='food':
                foodliist.append(k)
                
            i+=1
        clo=self.driver.find_element_by_xpath("//*[contains(@class,'aIYm8 coreSpriteSearchClear')]")
        clo.click()
        time.sleep(1)
        global d
        d={}
        for i in foodliist:   
            search=self.driver.find_element_by_class_name('TqC_a')
            search.click()
            time.sleep(1)
            serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
            time.sleep(1)
            serch.send_keys(i)
            time.sleep(2)
            w=self.driver.find_element_by_class_name("yCE8d  ")
            w.click()
            time.sleep(2)
            k=self.driver.find_elements_by_xpath("//*[contains(@class,'g47SY ')]")
            u=k[1].text
            t=0
            if u[-1]=='m':
                t=float(u[:len(u)-1])
                t=t*1000000
            elif u[-1]=='k':
                t=float(u[:len(u)-1])
                t=t*1000
            else:
                t=float(u)
            d[i]=int(t)

            time.sleep(1)
        global hand
        hand=[]
        dp=sorted(d.items(),key=lambda p:(p[1],p[0]),reverse=True)
        for i in dp:
            if len(hand)<5:
                hand.append(i[0])
            else:
                break
        l={}
        for i  in hand:
            search=self.driver.find_element_by_class_name('TqC_a')
            search.click()
            time.sleep(1)
            serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
            time.sleep(1)
            serch.send_keys(i)
            time.sleep(2)
            w=self.driver.find_element_by_class_name("yCE8d  ")
            w.click()
            time.sleep(2)
            de=self.driver.find_element_by_class_name("_9AhH0")
            de.click()
            time.sleep(2)
            while(1):
                po=self.driver.find_element_by_xpath("//*[contains(@class,'_1o9PC Nzb55')]")
                ii=po.text
                

                if ii[3]=='H' or ii[2]=='H' or (ii[2]=='D' and int(ii[0])<=3) or ii[3]=='M' or ii[2]=='M':
                    l[i]=l.get(i,0)+1
                    self.driver.execute_script('window.scrollBy(0,100);')
                    nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                    nex.click()
                    time.sleep(2)
                else:
                    time.sleep(2)
                    close=self.driver.find_element_by_xpath("//*[contains(@class,'                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG')]")
                    close.click()
                    break
        l1=[]
        l2=[]
        print("the username and nummber of posts in past three days")
        for i in l:
            l1.append(i)
            l2.append(l[i])
            print(i,l[i])
        plt.bar(l1,l2)
        #plt.show()
    #end of FUNCTION FOR QUESTION 1
    def hashtags(self):
        ht={}
        for i in hand:
            search=self.driver.find_element_by_class_name('TqC_a')
            search.click()
            serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
            time.sleep(1)
            serch.send_keys(i)
            time.sleep(2)
            w=self.driver.find_element_by_class_name("yCE8d  ")
            w.click()
            time.sleep(3)
            de=self.driver.find_element_by_class_name("_9AhH0")
            de.click()
            time.sleep(2)
            for i in range(10):
                try:
                    ll=self.driver.find_elements_by_xpath("//*[contains(@class,' xil3i')]")
                    for j in ll:
                        ht[j.text]=ht.get(j.text,0)+1
                    nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                    nex.click()
                    time.sleep(2)
                except:
                    nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                    nex.click()
                    time.sleep(2)
            close=self.driver.find_element_by_xpath("//*[contains(@class,'                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG')]")
            close.click()
        ht=sorted(ht.items(),key=lambda p:(p[1],p[0]),reverse=True)
        t1=[]
        t2=[]
        t3=[]
        try:
            print("most used hashtags is : ")
            print(ht[0])
        except:print("hehe")
        for i in ht:
            t3.append([i[0],i[1]])
            if len(t1)<5:
                t1.append(i[0])
                t2.append(i[1])
                
        plt.pie(t2,labels=t1,autopct='%.2f')
        #plt.show()
        data=pd.DataFrame(t3,columns=["hashtag","frequency"])
        data.to_csv('nmn.csv')
    #end OF FUNCTION FOR QUESTION 2
    def average_followers(self):
        oo={}
        for i in hand:
            search=self.driver.find_element_by_class_name('TqC_a')
            search.click()
            time.sleep(1)
            serch=self.driver.find_element_by_xpath("//*[contains(@class,'XTCLo x3qfX focus-visible')]")
            time.sleep(1)
            serch.send_keys(i)
            time.sleep(3)
            w=self.driver.find_element_by_class_name("yCE8d  ")
            w.click()
            time.sleep(2)
            de=self.driver.find_element_by_class_name("_9AhH0")
            de.click()
            time.sleep(2)
            ty=0
            while ty<10:

                try:
                    de=self.driver.find_element_by_xpath("//*[contains(@class,'vcOH2')]")
                    de.click()
                    time.sleep(2)
                    re=self.driver.find_element_by_xpath("//*[contains(@class,'vJRqr')]")
                    p=re.get_attribute('outerHTML')[25:33]
                    num=''
                    for j in p:
                        if j in '0123456789':
                            num=num+str(j)
                    num=float(num)
                    oo[i]=oo.get(i,0)+(num/10)
                    act=webdriver.common.action_chains.ActionChains(self.driver)
                    act.move_to_element_with_offset(re,100,100).click().perform()
                    time.sleep(2)
                    nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                    nex.click()
                    time.sleep(2)
                except:
                        try:
                            time.sleep(2)
                            de=self.driver.find_element_by_xpath("//*[contains(@class,'sqdOP yWX7d     _8A5w5    ')]")
                            p=de.get_attribute('outerHTML')[40:]
                            num=''
                            for j  in p:
                                if j in '0123456789':
                                    num=num+str(j)
                            n=float(num)
                            oo[i]=oo.get(i,0)+(n/10)
                            time.sleep(2)
                            nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                            nex.click()
                            time.sleep(2)
                        except:
                        
                            time.sleep(2)
                            nex=self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
                            nex.click()
                
                ty+=1
            close=self.driver.find_element_by_xpath("//*[contains(@class,'                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG')]")
            close.click()
        final={}
        for i in oo:
            u=oo[i]/d[i]
            final[i]=u
        f1=[]
        f2=[]
        print("the username and follower:like ratio is : ")
        for i in final:
            f1.append(i)
            f2.append(final[i])
            print(i,final[i])
        plt.bar(f1,f2)
        #plt.show()

obj=instabot()
obj.login()
time.sleep(2)
obj.past_three_days_posts()
time.sleep(2)
obj.hashtags()
time.sleep(2)
obj.average_followers()
time.sleep(200)


