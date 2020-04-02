import xml.etree.ElementTree as ET
import urllib.request
import re
import requests
import os
import time
import openpyxl

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Cookie': '__cfduid=de0059a8637a27a6a30556ff3b206a36c1585728544; chii_theme=light; __utma=1.1290609121.1585728548.1585728548.1585728548.1; __utmc=1; __utmz=1.1585728548.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); chii_sid=62r3E8; __utmt=1; chii_searchDateLine=1585732454; __utmb=1.11.10.1585728548'
    }

def bgmtv(name_Z,name_Y,name_R):
	name_Z_mohu = "https://bgm.tv/subject_search/%s?cat=2" %(name_Z)#2
	name_Y_mohu = "https://bgm.tv/subject_search/%s?cat=2" %(name_Y)#6
	name_R_mohu = "https://bgm.tv/subject_search/%s?cat=2" %(name_R)#4
	name_Z_jizu = "https://bgm.tv/subject_search/%s?cat=2&legacy=1" %(name_Z)#1
	name_Y_jizu = "https://bgm.tv/subject_search/%s?cat=2&legacy=1" %(name_Y)#5
	name_R_jizu = "https://bgm.tv/subject_search/%s?cat=2&legacy=1" %(name_R)#3
	time.sleep(3)
	idhtml = requests.get(name_Z_jizu,headers=ua_headers)
	idhtml=idhtml.text
	bgmid_Z_jizu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid1
	if len(bgmid_Z_jizu) != 1:
		time.sleep(3)
		idhtml = requests.get(name_Z_mohu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid_Z_mohu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid2
		if len(bgmid_Z_mohu) != 1:
			time.sleep(3)
			idhtml = requests.get(name_R_jizu,headers=ua_headers)
			idhtml=idhtml.text
			bgmid_R_jizu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid3
			if len(bgmid_R_jizu) != 1:
				time.sleep(3)
				idhtml = requests.get(name_R_mohu,headers=ua_headers)
				idhtml=idhtml.text
				bgmid_R_mohu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid4
				if len(bgmid_R_mohu) != 1:
					time.sleep(3)
					idhtml = requests.get(name_Y_jizu,headers=ua_headers)
					idhtml=idhtml.text
					bgmid_Y_jizu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml_Y_jizu)#bgmid5
					if len(bgmid_Y_jizu) != 1:
						time.sleep(3)
						idhtml = requests.get(name_Y_mohu,headers=ua_headers)
						idhtml=idhtml.text
						bgmid_Y_mohu=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid6
	return bgmid