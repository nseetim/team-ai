import urllib.request
from bs4 import BeautifulSoup as bs

# test urls - uncomment one url at a time 

# url_to_fetch = "http://www.pulse.ng/sports/manchester-united-liverpool-draw-0-0-id7460504.html"
url_to_fetch = "http://www.pulse.ng/entertainment/celebrities/5-celebrities-who-died-just-before-their-prime-id7447346.html"
# url_to_fetch = "http://www.pulse.ng/sports/football/arsene-wenger-manager-admits-ozil-sanchez-could-leave-in-january-id7451069.html"
# url_to_fetch = "http://www.pulse.ng/sports/football/barcelona-fc-what-next-for-football-club-in-case-of-catalan-independence-id7443368.html"
# url_to_fetch = "http://www.pulse.ng/news/politics/femi-adesina-calls-ezekwesili-a-wailing-wailer-id7465827.html"
# url_to_fetch = "http://www.pulse.ng/entertainment/celebrities/omotola-hubby-get-raunchy-in-pool-pics-id7463976.html"

# query the url, get the html to the variable ‘page’
# returns Beautiful Soup Object

def get_article(url):
	url_to_fetch = url
	
	page = urllib.request.urlopen(url_to_fetch).read()
	soup = bs(page, 'html.parser')

	return soup
	
# returns the Headline of particular blog post
# accepts beautiful soup object of the page in question

def get_head_line(BeautifulSoupObject):
	soup = BeautifulSoupObject
	head_line = soup.find('div', attrs={"class",'vspace'})
	return head_line.h2
	

# returns a list of objects of images in a particular blog post
# accepts beautiful soup object of the page in question

def get_picture_urls(BeautifulSoupObject):
	blog_images = []
		
	soup_obj = BeautifulSoupObject
	pictures_url = soup.find_all('img', attrs={"class",'centeredPicture'})	

	for x in range(0,len(pictures_url)):
		img_dict = {} # create img_dict on the fly
		img_dict['url'] = pictures_url[x]['src']
		img_dict['alt'] = pictures_url[x]['alt']
		
		blog_images.append(img_dict)
	
	print(blog_images)

	return blog_images

# accepts Beautiful Soup Object
# returns the story, i.e the content of the article in question

def get_article_story(BeautifulSoupObject):
	soup_obj = BeautifulSoupObject

	story = soup.find_all('div', attrs={"class",'vspace'})[2]

	return story.get_text()

# accepts Beautiful Soup Object
# returns a snippet and sumamry of the article in question

def get_article_snippet(BeautifulSoupObject):
	soup_obj = BeautifulSoupObject

	snippet = soup.find('div', attrs={"class",'articleHeader'})
	return snippet.p.get_text()


def get_article_comments():
	pass

def get_options_from_social_media():
	pass


soup = get_article(url_to_fetch)
# get_picture_urls(soup)
get_article_story(soup)