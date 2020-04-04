import xml.etree.ElementTree as ET
import urllib.request
import re
import requests
import os
import time
import openpyxl
import json
import difflib

anidbkehuduan=""   #anidb申请的api客户端名称，默认版号为1(用于获取Anidn-API返回的XML数据)

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Cookie': '__cfduid=de0059a8637a27a6a30556ff3b206a36c1585728544; chii_theme=light; __utma=1.1290609121.1585728548.1585728548.1585728548.1; __utmc=1; __utmz=1.1585728548.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); chii_sid=62r3E8; __utmt=1; chii_searchDateLine=1585732454; __utmb=1.11.10.1585728548'
    }
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
def save_api_anidb(anidb):#保存API返回的XML数据
    Anidb_xml="%s.xml" %(anidb)
    idurl = "http://api.anidb.net:9001/httpapi?request=anime&client=%s&clientver=1&protover=1&aid=%s" %(anidbkehuduan,anidb)
    idhtml = requests.get(idurl,headers=ua_headers)
    f = open(Anidb_xml, "w",encoding="utf-8")
    for i in idhtml.text:
        f.write(i)
    f.close()

def jiexi_Anidb_z(Anidb):#返回XML里的中文名
	Anidb_xml="%s.xml" %(Anidb)
	with open(Anidb_xml, "r",encoding='utf-8') as f:
		data = f.read()
		Anidb_z=re.findall(r'<title xml:lang="zh-Hans" type="official">(.*)</title>',data)[0]
	return Anidb_z

def jiexi_Anidb_y(Anidb):#返回XML里的英文名
	Anidb_xml="%s.xml" %(Anidb)
	with open(Anidb_xml, "r",encoding='utf-8') as f:
		data = f.read()
		Anidb_y=re.findall(r'<title xml:lang="en" type="official">(.*)</title>',data)[0]
	return Anidb_y

def jiexi_Anidb_r(Anidb):#返回XML里的日文名
	Anidb_xml="%s.xml" %(Anidb)
	with open(Anidb_xml, "r",encoding='utf-8') as f:
		data = f.read()
		Anidb_r=re.findall(r'<title xml:lang="ja" type="official">(.*)</title>',data)[0]
	return Anidb_r

def jiexi_Anidb_l(Anidb):#返回XML里的罗马音
	Anidb_xml="%s.xml" %(Anidb)
	with open(Anidb_xml, "r",encoding='utf-8') as f:
		data = f.read()
		Anidb_l=re.findall(r'<title xml:lang="x-jat" type="main">(.*)</title>',data)[0]
	return Anidb_l

def jiexi_Anidb_time(Anidb):#返回XML里的时间
	Anidb_xml="%s.xml" %(Anidb)
	with open(Anidb_xml, "r",encoding='utf-8') as f:
		data = f.read()
		Anidb_time=re.findall(r'<startdate>(.*)</startdate>',data)[0]
	return Anidb_time

def jiexi_Anidb_haibao(Anidb):#返回XML里jpg ID
	Anidb_xml="%s.xml" %(Anidb)
	tree = ET.ElementTree(file=Anidb_xml)
	root = tree.getroot()
	for child in root:
		try:
			if re.findall('jpg',child.text)[0] == "jpg":
				Anidb_jpg = child.text
		except:
			pass
	return Anidb_jpg

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
def get_equal_rate_1(str1, str2):# 字符串对比
	return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

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
	bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid1
	bgmid_name_Z_jizu=bgmid
	if len(bgmid) != 1:
		time.sleep(3)
		idhtml = requests.get(name_Z_mohu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid2
		bgmid_name_Z_mohu=bgmid
	if len(bgmid) != 1:
		time.sleep(3)
		idhtml = requests.get(name_R_jizu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid3
		bgmid_name_R_jizu=bgmid
	if len(bgmid) != 1:
		time.sleep(3)
		idhtml = requests.get(name_R_mohu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid4
		bgmid_name_R_mohu=bgmid
	if len(bgmid) != 1:
		time.sleep(3)
		idhtml = requests.get(name_Y_jizu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid5
	if len(bgmid) != 1:
		time.sleep(3)
		idhtml = requests.get(name_Y_mohu,headers=ua_headers)
		idhtml=idhtml.text
		bgmid=re.findall(r'<a href="/subject/(.*)" class="l">',idhtml)#bgmid6
	#print(bgmid_name_Z_jizu)   #3
	#print(bgmid_name_Z_mohu)   #4
	#print(bgmid_name_R_jizu)   #1
	#print(bgmid_name_R_mohu)   #2
	if len(bgmid) != 1:
		bgmid=[]
		for diffaa in bgmid_name_R_jizu:
			time.sleep(3)
			apiurl="http://api.bgm.tv/subject/%s" %(diffaa)
			apiurlhtml = requests.get(apiurl,headers=ua_headers)
			apiurlhtml = apiurlhtml.text
			apiurltext = json.loads(apiurlhtml)
			duibidu=get_equal_rate_1(apiurltext['name'],name_R)
			if duibidu == 1.0:
				bgmid.append(diffaa)
				break
	if len(bgmid) != 1:
		bgmid=[]
		for diffaa in bgmid_name_R_mohu:
			time.sleep(3)
			apiurl="http://api.bgm.tv/subject/%s" %(diffaa)
			apiurlhtml = requests.get(apiurl,headers=ua_headers)
			apiurlhtml = apiurlhtml.text
			apiurltext = json.loads(apiurlhtml)
			duibidu=get_equal_rate_1(apiurltext['name'],name_R)
			if duibidu == 1.0:
				bgmid.append(diffaa)
				break
	if len(bgmid) != 1:
		bgmid=[]
		for diffaa in bgmid_name_Z_jizu:
			time.sleep(3)
			apiurl="http://api.bgm.tv/subject/%s" %(diffaa)
			apiurlhtml = requests.get(apiurl,headers=ua_headers)
			apiurlhtml = apiurlhtml.text
			apiurltext = json.loads(apiurlhtml)
			duibidu=get_equal_rate_1(apiurltext['name_cn'],name_Z)
			if duibidu == 1.0:
				bgmid.append(diffaa)
				break
	if len(bgmid) != 1:
		bgmid=[]
		for diffaa in bgmid_name_Z_mohu:
			time.sleep(3)
			apiurl="http://api.bgm.tv/subject/%s" %(diffaa)
			apiurlhtml = requests.get(apiurl,headers=ua_headers)
			apiurlhtml = apiurlhtml.text
			apiurltext = json.loads(apiurlhtml)
			duibidu=get_equal_rate_1(apiurltext['name_cn'],name_Z)
			if duibidu == 1.0:
				bgmid.append(diffaa)
				break
	if len(bgmid) != 1:
		bgmid=[]
	return bgmid

#print(bgmtv("我的妹妹哪有这么可爱.","Ore no Imouto ga Konna ni Kawaii Wake ga Nai.","俺の妹がこんなに可愛いわけがない."))

print(jiexi_Anidb_z(8692))
print(jiexi_Anidb_y(8692))
print(jiexi_Anidb_r(8692))
print(jiexi_Anidb_l(8692))
print(jiexi_Anidb_time(8692))
print(jiexi_Anidb_haibao(8692))
