# Mini1 Project 1 --- A Effective Time-Variating Sentiment Evaluating Tool Towards Specific Topic Based on Twitter API

<h2>Abstract:</h2>
nowadays, social media has generated significant impact on people’s life from public to everyone’s life. 	every individual can share and spread their sentiment and altitude towards events and heart point, and some of which are positive and some are negtive. Researching on these altitudes are quite valuable.  By using the sentiment evaluating tools, the user can grab people’s altitude and make in time adjustment to their behavior. In this project, a tool base on Twitter has been applied to meet the demands. 


<h2>introduction:</h2>
With the development of Internet, millions of web users spend hours a day on the website, especially on social networks. By December 2013, the number of Chinese internet users reached 618 million. The usage rate of social web is 45.0% (CNNIC33). People read news and write their views and opinions about online hot events and commodities [1]. Therefore, people’s posts constitute online public opinions. These opinions and views reflect people’s sentiments. The sentiments in social networks can affect people’s purchase behavior [2], the sellers’ marketing plan [3], political trends [4, 5] and effectively forecast stock market [6]. Moreover, many online hot events change trends with time going by. With the development of the events and increasing comments, the sentiment of users contained in the comments also varies.

In order to get different sentiment orientation of posts, we need to apply the sentiment analysis approach, whose one of purposes is to classify the attitude expressed in the text (such as positive or negative) [8]In order to get different sentiment orientation of posts, we need to apply the sentiment analysis approach, whose one of purposes is to classify the attitude expressed in the text (such as positive or negative) [8]

<h2>User Story:</h2>
The MVP in this project is to get sentiment analysis in a time period and analysis people’s sentiments changes over time. This is of particular interest for public figures to see how their sentiment changes over time and how people view the public figures.

<h2>Target Users:</h2>
This tool is designed for people who want to analyze a specific person’s change over time. You could track how a specific politician's sentiment changes throughout their campaign or time in office. With more commputing power, the program could easily be changed to analyze how people twitter view Politician's. Politician could change their election strategies according to the sentiment analysis result; movie actor/actress can evaluate his/her performance by the comments on Twitter. 

<h2>User Story:</h2>
 1. As a politician (Trump, Democratic Prez Candidate, etc.), I want to be able to track the live twitter reaction during a big public event like a debate or press conference.  
 
 2. As a star sports player (Football- Tom Brady, Basketball- Lebron James, Soccer- Messi) I want to be able to track the live twitter reaction during a game/season.
 
 3. As a political rival I want to be able to track how my opponent's sentiment changes overtime to see if our strategies affecting them. 
 
<h2>Description of How to Use the Program:</h2>

The program is primarily stored in the file: time.py. Edit the code on lines 146 and 147 to select the twitter handle you want to analyze and the number of tweets you want to be analyzed. The code will not run if you do not enter in the proper credential information. Enter your twitter keys in the file twitter_codes.py and they will be imported to time.py file. In the terminal you are working in type "export GOOGLE_APPLICATION_CREDENTIALS = 'PATH'" where 'PATH' is the path to where your google credentials are stored in the computer. In the terminal if you type "python time.py" it should output your time trend sentiment graph for the twitter handle you provided.

<h2>Architecture&Flowchart:</h2>
 


![image](https://github.com/mbu54/mini1/blob/master/IMG/Architecture.jpg) 
This project is based on PC. The tool search for Twitter content and the corresponding	time by using Twitter API. The collected contentdata was then convert to the easy-read type for the Google API, while the time would be analyzed with analyzed data from the Google NLP Engine. The final result would be displayed in user end.

![image](https://github.com/mbu54/mini1/blob/master/IMG/EC601_py.jpg)
The diagram shows how the Twitter program works. There are three types functions named Hashtags Searching,  Twitter Time Grab and User Timeline Grab. Timeline function are not used in the program. The desired data from the hashtags are time and content, the other repeated information such as “https://XXXX.XXX.XXX” should be striped. These two ruction would return data and time with easy-read data type for further analysis.


 
  
<h2>References:</h2>

1.  Balali A, Faili H, Asadpour M (2014) A Supervised Approach to Predict the Hierarchical Structure of Conversation Threads for Comments. Scientific World Journal: 23: 479746  https://www.hindawi.com/journals/tswj/2014/479746/abs/  
2. Bai X (2011) Predicting consumer sentiments from online text. Decision Support Systems 50: 732–742.https://www.sciencedirect.com/science/article/pii/S016792361000148X 
3.  Liu Y, Huang X, An A, Yu X (2007) ARSA: A sentiment-aware model for predicting sales performance using blogs, In Proceedings of the 30th annual international ACM SIGIR conference on research and development in information retrieval, New York: 607–614.https://journals.sagepub.com/doi/abs/10.1177/1461444811422894 
4.  Larsson AO, Moe H (2012) Studying political microblogging: Twitter users in the 2010 Swedish election campaign. New Media & Society 14: 729–747.https://journals.sagepub.com/doi/abs/10.1177/1461444811422894 
5.  Williams C, Gulati G (2008) What is a social network worth? Facebook and vote share in the 2008 presidential primaries. In the annual meeting of the American political science association. Boston, MA: 1–17. 	
6.  Eirinaki M, Pisal S, Singh J (2012) Feature-based opinion mining and ranking. Journal of Computer and System Sciences 78: 1175–1184.https://www.sciencedirect.com/science/article/pii/S0022000011001139 

7.  Zhi HD, Kun HL, Hong LY (2014) A study of supervised term weighting scheme for sentiment analysis. Expert Systems with Applications.41:3506–3513 https://www.sciencedirect.com/science/article/pii/S0957417413008737



			
      
 
   
   
