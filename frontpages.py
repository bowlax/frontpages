import twitter
#api = twitter.Api(consumer_key=[consumer key],
#                  consumer_secret=[consumer secret],
#                  access_token_key=[access token],
#                  access_token_secret=[access token secret])
                  
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
        
    feedXML = "blah"

    def getFeedXML(self):
        xml = self.getXMLHeader() + self.getXMLBody() + self.getXMLFooter()
        return xml

    def getXMLBody(self):
        xmlBody = "<item><title></title><pubDate></pubDate><link></link><description><![CDATA[xxx]]></description></item>"
        return xmlBody

    def getXMLHeader(self):
        xmlHeader = "<?xml version=\"1.0\" encoding=\"utf-8\"?><rss version=\"2.0\"><channel>"
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

