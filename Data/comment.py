'''
Comment.py: a comment class that encapsulates all attributes of our comment objects
by Cole Hanson, Chait Sayani and James Craig
'''

import time

class Comment():

    #initial constructor defining comment attributes
    def __init__(self):
        self.subreddit = ""
        self.subreddit_ID = ""
        self.author = ""
        self.score = 0
        self.stickied = ""
        self.linkID = ""
        self.body = ""
        self.contoversiality = 0
        self.retrieved_on = 0
        self.edited = ""
        self.ID = ""
        self.guilded = 0
        self.parent_ID = ""
        self.created_UTC = ""
        self.sentiment = 0

    #retreives comment author
    def getAuthor(self):
        '''
        Retrieves the author of a comment

		Returns:
			author of the comment (str)
        '''
        return self.author

    #sets comment author
    def setAuthor(self, author):
        '''
        sets the author of a comment

        Parameters:
            author - the author of the comment
        '''
        self.author = author

    #retreives comment score
    def getScore(self):
        '''
        Retrieves the score of a comment

		Returns:
			score of the comment (int)
        '''
        return self.score

    #sets comment score attribute
    def setScore(self, score):
        '''
        sets the score of a comment

        Parameters:
            score - the score of the comment
        '''
        self.score = score

    def getBody(self):
        '''
        Retrieves the body(text) of a comment

		Returns:
			body of the comment (str)
        '''
        return self.body

    def setBody(self, body):
        '''
        sets the body(text) of a comment

        Parameters:
            body - the body of the comment
        '''
        self.body = body

    def getControversiality(self):
        '''
        Retrieves the controversiality of a comment

		Returns:
			controversiality of the comment (int)
        '''
        return self.controversiality

    def setControversiality(self, controversiality):
        '''
        sets the controversiality of a comment

        Parameters:
            controversiality - the controversiality of the comment (int)
        '''
        self.controversiality = controversiality

    def getEdited(self):
        '''
        Retrieves the edited status of a comment

		Returns:
			edited status of a comment ('TRUE'/'FALSE')
        '''
        return self.edited

    def setEdited(self, edited):
        '''
        sets the edited status of a comment

        Parameters:
            edited - the edited status of the comment ('TRUE'/'FALSE')
        '''
        if edited.isalpha():
            self.edited = "FALSE"
        else:
            self.edited = "TRUE"

    def getGuilded(self):
        '''
        Retrieves the guilded status of a comment

		Returns:
			guilded status of the comment (int)
        '''
        return self.guilded

    def setGuilded(self, guilded):
        '''
        sets the guilded status of a comment

        Parameters:
            guilded - the guilded status of the comment
        '''
        self.guilded = guilded


    def getTimeCreated(self):
        '''
        Retrieves the time a comment was created in UTC

		Returns:
			The time a comment was created (int)
        '''
        return self.created_UTC

    def setTimeCreated(self, UTCtime):
        '''
        sets the time of creation (converted from UTC to local time)

        Parameters:
            time - the time a comment was created
        '''
        self.created_UTC = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(UTCtime))


    def getSentiment(self):
        '''
        Retrieves the sentiment score (-1,1) of a comment

		Returns:
			The sentiment score of a comment (float)
        '''
        return self.sentiment

    def setSentiment(self, sentimentScore):
        '''
        sets the sentiment score of a comment

        Parameters:
            sentimentScore - sentiment score of a comment (from -1 to 1)
        '''
        self.sentiment = sentimentScore

    def getLink(self):
        '''
        Retrieves the sentiment score (-1,1) of a comment

		Returns:
			The sentiment score of a comment (float)
        '''
        return self.linkID

    def setLink(self, link):
        '''
        sets the sentiment score of a comment

        Parameters:
            sentimentScore - sentiment score of a comment (from -1 to 1)
        '''
        self.linkID = link[3:]
