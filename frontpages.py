# Main class which returns the feed.xml
import frontpageTweets
from datetime import datetime
from email import utils

class feed:
    title = "frontpages"
    link = "https://twitter.com/hashtag/TomorrowsPapersToday?src=hashtag_click"
    desc = "RSS feed showing today's hashtag TomorrowsPapersToday"
    language = "en-us"
    imgLink = "https://twitter.com/hashtag/TomorrowsPapersToday?src=hashtag_click"     #link to where the image goes
    imgURL = "https://images.app.goo.gl/HA6GnKi1UTbHNYbd6"      #url to image source
    imgWidth = "20"
    imgHeight = "20"

    eol = "\n"
    indent = "   "

    def getFeedXML(self):
        xml = self.getXMLHeader() + self.getXMLBody() + self.getXMLFooter()
        return xml


    def getXMLBody(self):
        xmlBody = ""
        todaysTweets = frontpageTweets.getTodaysTweets()
        image_dict = {}
        image_json = todaysTweets["includes"]["media"]
        for j in image_json:
            image_dict[j["media_key"]] = j["url"]

        for i in todaysTweets['data']:
            text = i["text"]
            tweet = text[0:text.find('#')-1]
            link = text[text.find('http'):]

            xmlBody = xmlBody + "<item>" + self.eol
            xmlBody = xmlBody + self.indent + "<guid>" + link + "</guid>" + self.eol
            xmlBody = xmlBody + self.indent + "<title>" + tweet + "</title>" + self.eol
            xmlBody = xmlBody + self.indent + "<pubDate>" + datetime.strptime(i["created_at"], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%a, %d %b %Y %H:%M:%S') + " GMT</pubDate>" + self.eol
            xmlBody = xmlBody + self.indent + "<link>" + link + "</link>" + self.eol
            xmlBody = xmlBody + self.indent + "<description>" + tweet + " <a href=\"" + link + "\">" + link + "</a><img src=\"" + image_dict[i["attachments"]["media_keys"][0]] + "\"/></description>" + self.eol
            xmlBody = xmlBody + "</item>" + self.eol

        return xmlBody

    def getXMLHeader(self):
#        xmlHeader = "HTTP/1.1 200 OK\nCache-Control: private, s-maxage=0\nContent-Type: application/xml; charset=utf-8\nServer: Microsoft-IIS/8.0n"

        xmlHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + self.eol

        xmlHeader = xmlHeader + "<rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">" + self.eol
        xmlHeader = xmlHeader + "<channel>" + self.eol
        xmlHeader = xmlHeader + "<atom:link href=\"http://dallas.example.com/rss.xml\" rel=\"self\" type=\"application/rss+xml\" />"  + self.eol
        xmlHeader = xmlHeader + "<title>" + self.title + "</title>" + self.eol
        xmlHeader = xmlHeader + "<link>" + self.link + "</link>" + self.eol
        xmlHeader = xmlHeader + "<description>" + self.desc + "</description>" + self.eol
        xmlHeader = xmlHeader + "<language>" + self.language + "</language>" + self.eol
        xmlHeader = xmlHeader + "<image>" + self.eol
        xmlHeader = xmlHeader + self.indent + "<title>" + self.title + "</title>" + self.eol
        xmlHeader = xmlHeader + self.indent + "<link>" + self.imgLink + "</link>" + self.eol
        xmlHeader = xmlHeader + self.indent + "<url>" + self.imgURL + "</url>" + self.eol
        xmlHeader = xmlHeader + self.indent + "<width>" + self.imgWidth + "</width>" + self.eol
        xmlHeader = xmlHeader + self.indent + "<height>" + self.imgHeight + "</height>" + self.eol
        xmlHeader = xmlHeader + "</image>" + self.eol
        return xmlHeader

    def getXMLFooter(self):
        xmlFooter = "</channel></rss>"
        return xmlFooter

