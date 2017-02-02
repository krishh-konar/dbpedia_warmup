# dbpedia-warmup
Warm-up tasks for dbpedia

##DBpedia Chatbot
A simple interactive bot that translates english and arabic numbers into roman number.

### Usage
run the script: `python arabic_roman.py` and then type in the queries. Type `exit` to quit.

Examples: 

- 'translate 145 into roman numbers'
- 'translate 2012 to roman'
- 'translate ٣٨٦ to roman'

It also supports multiple number translations at once (comma or space seperate).

- 'translate ٣٨٦, ٣ to roman'


Output: 
`
>>  translate 145 into roman numbers
145 : ( 145 )  CXLV

>>  translate 2012 to roman
2012 : ( 2012 )  MMXII

>>  translate ٣٨٦ to roman
٣٨٦ : ( 386 )  CCCLXXXVI

>> translate ٣٨٦, ٣ to roman
٣٨٦, : ( 386 )  CCCLXXXVI
٣ : ( 3 )  III
'
