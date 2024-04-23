from bs4 import BeautifulSoup
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

html = '''
<div id="bz_assignee_edit_container" class="">
    <span><span class="vcard">
        <a class="email" href="mailto:tim.orling@konsulko.com" title="Tim Orling <tim.orling@konsulko.com>">
            <span class="fn">Tim Orling</span>
        </a>
    </span>
    (<a href="#" id="bz_assignee_edit_action">edit</a>)
    (<a title="Reassign to yourself" href="#" id="bz_assignee_take_action">take</a>)
    </span>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
email_link = soup.find('a', class_='email')

print(email_link)