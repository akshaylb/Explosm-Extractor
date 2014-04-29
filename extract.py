import urllib, mechanize, re, os
br=mechanize.Browser()
GLOBALDIR='C&HComics'
if not os.path.exists(GLOBALDIR):
	os.makedirs(GLOBALDIR)
os.chdir(GLOBALDIR)
def getcomic(path):
    print "Reading link "+path+" ..."
    source=br.open(path).read()
    imgpath=re.search('http://www.explosm.net/db/files/Comics/[-\w/]+\.(?:jpg|gif|png)', source).group(0)
    if imgpath:
		print "Found image path "+imgpath
		parts=imgpath.split('/')
		if not parts[-2]=='Comics':
			if not os.path.exists(parts[-2]):
				os.makedirs(parts[-2])
		file=urllib.urlopen(imgpath).read()
		pathname=parts[-2]+'/'+parts[-1]
		if not os.path.exists(pathname):
			outputfile=open(pathname,'wb')
			outputfile.write(file)
			outputfile.close
    rs=br.follow_link(text_regex=r"Previous")
    print "Found next link "+rs.geturl()
    getcomic(rs.geturl())
    return

getcomic("http://explosm.net/comics")	