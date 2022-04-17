import PySimpleGUI as sg #Our Primary GUI builder
from deepgram import Deepgram #API that helps extract audio transcript
import asyncio, json #To deal with asynchronous processes
from nltk.corpus import stopwords #Natural Language Processing Packages
from nltk.tokenize import word_tokenize, sent_tokenize #Natural Language Processing Packages
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor #Natural Language Processing Packages
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer #Natural Language Processing Packages
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor #Natural Language Processing Packages
import pyautogui as pg #Secondary GUI builder
with open('db.txt') as f:
    lines = f.readlines()
    #print(lines)
    zay = (lines[0])
    zay = str(zay)
DEEPGRAM_API_KEY = zay 
import os #To manage local files and API keys
from yt_dlp import YoutubeDL #To download YouTube links

while True: #While loop to keep the GUI running
    sg.theme('dark grey 10')
    layout = [[sg.Text("Enter YouTube video link here:")],
            [sg.Input(key='-INPUT-')],
            [sg.Text(size=(10,3), key='-OUTPUT-')],
            [sg.Button('Enter')]]
    window = sg.Window('TL;DW-inator', layout)
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    window['-OUTPUT-'].update('Your Video is being processed please wait for a few minutes!')
    
    linkz = values['-INPUT-']
    ydl_opts = {'format': 'bestaudio'}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([linkz])# Youtube video downloading 

            
    abc = "demo"

    x = os.listdir()
    for i in x:
        if i.endswith('.webm'):
            global xz
            xz = abc + '.mp4'
            os.rename(i,xz) #Renaming downloaded file
            print(xz)
    PATH_TO_FILE = xz
    MIMETYPE = 'audio/wav'

    async def main():#Async function to handle DeepGram API

        dg_client = Deepgram(DEEPGRAM_API_KEY)
        
        with open(PATH_TO_FILE, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': MIMETYPE}
            options = {'punctuate': True, 'language': 'en-GB'}
            response = await dg_client.transcription.prerecorded(source,  options)
            ya = response["results"]["channels"]
            index = 0
            fog = ya[index]
            fog2 = fog["alternatives"]
            index_3 = 0
            fogz = fog2[index_3]
            global xas
            xas = fogz['transcript']
            
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())   
    def transcript(): #using NLTK to understand text summarization, more details in the PPT
        text = xas
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)

        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues / len(sentenceValue))
        global summary
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence

    transcript()
    def transr(): #summarizing already summarized text to extract shorter version of the summary.
        document = summary
        auto_abstractor = AutoAbstractor()

        auto_abstractor.tokenizable_doc = SimpleTokenizer()

        auto_abstractor.delimiter_list = [".", "\n"]

        abstractable_doc = TopNRankAbstractor()

        result_dict = auto_abstractor.summarize(document, abstractable_doc)


        for sentence in result_dict["summarize_result"]:
            #print(sentence)
            listToStr = ' '.join([str(elem) for elem in result_dict["summarize_result"]])
        #print(listToStr)  
        
        pg.alert(text=listToStr, title='Video Summary [TL;DW-inator]')
    transr()
    os.remove(xz) #Deleting the file after the process ended.
    window.close()
