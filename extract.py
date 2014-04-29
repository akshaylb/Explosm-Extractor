import urllib, mechanize, re, os
br=mechanize.Browser()
os.makedirs('C&HComics')
os.chdir('C&HComics')
def getcomic(path):
    source=urllib.urlopen(path).read()
    for m in re.findall('http://www.explosm.net/db/files/Comics/[-\w/]+\.(?:jpg|gif|png)', source):
		print m
		parts=m.split('/')
		if not parts[-2]=='Comics':
			if not os.path.exists(parts[-2]):
				os.makedirs(parts[-2])
		file=urllib.urlopen(m).read()
		outputfile=open(parts[-2]+'/'+parts[-1],'wb')
		outputfile.write(file)
		outputfile.close
    br.open(path)
    rs=br.follow_link(text_regex=r"Previous")
    print rs.geturl()
    getcomic(rs.geturl())
    return

getcomic("http://explosm.net/comics/3535/")	