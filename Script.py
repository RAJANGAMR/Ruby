class script(object):
    START_TXT = """ššššš {}šā¤ļøāš„ 
\nš ššš ššššššš šššššš & šššššš šš ššš šššš ššššššš šš ššššš šā¤ļøāš„   \nšššš ššš šš šš šššš ššššš & ššššš š„³š"""
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš šš·š“ š·š“š»šæ šµš¾š š¼š š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """āæ  š¼š š½š°š¼š“: {}

āæ  š²šš“š°šš¾š: <a href=https://t.me/ABHINAND3510>AŅBŅHŅIŅNŅAŅNŅDŅ</a>

āæ  š»šøš±šš°šš & š»š°š½š¶: šæššš¾š¶šš°š¼ | šæššš·š¾š½ š¹

āæ  š³š°šš°š±š°šš“ & šš“ššš“š: š¼š¾š½š¶š¾š³š± | š·š“šš¾šŗš

āæ  š±ššøš»š³ ššš°ššš: v1.0.1 [ š±š“šš° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/thefilmyspot

<b>DEVS:</b>
- <a href=https://t.me/thefilmyspot>RUBY šš</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/RubymathewsBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message Heheš)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my database ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of RUBYš

<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specified user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my adminsš¼

<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code> š
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š¶šš¾ššæš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> 
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
