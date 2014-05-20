import urllib, mechanize, re, os
br=mechanize.Browser()
logfile=open('logfile.txt','rb')
GLOBALDIR='C&HComics'
if not os.path.exists(GLOBALDIR):
	os.makedirs(GLOBALDIR)
os.chdir(GLOBALDIR)
def getcomic(path):
	if path.split('/')[-2]=='15':
		return
	print "Reading link "+path+" ..."
	source=br.open(path).read()
	imgpath=re.search('http://www.explosm.net/db/files/Comics/[-\w/]+\.(?:jpg|gif|png)', source)
	if imgpath:
		print "Found image path "+imgpath.group(0)
		parts=imgpath.group(0).split('/')
		if not parts[-2]=='Comics':
			if not os.path.exists(parts[-2]):
				os.makedirs(parts[-2])
			pathname=parts[-2]+'/'+path.split('/')[-2]+'_'+parts[-1]
		else:
			pathname=path.split('/')[-2]+'_'+parts[-1]
		if not os.path.exists(pathname):
			file=urllib.urlopen(imgpath.group(0)).read()
			outputfile=open(pathname,'wb')
			outputfile.write(file)
			outputfile.close
	rs=br.follow_link(text_regex=r"Previous")
	print "Found next link "+rs.geturl()
	getcomic(rs.geturl())
lastlink=re.findall('http://explosm.net/comics/[0-9]+/',logfile.read())
if lastlink:
	getcomic(lastlink[-1])
else:
	getcomic("http://explosm.net/comics")