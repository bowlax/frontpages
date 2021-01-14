# Main class which returns the feed.xml
import frontpageTweets
import datetime
from email import utils

class feed:
    title = "frontpages"
    link = "https://twitter.com/hashtag/TomorrowsPapersToday?src=hashtag_click"         #
    desc = "RSS feed showing today's hashtag TomorrowsPapersToday"
    language = "en-us"
    imgLink = "https://twitter.com/hashtag/TomorrowsPapersToday?src=hashtag_click"      #link to where the feed image goes (not the item image)
    imgURL = "https://images.app.goo.gl/HA6GnKi1UTbHNYbd6"                              #url to image source - twitter logo :)
    imgWidth = "20"
    imgHeight = "20"
    lastBuildDate = datetime.datetime.today() - datetime.timedelta(days=1, hours=8)     #start from a day ago

    def getFeedXML(self):
        xml = self.getXMLHeader() + self.getXMLBody() + self.getXMLFooter()
#        print(xml)
        return xml


    def getXMLBody(self):
        xmlBody = ""
        #read updates from the last time the XML got built, then reset
        todaysTweets = frontpageTweets.getTodaysTweets(self.lastBuildDate)
        self.lastBuildDate = datetime.datetime.today()
        
        #build a dictionary of the imageUrl by the media_key
        image_dict = {}
        image_json = todaysTweets["includes"]["media"]
        for j in image_json:
            image_dict[j["media_key"]] = j["url"]

        #create an rss <item> for each tweet
        for i in todaysTweets['data']:
            text = i["text"]
            tweet = text[0:text.find('#')-1] #parse out the headline, ignore the hashtag
            link = text[text.find('http'):] #parse out the url that twitter provides at the end of the text

            xmlBody = xmlBody + "<item>"
            xmlBody = xmlBody + "<guid isPermaLink=\"true\">" + link + "</guid>" #url is the permalink
            xmlBody = xmlBody + "<title><![CDATA[" + tweet + "]]></title>" #headline
            xmlBody = xmlBody + "<pubDate>" + self.isoDateToRFC822(i["created_at"]) + " GMT</pubDate>" #format the date
            xmlBody = xmlBody + "<link>" + link + "</link>" #url is also the tweet link (obvs)
            imgUrl = image_dict[i["attachments"]["media_keys"][0]] # get the front page image url
            xmlBody = xmlBody + "<enclosure url=\"" + imgUrl + "\" length=\"0\" type=\"image/jpeg\" />" #some readers use enclosure
            xmlBody = xmlBody + "<description><![CDATA[ <a href=\"" + link + "\">" + tweet + "</a> <br /> <img src=\"" + imgUrl + "\" /> ]]></description>" #some use the desc
            xmlBody = xmlBody + "</item>"

        return xmlBody

    def getXMLHeader(self):
        xmlHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        xmlHeader = xmlHeader + "<rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">"
        xmlHeader = xmlHeader + "<channel>"
#        xmlHeader = xmlHeader + "<atom:link href=\"http://dallas.example.com/rss.xml\" rel=\"self\" type=\"application/rss+xml\" />" 
        xmlHeader = xmlHeader + "<title>" + self.title + "</title>"
        xmlHeader = xmlHeader + "<link>" + self.link + "</link>"
        xmlHeader = xmlHeader + "<description>" + self.desc + "</description>"
        xmlHeader = xmlHeader + "<language>" + self.language + "</language>"
        xmlHeader = xmlHeader + "<lastBuildDate>" + self.isoDateToRFC822(self.lastBuildDate.isoformat() + "Z") + "</lastBuildDate>" # hacking on a Z so the parsing works
        xmlHeader = xmlHeader + "<ttl>1</ttl>" #minutes
        xmlHeader = xmlHeader + "<image>"
        xmlHeader = xmlHeader + "<title>" + self.title + "</title>"
        xmlHeader = xmlHeader + "<link>" + self.imgLink + "</link>"
        xmlHeader = xmlHeader + "<url>" + self.imgURL + "</url>"
        xmlHeader = xmlHeader + "<width>" + self.imgWidth + "</width>"
        xmlHeader = xmlHeader + "<height>" + self.imgHeight + "</height>"
        xmlHeader = xmlHeader + "</image>"
        return xmlHeader

    def getXMLFooter(self):
        xmlFooter = "</channel></rss>"
        return xmlFooter

    def isoDateToRFC822(self, d):
        return datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%a, %d %b %Y %H:%M:%S')

