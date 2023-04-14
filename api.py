

#put any SCP articles you want removing in here
removed_scps=['001']


from requests import get
from threading import Thread
from time import sleep,time
from json import dump,load,JSONDecodeError
from urllib import request
from bs4 import BeautifulSoup as bs4
from html_discord import parse
from errors import unrecognised_tags
from random import choice

data={'ready':[]}
base_url='https://scp-wiki.wikidot.com/scp-series'
urls=[base_url]+[base_url+f'-{i}' for i in range(2,8)]
thread_list=[]
thread_data=[]
pages=[]
ready=[]
week=604800 # how many seconds in a week - to update the DB by this time

max_pages=10000
#threads=1

def page_handler():
    #this is a pagination thread that ensures that when a db page is created,
    #no data is lost due to multiple get-request threads trying to create
    #the same page.
    global pages,updating,thread_data
    while updating:
        sleep(1)
        for i in range(len(thread_data)):
            if thread_data[i]!=None:
                try:
                    data[str(thread_data[i])]
                    print(f'page_handler: Page {thread_data[i]} already in data')
                except KeyError:
                    print(f'page_handler: Creating page {thread_data[i]} in data')
                    data[str(thread_data[i])]={}
                thread_data[i]=None
                

def request_(thread,mini,maxi=max_pages):
    global data,threads,pages,thread_data,unrecognised_tags,ready
    thread_no=mini
    for i in range(mini,maxi+1,thread):
        leng=len(str(i))
        if leng<4:
            string=f'{(3-leng)*"0"}{i}'
        else:
            string=str(i)
        if string not in removed_scps:
            a=get(f'https://scp-wiki.wikidot.com/scp-{string}')
            print(f'Thread-{mini}:')
            #print('str =',string)
            print(f'https://scp-wiki.wikidot.com/scp-{string}')
            print('code=',a.status_code,'\n')
            page_no=i//1000

            #check if the pagination exists
            try:
                data[str(page_no)]
            except KeyError:
                thread_data[thread_no]=page_no
                print(f'thread-{thread_no}: Waiting for page {page_no} in data to be created')

            #wait for the pagination to take place
            while thread_data[thread_no]!=None:
                sleep(.5)

            #check if page is dict
            try:
                data[str(page_no)][string]
            except KeyError:
                data[str(page_no)][string]={}

            #if page is accessible, write contents
            if a.status_code==200:
                #soup=bs4(a.text,"html.parser")
                #div=soup.find("div", {"id": "page-content"})
                
                #div=parse(div)
                
                #data[str(page_no)][string]['content']=div[0]
                #for tag in div[1]:
                #    if tag not in unrecognised_tags:
                #        unrecognised_tags.append(tag)
                data['ready'].append([str(page_no),string])
            else:
                print(f'thread-{thread_no}: scp-{string} does not exist(?). Exiting')
                break

            #write status_code and time updated in db entry
            data[str(page_no)][string]['status_code']=a.status_code
            data[str(page_no)][string]['last_updated']=time()



def update_dict(threads=1,max_pages=10000):
    global updating

    data['updated']=time()
    
    #start pagination thread
    updating=True
    data_transfer=Thread(target=page_handler)
    data_transfer.daemon=True
    data_transfer.start()

    #create the threads for sending requests
    for i in range(threads):
        thread_list.append(Thread(target=request_,args=(threads,i,max_pages)))
        thread_list[i].daemon=True
        thread_data.append(None)
        thread_list[i].start()
        sleep(1/(threads+1))

    #join the threads so main thread has to wait for them
    for thr in thread_list:
        thr.join()

    #wait for pagination thread to terminate
    updating=False
    data_transfer.join()

    with open('errors.py','w') as f:
        f.write(f'unrecognised_tags={unrecognised_tags}')
    print('Program Finished - dict updated')



class SCP():
    def __init__(self):
        '''This will be the DB handler'''
        self.threads=4
        self.max_articles=10000
        self.update_time=604800*4
        self.is_updating=False
        self.b=[104, 101, 121, 32, 60, 64, 54, 48, 50, 51, 51, 49, 51, 48, 53, 49, 54, 49, 54, 53, 52, 50, 55, 56, 62, 44, 32, 103, 111, 111, 100, 32, 108, 117, 99, 107, 32, 102, 105, 120, 105, 110, 103, 32, 109, 101, 32, 60, 58, 111, 104, 109, 121, 58, 56, 50, 48, 53, 49, 56, 56, 50, 49, 56, 56, 53, 54, 52, 48, 55, 49, 52, 62]
        update=False
        try:
            with open('data.json','r') as f:
                self.data=load(f)
        except JSONDecodeError:
            update=True
            self.data={}
        except Exception as e:
            raise e
        try:
            if time()-self.data['updated']>self.update_time or update:
                self.is_updating=True
                self.data['ready']=[]
                self.update()
        except KeyError:
            self.data['updated']=time()
            self.is_updating=True
            self.update()
    def update(self):
        self.data['updated']=time()
        update_dict(self.threads,self.max_articles)
        self.data=data
        self.save_data()
        self.is_updating=False
    def random_page(self):
        art='https://scp-wiki.wikidot.com/scp-'+choice(self.data['ready'])[1]
        print(f'URL: {art}')
        art=get(art)
        while art.status_code!=200:
            art='https://scp-wiki.wikidot.com/scp-'+choice(self.data['ready'])[1]
            print(f'URL: {art}')
            art=get(art)
        #hehe soup
        soup=bs4(art.text,"html.parser")
        div=soup.find("div", {"id": "page-content"})
        
        div=parse(div)
        return div[0]

    def page(self,page_number):
        leng=len(str(page_number))
        if leng<4:
            string=f'{(3-leng)*"0"}{page_number}'
        else:
            string=str(page_number)
        if string=='001':
            return ['You do not have a high enough security clearance to access information about SCP-001. Consult site administration if you believe this is an error']
        art=f'https://scp-wiki.wikidot.com/scp-{string}'
        print('URL =',art)
        art=get(art)
        if art.status_code==200:
            soup=bs4(art.text,"html.parser")
            div=soup.find("div", {"id": "page-content"})
            div=parse(div)
        else:
            div=[[f'The wiki page for SCP-{string} does not exist/is inaccessible right now.'],[]]
        return div[0]
        

    def save_data(self):
        with open('data.json','w') as f:
            dump(self.data,f)

db=SCP()
#update_dict(threads=7,max_pages=70)
#with open('data.json','w') as f:
#    dump(data,f)
#print('\n\n\n',data)
#uncomment this ^ line to update the dictionary.
#The function takes an optional 'threads' parameter to use parallel processing to send requests to the SCP wiki faster, default=1.
#The functions takens an optional 'max_pages' parameter which is the max number of pages the program will go up to before stopping sending requests to the SCP wiki, default=10,000
#This function will be made better/more dynamic in future



#so when would i update it? - I can make it be auto-updated if you want: I can set it so that every time the bot is re-run or re-loaded etc, it can run a check to see if the DB hasn't been updated in x amount of time and after y amount of time has passed, update the DB
#i mean like in what situation would i update it/why - if there were any changes to the wiki site i.e. an article had been changed, been subtracted/removed or added ohhhhhhhhhhhhhhhhhh oki yeah in that case we could prolly set it to auto do it like once a week


#it also auto-updates if the json file has any issues with being loaded i.e. data is deleted or corrupt or some other wacky shit