# Main class which returns the feed.xml
import frontpageTweets

class feed:
    title = "frontpages"
    link = "TBD"
    desc = "TBD"
    language = "en-us"
    imgTitle = "TBD"
    imgLink = "TBD"     #link to where the image goes
    imgURL = "TBD"      #url to image source
    imgWidth = "10"
    imgHeight = "10"
        
    def getFeedXML(self):
        xml = self.getXMLHeader() + self.getXMLBody() + self.getXMLFooter()
        return xml

    def getXMLBody(self):
        xmlBody = ""
        todaysTweets = frontpageTweets.getTodaysTweets()
        for i in todaysTweets['data']:
            text = i["text"]
            tweet = text[0:text.find('#')-1]
            link = text[text.find('http'):]
            print(link)

            xmlBody = xmlBody + "<item><title>" + tweet + "</title>"
#            xmlBody = xmlBody + "<pubDate>" + print(i["created_at"]) + "</pubDate>"
            xmlBody = xmlBody + "<link>" + link + "</link>"
            xmlBody = xmlBody + "<description><![CDATA[" + tweet + "]]></description>"
            xmlBody = xmlBody + "</item>"

        print(xmlBody)
        return xmlBody

    def getXMLHeader(self):
#        xmlHeader = "HTTP/1.1 200 OK\nCache-Control: private, s-maxage=0\nContent-Type: application/xml; charset=utf-8\nServer: Microsoft-IIS/8.0n"
#        xmlHeader = xmlHeader + "<?xml version=\"1.0\" encoding=\"UTF-8\"?><rss version=\"2.0\"><channel>"
        xmlHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

        xmlHeader = xmlHeader + "<rss version=\"2.0\"><channel>"
        xmlHeader = xmlHeader + "<title>" + self.title + "</title>"
        xmlHeader = xmlHeader + "<link>" + self.link + "</link>"
        xmlHeader = xmlHeader + "<description>" + self.desc + "</description>"
        xmlHeader = xmlHeader + "<language>" + self.language + "</language>"
        xmlHeader = xmlHeader + "<image>"
        xmlHeader = xmlHeader + "<title>" + self.imgTitle + "</title>"
        xmlHeader = xmlHeader + "<link>" + self.imgLink + "</link>"
        xmlHeader = xmlHeader + "<url>" + self.imgURL + "</url>"
        xmlHeader = xmlHeader + "<width>" + self.imgWidth + "</width>"
        xmlHeader = xmlHeader + "<height>" + self.imgHeight + "</height>"
        xmlHeader = xmlHeader + "</image>"
        return xmlHeader

    def getXMLFooter(self):
        xmlFooter = "</channel></rss>"
        return xmlFooter

