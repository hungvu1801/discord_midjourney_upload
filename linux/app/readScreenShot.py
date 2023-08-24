import pytesseract
import PIL.ImageGrab
import time
import cv2
import re
import logging
import sys
from app.init import loggerDecor

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s: %(levelname)s: %(message)s ", 
    stream=sys.stdout)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@loggerDecor
def screenShot():
    time.sleep(2)
    # Capture the screenshot
    screenshot = PIL.ImageGrab.grab()
    fileName = "Tmp/savedscreenshot.png"
    screenshot.save(fileName)
    return fileName

@loggerDecor
def checkPattern(text):
  pattern1 = "(Your job queue is full)"
  pattern2 = "(Please check the bottom of the channel)"
  if re.search(pattern1, text) or re.search(pattern2, text):
    return True
  return False
  
@loggerDecor   
def readScreenShot():
  fileName = screenShot()
  imageCv = cv2.imread(fileName)
  # Extract the text from the screenshot
  custom_config = r'-l eng --oem 3 --psm 6'
  text = pytesseract.image_to_string(imageCv, config=custom_config)
  textCleaned = re.sub("\n", "", text)
  if checkPattern(textCleaned):
     return True
  return False

# test1 = """
# Activities CDK) Aug23 17:52 & & en & 4) 1 100%; CO eC ea} er ee 3a | cy ae eee oer @ Midjourney Bot Oa me Me ia age>) CRT ‘a ae aara ® Nitro :ay vy Vk) ua fey avQ (>, Pete a ed ae 0 2]5 o O seem raspberry popsicle sublimation clipart, high quality, detailed clipart, white background, very detailed, Cartoon, hyper realistic, intricate detail,5° 6 illustration style, high solution, on the white background --s 750 --v 5.1- @bcboss (relaxed) Pe SeaAse taal+ /" f Pnj2 bse Generate an image based on a text prompt inQe Za a p Pie eee eae uC)fe 5 | ET a nerdeae firey eeu ey ey nuePeayi f a Pee Ns st@y\a arr)= ae‘ SS a odaoe Cree nSPart: PP aCeis Ca SaxDRC)Your job queue is full. Please wait for a job to finish first, then resubmit this one.Please check the bottom of the channel for more information.Ee eeaa) ace ac} aceCreate a watercolor realm of fantasy Envision mythical creatures, floating islands, and ethereal landscapes that transport viewers to a dreamlikePCRs CM cr ex Olete ene)SMCRIe ret Cacao aac ain_ P saneer oooe tice
# """
# test2 = """
# Activities CDK) Aug23 18:03 & & vi & 4) 1M 100%; CO eC ea} er ee 3a | cy ae eee oer @ Midjourney Bot Oa me Me ia age| a] ayy AA COCs you a oxrit ® Nitroes ee Dra> Weer i 8- (2 O Dee Ce Cue oa CeCe ea eT cet a Cu em ccc er Coan ead5° 6 Crees Lol uel uae \d --s 750 --v 5.1- @bcboss (relaxed AmTEU Leal Ue CURR a ed REO eA) Pe SeaAse taala7 , BaerY=) — sors« ie E om. lene UE cee hues sai}i) ear Be = ae under 60 seconds using the /imagine| a Sd 3 Senawe i ~ aSSS https://docs midjourney.com/docs/terms-of-Peayi * DISCORD MEMBER SINCEi A BrUPL eedas y .? { = eh& - i i iis —Nee] " Cree enB ie weDRC)Ngee ete sera ev eet aePlease check the bottom of the channel for more information.Uy Ld LK re iaa) ace ac} aceraspberry donut sublimation clipart, watercolor clipart, white background, detailed clipart, very detailed, Cartoon,hyper realistic, intricate detail,illustration style, high solution,on the white background --s 750 --v 5.1 - @bcboss (relaxed)RnR Ten eae meee aac ain_ P saneer oooe tice
# """
# test3 = """
# Activities CDK) Aug23 18:27 & & vi & 4) 1M 100%; CO eC ea} er ee 3| cy ae eee eee @ Midjourney Bot (Oa ee Se Me Wort aca ee aa 2 |me 75. ‘TatePe] TCs te pe coated TEC MECCpe easo s ee) — . =®D Nitro ae i a, i td a4 Se = Perec cee eta Deanery 4 Peery_ PO sa quality, detailed clipart, whiteSee) @ Data eae Pe eC Cece Mer toea DTT Ree a a eC Ne nae ice“= - Pee ee ate cea age ogee illustration style, high solution, on thean Pees et meee eee. e “ vl v7 We) W3 Site. aiaty() @ (CT Midjourney Bot black gothic color beautiful mushroom fairy house sublimation clipart, high quality, detailed clipart, white background, very detail ( Be A 5o 5 | ie MS dea ae aoe eno Sa heblack gothic color beautiful mushroom fairy house sublimation clipart, high quality, detailed clipart, white background, very detailed, ae Cartoon, hyper realistic, intricate detall, illustration style, high solution, on the white background --s 750 --v 5.1 - Image #1 @bcboss/ Se fe 5- KU, ee3 | t= ~ Ja ¥ x. ca aC) ae}NS vn S eeep = * Sart eee ne oe a2k yee a Please check the bottom of the channel forSD a eee aeraee t% phoalg Reyed | SMeSas of 1 Srl mee — ee ee ed eae= oa Ie US: 1a a ea eTren Coes rcaarea ean Carnac ccm ri= white background, very detailed,bees ae ees PD CTU mC Cenkillustration style, high solution, on the- = = =SO ee a Re ere ad CS CTT Bae ae@beboss (relaxed)aes NBee bebose ° zOBbe oess e
# """
# pattern1 = "(Your job queue is full)"
# pattern2 = "(Please check the bottom of the channel)"
# if re.search(pattern1, test2) or re.search(pattern2, test2):
#     print(True)
