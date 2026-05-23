---
base_model: sentence-transformers/all-MiniLM-L6-v2
library_name: setfit
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: will i be charged if i use my card in china
- text: speak it again slowly
- text: tell me today s date
- text: how s the weather in tallahassee
- text: make a chart of the different types of whales
inference: true
---

# SetFit with sentence-transformers/all-MiniLM-L6-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 256 tokens
- **Number of Classes:** 151 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label | Examples                                                                                                                                                                                                                                                               |
|:------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 98    | <ul><li>'what s the time of arrival on my new credit card'</li><li>'how long should i wait to get my new card when my old one was stolen'</li><li>'how long does it usually take for a new credit card to come'</li></ul>                                              |
| 107   | <ul><li>'i need to get some assistance figuring out how i can rollover my 401k please'</li><li>'how do i do a 401 k rollover'</li><li>'my 401k can i roll it over'</li></ul>                                                                                           |
| 78    | <ul><li>'give me manual on how to change oil'</li><li>'diy oil change and oil type'</li><li>'what oil do i need for my honda crv and how do i change it'</li></ul>                                                                                                     |
| 21    | <ul><li>'i want your new name to be joshua'</li><li>'i want to set your name to gaffigan'</li><li>'can i refer to you as mike from here on out'</li></ul>                                                                                                              |
| 2     | <ul><li>'set an alarm'</li><li>'i want to make an alarm'</li><li>'i need an alarm'</li></ul>                                                                                                                                                                           |
| 108   | <ul><li>'how can i find my routing number for el dorado'</li><li>'where should i go to find the routing number for well s fargo'</li><li>'i need to know bank of america s routing'</li></ul>                                                                          |
| 113   | <ul><li>'remove carrots from my shopping list and add soda'</li><li>'i d like to add pancake mix to my shopping list if it s not already there'</li><li>'please get milk removed from my shopping list and add bread'</li></ul>                                        |
| 95    | <ul><li>'do i have a reminder for our neighbor s anniversary'</li><li>'can you tell me all the reminders i have set on my reminder list'</li><li>'what items did i want to remember'</li></ul>                                                                         |
| 49    | <ul><li>'bye bye'</li><li>'it was enjoyable to chat with you'</li><li>'good speaking to you'</li></ul>                                                                                                                                                                 |
| 142   | <ul><li>'what hobbies do you do'</li><li>'what do you like to do in your spare time'</li><li>'what are your favorite things to do'</li></ul>                                                                                                                           |
| 93    | <ul><li>'will you give me some guidance on how to make ceviche'</li><li>'what steps are involved in making lasagna'</li><li>'look up easy to follow recipes for beef ribs'</li></ul>                                                                                   |
| 123   | <ul><li>'remind me that time is up in sixty minutes'</li><li>'who set up the numbers for it'</li><li>'can you please the timer'</li></ul>                                                                                                                              |
| 41    | <ul><li>'can you call my cellphone'</li><li>'i lost my phone'</li><li>'help me find my phone'</li></ul>                                                                                                                                                                |
| 83    | <ul><li>'what is the median salary for someone with an engineering degree'</li><li>'how can i breach a network'</li><li>'i would like to know how long a charge is suppose to last on my phone'</li></ul>                                                              |
| 146   | <ul><li>'what is your nationality'</li><li>'tell me where you were created'</li><li>'are you from europe'</li></ul>                                                                                                                                                    |
| 86    | <ul><li>'set my amex pin to 1234'</li><li>'i d like to change my pin number for my savings account'</li><li>'change pin to 1234 on account banner'</li></ul>                                                                                                           |
| 122   | <ul><li>'what s the current time please'</li><li>'the time is what'</li><li>'what time is it in the greenwich timezone'</li></ul>                                                                                                                                      |
| 51    | <ul><li>'tell me how busy macaroni grill will be around 8 pm'</li><li>'i wanna know how busy denny s is at 5 am'</li><li>'how many people do you think will be at applebees at 7'</li></ul>                                                                            |
| 77    | <ul><li>'i would like to know how much fat is in tbsp of olive oil'</li><li>'what are the nutrition facts for carrots'</li><li>'i want to know if pizza is healthy'</li></ul>                                                                                          |
| 60    | <ul><li>'will i be charged if i use my card in mexico'</li><li>'does my american express card have any international transaction fees'</li><li>'show me the international transactions fees for the zenith card'</li></ul>                                             |
| 58    | <ul><li>'i need a new house insurance plan'</li><li>'how do i get different terms on my insurance policy'</li><li>'what is the procedure for signing up for a new allstate plan'</li></ul>                                                                             |
| 149   | <ul><li>'which company made you'</li><li>'who created your ai program'</li><li>'whats the name of the person who made you'</li></ul>                                                                                                                                   |
| 67    | <ul><li>'i need to quick dinner suggestions'</li><li>'what can i make for dinner'</li><li>'i m feeling like a greek meal and need some suggestions'</li></ul>                                                                                                          |
| 9     | <ul><li>'find me a flight from nyc to la on march 1 returning on march 5'</li><li>'for the dates april 1st to the 7th find me round trip air tickets from la to sfo'</li><li>'book a flight from bangor to las vegas on may 1st and returning july 4th'</li></ul>      |
| 27    | <ul><li>'what should i put on the timer to cook this dish'</li><li>'how much time do i need to prepare chicken'</li><li>'how long to reheat chinese food'</li></ul>                                                                                                    |
| 40    | <ul><li>'tell me when my credit card expires'</li><li>'during what month will my card s expiration date fall on'</li><li>'how long do i ve got until my discovery card expires'</li></ul>                                                                              |
| 74    | <ul><li>'when will i get the next holiday with pay'</li><li>'what is my next day off'</li><li>'i need to know when the next holiday will be'</li></ul>                                                                                                                 |
| 88    | <ul><li>'i m going out of country what type of outlet plug do i need'</li><li>'what kind of plug is used in japan'</li><li>'does england require socket converters'</li></ul>                                                                                          |
| 23    | <ul><li>'can you permanently talk faster'</li><li>'is it possible to speed up of your replies'</li><li>'please slow down i can t understand you'</li></ul>                                                                                                             |
| 109   | <ul><li>'can someone look at my check engine light'</li><li>'i need an oil change make an appointment'</li><li>'i want to get an appointment to get my oil changed'</li></ul>                                                                                          |
| 55    | <ul><li>'are you able to switch butter and oil'</li><li>'is it okay to substitute oregano for basil'</li><li>'is butter ok to use instead of oil'</li></ul>                                                                                                            |
| 99    | <ul><li>'i believe there s fraud on my card'</li><li>'can you help me deal with this fraudulent transaction from verizon on my account'</li><li>'i think there s a fraudulent transaction on my account'</li></ul>                                                     |
| 68    | <ul><li>'what do you think is the meaning of life'</li><li>'i want to know the meaning of life'</li><li>'what makes life have any meaning'</li></ul>                                                                                                                   |
| 70    | <ul><li>'any meetings on the schedule today'</li><li>'is the gang getting together this afternoon'</li><li>'do i have meetings with anyone today'</li></ul>                                                                                                            |
| 110   | <ul><li>'can you book a meeting room for friday at 9 00 am'</li><li>'what is the process to set up a meeting'</li><li>'can you reserve a meeting space for 4 00 on thursday'</li></ul>                                                                                 |
| 144   | <ul><li>'how can i get your attention'</li><li>'ai what do people call you'</li><li>'do you have a nickname'</li></ul>                                                                                                                                                 |
| 105   | <ul><li>'can you give me a points update on my rewards plus card'</li><li>'do i have enough points on my starbucks card yet'</li><li>'how can i see my rewards for my chase card'</li></ul>                                                                            |
| 17    | <ul><li>'i need to rent a car from traveler s rent a car downtown and make it from friday the 6th to monday the 9th cheapest available'</li><li>'help me find a car to rent'</li><li>'i would like some help getting a rental car reserved in los angeles'</li></ul>   |
| 66    | <ul><li>'i do not have that information'</li><li>'it could be that one or the other one'</li><li>'both maybe'</li></ul>                                                                                                                                                |
| 73    | <ul><li>'i need to get a new credit card application'</li><li>'how do i sign up for a new credit card'</li><li>'can i maybe apply for a new card'</li></ul>                                                                                                            |
| 33    | <ul><li>'what is today'</li><li>'which day will it be five days from now'</li><li>'date please'</li></ul>                                                                                                                                                              |
| 101   | <ul><li>'alter back to your orginal settings'</li><li>'reset the factory settings'</li><li>'please go back to the original settings'</li></ul>                                                                                                                         |
| 112   | <ul><li>'shopping list'</li><li>'what does my shopping list say that i should get'</li><li>'what does my shopping list contain'</li></ul>                                                                                                                              |
| 38    | <ul><li>'do you have many kinds of pets at your house'</li><li>'what pets are with you'</li><li>'what sort of animals are your pets'</li></ul>                                                                                                                         |
| 82    | <ul><li>'when will my order be here'</li><li>'online order status'</li><li>'have my goods been delivered yet'</li></ul>                                                                                                                                                |
| 92    | <ul><li>'what is the amount of pto have i used'</li><li>'what s the total of days i ve taken for me time so far'</li><li>'tell me how many days off you see that i have taken so far this year please'</li></ul>                                                       |
| 91    | <ul><li>'was there any progress on my vacation request'</li><li>'please inform me on my current vacation request status'</li><li>'is my day off request still pending'</li></ul>                                                                                       |
| 130   | <ul><li>'i need to know all the recent transactions i ve made'</li><li>'please tell me my in person transactions for the last three days using my debit card'</li><li>'show me all new transactions'</li></ul>                                                         |
| 111   | <ul><li>'share my location with google'</li><li>'how do i share my location with noel'</li><li>'share with current location with ben'</li></ul>                                                                                                                        |
| 65    | <ul><li>'i want to call mark'</li><li>'call my friend aj'</li><li>'call erryn'</li></ul>                                                                                                                                                                               |
| 89    | <ul><li>'could you tell me how many pto days do i have left'</li><li>'how many more vacation days can i use this year'</li><li>'what is the amount of time i can request off in the coming year'</li></ul>                                                             |
| 116   | <ul><li>'could you tell me what kind of money i ve recently spent'</li><li>'looking at this week only have i overspent on hoagies'</li><li>'about how much did i spend recently'</li></ul>                                                                             |
| 141   | <ul><li>'how cold is it going to be tonight'</li><li>'what is the weather doing in austin'</li><li>'what are the weather conditions in seattle'</li></ul>                                                                                                              |
| 131   | <ul><li>'transfer 500 from my checking to my savings'</li><li>'can you transfer 5 from savings to checking'</li><li>'i want seventy bucks transferred from b of a to chase'</li></ul>                                                                                  |
| 104   | <ul><li>'please give me the name of a few good options for places to eat dinner tonight'</li><li>'suggest a few local eateries in mid price range'</li><li>'can you find a keto friendly restaurant'</li></ul>                                                         |
| 59    | <ul><li>'how much is the interest rate for the account i have at bluebird'</li><li>'where do i go to find the interest rate on my savings account'</li><li>'i need my checking account s interest rate'</li></ul>                                                      |
| 97    | <ul><li>'repeat your last message'</li><li>'can you please sat it one more time'</li><li>'tell me once more'</li></ul>                                                                                                                                                 |
| 56    | <ul><li>'what ingredients are in cake'</li><li>'what do you purchase to put in a shepherd s pie'</li><li>'what do i need to buy for spaghetti'</li></ul>                                                                                                               |
| 76    | <ul><li>'hell nah'</li><li>'no that is my response'</li><li>'that s not true'</li></ul>                                                                                                                                                                                |
| 90    | <ul><li>'what do i need to do to request vacation time off'</li><li>'what are the steps required for making a vacation request'</li><li>'i need a pto request put in for the weekend of june 1st to june 2nd'</li></ul>                                                |
| 117   | <ul><li>'are you able to link to my phone'</li><li>'i d like you to pair with my phone'</li><li>'i want you paired to my phone'</li></ul>                                                                                                                              |
| 48    | <ul><li>'tell me the gas i need to fill this car up with'</li><li>'what type of gas does this car take'</li><li>'what gas does this car take'</li></ul>                                                                                                                |
| 128   | <ul><li>'on my to do list add cleaning'</li><li>'put laundry on my to do list'</li><li>'blank out my todo list'</li></ul>                                                                                                                                              |
| 50    | <ul><li>'howdy what s new'</li><li>'hello ai'</li><li>'hi there how are things'</li></ul>                                                                                                                                                                              |
| 0     | <ul><li>'are reservations taken at redrobin'</li><li>'does cowgirl creamery in san francisco take reservations'</li><li>'does ruby tuesday accept reservations'</li></ul>                                                                                              |
| 37    | <ul><li>'what is the time frame to get to phoenix'</li><li>'how long is a bus ride to staples'</li><li>'estimated time to airport from current location la'</li></ul>                                                                                                  |
| 29    | <ul><li>'can i increase the credit limit for my visa platinum card'</li><li>'can i have my credit limit changed'</li><li>'is it possible to increase the credit limit on my mastercard'</li></ul>                                                                      |
| 30    | <ul><li>'what s my credit rating right now'</li><li>'where can i check my credit rating'</li><li>'can you check my credit score for me'</li></ul>                                                                                                                      |
| 87    | <ul><li>'put my music on please'</li><li>'would you play my maroon 5 playlist'</li><li>'can you play the song that sounds like thun thun thun'</li></ul>                                                                                                               |
| 134   | <ul><li>'let my bank know that i m traveling to prague'</li><li>'tell the bank i will be traveling internationally soon'</li><li>'i m leaving for montreal tomorrow and need to let my bank know'</li></ul>                                                            |
| 132   | <ul><li>'how do they say hello in france'</li><li>'if i were english how would i say subway'</li><li>'how do you say good bye in french'</li></ul>                                                                                                                     |
| 11    | <ul><li>'what is 13 times 45'</li><li>'tell me what 1875 plus 3459 equals'</li><li>'can you tell me the square root of pi'</li></ul>                                                                                                                                   |
| 100   | <ul><li>'report a card lost for me'</li><li>'report my lost visa card'</li><li>'my bronze card is missing i would like to report it as lost'</li></ul>                                                                                                                 |
| 16    | <ul><li>'i won t require my reservation anymore'</li><li>'call the restaurant and cancel my reservation'</li><li>'could you cancel my reservation for winters at the palace tonight'</li></ul>                                                                         |
| 13    | <ul><li>'take work from my calendar for may 7th'</li><li>'add my spa appointment on the 12th to my calendar'</li><li>'erase any event on my calendar that s set for wednesday of next week'</li></ul>                                                                  |
| 61    | <ul><li>'i m going to canada soon do i need a visa'</li><li>'i want to go to china but am not sure if i need an international visa'</li><li>'do i need an international visa to go to mexico'</li></ul>                                                                |
| 19    | <ul><li>'ist all carry on restrictions applicable to my flight'</li><li>'how many carry ons can i take on a flight with united airlines to austin'</li><li>'tell me the the carry on restrictions for american airlines'</li></ul>                                     |
| 24    | <ul><li>'i want you to call me lord'</li><li>'my name is jason'</li><li>'i go by brad'</li></ul>                                                                                                                                                                       |
| 12    | <ul><li>'what is on my schedule for the day of march 5th'</li><li>'read my calendar for march 7th'</li><li>'when am i next having a meeting in december'</li></ul>                                                                                                     |
| 46    | <ul><li>'what s an interesting fact about flamingos'</li><li>'i want to know some trivia about our solar system'</li><li>'what s a fun fact about mythology'</li></ul>                                                                                                 |
| 36    | <ul><li>'please tell me the location of the nearest target store'</li><li>'what s the direction for foot traffic to get to the eiffel tower'</li><li>'where is the closest pharmacy'</li></ul>                                                                         |
| 133   | <ul><li>'does finland have any travel alerts i should be aware of'</li><li>'safety concerns for malaysia'</li><li>'will i be safe while traveling to lyon will you be safe '</li></ul>                                                                                 |
| 18    | <ul><li>'i couldn t buy a mug from target because my card got declined'</li><li>'my card got declined why'</li><li>'why was my card declined for my monthly netflix subscription payment'</li></ul>                                                                    |
| 53    | <ul><li>'how can i build my credit score'</li><li>'how to keep my credit from dropping'</li><li>'what steps can i take to build my credit score'</li></ul>                                                                                                             |
| 69    | <ul><li>'what amount of miles are in a hundred kilometers'</li><li>'inform me how many pounds are in 10 kilos'</li><li>'how many centimeters are in 4 inches'</li></ul>                                                                                                |
| 85    | <ul><li>'when s the next time i get paid'</li><li>'what is the date i get paid'</li><li>'i want to know when i was last paid'</li></ul>                                                                                                                                |
| 114   | <ul><li>'put fan on'</li><li>'check who s at the door'</li><li>'what is my ac set to right now'</li></ul>                                                                                                                                                              |
| 139   | <ul><li>'are there shots required before going to south africa'</li><li>'are shots needed for uk travel'</li><li>'will i need immunization for a trip to turkey'</li></ul>                                                                                             |
| 44    | <ul><li>'is the meatloaf still good to eat i ve had it in the refrigerator since last monday'</li><li>'does tofu last long in the freezer before it goes bad'</li><li>'apple cider has been in my fridge for four months so can i still drink it'</li></ul>            |
| 79    | <ul><li>'when do i need an oil change'</li><li>'when to change my oil'</li><li>'oil changes are typical done when'</li></ul>                                                                                                                                           |
| 8     | <ul><li>'do you know when i need to pay my mastercard'</li><li>'when do i have to pay my electric bill by'</li><li>'when is next month s cable bill due'</li></ul>                                                                                                     |
| 96    | <ul><li>'remind me to check the steak'</li><li>'remind me tommorow at 3pm i have a doctors appointment'</li><li>'can you set a reminder for the current time tommorow'</li></ul>                                                                                       |
| 1     | <ul><li>'how can i unfreeze my bank account'</li><li>'what is the reason i am locked out of my bank account'</li><li>'can you help me unlock my bank account'</li></ul>                                                                                                |
| 4     | <ul><li>'what s the current apr on my credit card'</li><li>'tell me the apr of my credit card'</li><li>'how much do i pay in apr on my amex card'</li></ul>                                                                                                            |
| 10    | <ul><li>'please book a hotel in ny close to brooklyn on the 25th to 30th'</li><li>'i want a hotel booked in salem near the concert hall from the first to the second'</li><li>'is there a room big enough for 10 people from monday to tuesday in manhattan'</li></ul> |
| 145   | <ul><li>'what is that tune'</li><li>'tell me the title of the song playing'</li><li>'let me know what song is playing'</li></ul>                                                                                                                                       |
| 28    | <ul><li>'what is the credit limit on my discover card'</li><li>'what is my credit limit on my discover'</li><li>'what is the credit limit for my usaa card'</li></ul>                                                                                                  |
| 140   | <ul><li>'i wanna know where the w2 is'</li><li>'who should i call for a w2'</li><li>'where could i find forms to get my w2'</li></ul>                                                                                                                                  |
| 20    | <ul><li>'you need to change your accent to the male british one'</li><li>'use a different accent'</li><li>'can you change the way you talk to a male british voice'</li></ul>                                                                                          |
| 148   | <ul><li>'whom do you work for'</li><li>'who is your superior'</li><li>'let me know who is your boss'</li></ul>                                                                                                                                                         |
| 39    | <ul><li>'i wanna know five dollars in yen and rubles'</li><li>'look up the rate of exchange between pesos and usd'</li><li>'how many dollars is 20 yen worth'</li></ul>                                                                                                |
| 72    | <ul><li>'what is the city mpg for this car'</li><li>'tell me my car s gas mileage please'</li><li>'what is the cars mpg on the highway'</li></ul>                                                                                                                      |
| 124   | <ul><li>'which timezone is france in'</li><li>'can you tell me britain s timezone'</li><li>'what timezone does bangor have'</li></ul>                                                                                                                                  |
| 125   | <ul><li>'when is it imperative that i get my tires changed'</li><li>'when should i replace my tires sense i last replaced them on 3 21 17'</li><li>'tell me when to get my tires changed'</li></ul>                                                                    |
| 6     | <ul><li>'do i have enough in my chase account for a plane ticket'</li><li>'what is in my bank accounts'</li><li>'what s the total of my bank accounts'</li></ul>                                                                                                       |
| 143   | <ul><li>'what kind of things can you help with'</li><li>'can i ask you all different types of questions'</li><li>'tell me the subject areas you are familiar with'</li></ul>                                                                                           |
| 138   | <ul><li>'who do you think i am'</li><li>'what did i tell you to call me'</li><li>'what will you refer to me as'</li></ul>                                                                                                                                              |
| 34    | <ul><li>'what is the definition of succumb'</li><li>'what is the definition of altruism'</li><li>'what does anachronistic mean'</li></ul>                                                                                                                              |
| 129   | <ul><li>'is there traffic on the way to work'</li><li>'is traffic bad on the parkway'</li><li>'what is the traffic like'</li></ul>                                                                                                                                     |
| 15    | <ul><li>'shut up '</li><li>'abort it'</li><li>'how to cancel'</li></ul>                                                                                                                                                                                                |
| 22    | <ul><li>'select a new language'</li><li>'i would appreciate it if you could talk to me in french'</li><li>'i would like to change your language from portuguese to italian'</li></ul>                                                                                  |
| 45    | <ul><li>'would you freeze my bank account'</li><li>'please put my account on hold'</li><li>'i need you to act swiftly and freeze all activity on my capital one checking'</li></ul>                                                                                    |
| 126   | <ul><li>'what s the tire pressure of my tires'</li><li>'do the tires need air'</li><li>'hows the air in my tires'</li></ul>                                                                                                                                            |
| 120   | <ul><li>'i want a text sent to bob saying i will be late'</li><li>'text matt and tell him i will be late tonight'</li><li>'text roderick and tell him im running late'</li></ul>                                                                                       |
| 127   | <ul><li>'the tasks for today what are they'</li><li>'can you look to see whether feeding the fish is on my to do list'</li><li>'what does my to do list consist of'</li></ul>                                                                                          |
| 32    | <ul><li>'what do i do with a damaged credit card'</li><li>'my credit card snapped in half while i was fiddling with it'</li><li>'unfortunately my card is damaged and unusable'</li></ul>                                                                              |
| 57    | <ul><li>'what are the benefits of having this insurance'</li><li>'can you explain my benefits'</li><li>'define my health benefits'</li></ul>                                                                                                                           |
| 115   | <ul><li>'what s the right spelling of rambunctious'</li><li>'i forget how to spell xylophone'</li><li>'how can i spell avocado'</li></ul>                                                                                                                              |
| 71    | <ul><li>'what s the smallest amount i can pay on the water bill'</li><li>'tell me minimum to pay on landscape bill'</li><li>'what is the smallest i can pay on the water bill'</li></ul>                                                                               |
| 7     | <ul><li>'how much do i have to pay this month'</li><li>'how much do i owe on all of my bills'</li><li>'how much is my electricity bill costing me'</li></ul>                                                                                                           |
| 150   | <ul><li>'yes that is a fact'</li><li>'that is not false'</li><li>'that checks out'</li></ul>                                                                                                                                                                           |
| 3     | <ul><li>'check the status of my credit card application for me'</li><li>'go to the credit card site and check if my application has gone through'</li><li>'has my visa card application been approved yet'</li></ul>                                                   |
| 80    | <ul><li>'aquire me them kyrie 4s'</li><li>'order a disney gift card in the amount of five hundred dollars from costco'</li><li>'please order me a 7lb bag of world s best cat litter from targetcom'</li></ul>                                                         |
| 137   | <ul><li>'get happy on my rb playlist'</li><li>'add coming undone by korn to my playlist'</li><li>'please place this track on my driving mix'</li></ul>                                                                                                                 |
| 103   | <ul><li>'how good are the ratings for olive garden'</li><li>'what are the reviews like for l auberge aubergine'</li><li>'do people like the food at wendy s'</li></ul>                                                                                                 |
| 94    | <ul><li>'how can i redeem my credit card points'</li><li>'i need to redeem my visa points'</li><li>'how can i redeem the points i ve earned with my credit card'</li></ul>                                                                                             |
| 119   | <ul><li>'tell me a joke if you d like to'</li><li>'what do people find funny about food'</li><li>'tell me a joke about dogs'</li></ul>                                                                                                                                 |
| 54    | <ul><li>'tell me about my income this week'</li><li>'yearly salary'</li><li>'how much is the pay offered for my work'</li></ul>                                                                                                                                        |
| 118   | <ul><li>'what s my irs bill going to look like'</li><li>'can you find the exact amount i pay income taxes'</li><li>'how much did my state taxes change'</li></ul>                                                                                                      |
| 43    | <ul><li>'i need you to flip a coin so i can decide'</li><li>'i wanna flip a coin'</li><li>'can you flip a coin i pick heads'</li></ul>                                                                                                                                 |
| 81    | <ul><li>'i used the last check so i want you to help me order more'</li><li>'i don t have checks so can i order some new ones'</li><li>'help me get some new checks since i ran out of them'</li></ul>                                                                 |
| 35    | <ul><li>'i want my paycheck to go directly to my bank account'</li><li>'tell me how to set up a direct deposit'</li><li>'tell me how to get my paycheck on direct deposit'</li></ul>                                                                                   |
| 102   | <ul><li>'reserve a table at tropicana for 5 people under the name martins for 8pm'</li><li>'can you get me a table for two for 8 00 pm at parc'</li><li>'go ahead and book a reservation for 8 pm at red robin under the name kevin'</li></ul>                         |
| 25    | <ul><li>'i want the volume at level 4'</li><li>'boost volume to 4'</li><li>'turn up your volume'</li></ul>                                                                                                                                                             |
| 63    | <ul><li>'give me the date of my last oil change'</li><li>'was my car in the shop this past week'</li><li>'when was my last car service date'</li></ul>                                                                                                                 |
| 14    | <ul><li>'what is the caloric total in these muffins'</li><li>'how many calories are in a serving of deans french onion dip'</li><li>'how many calories in meatloaf'</li></ul>                                                                                          |
| 135   | <ul><li>'what are some popular tourist activities in mexico city'</li><li>'what s fun to do in thailand'</li><li>'find something fun for me to do in dallas'</li></ul>                                                                                                 |
| 147   | <ul><li>'i want you to be in whisper mode now because i am in the library'</li><li>'use your indoor voice please'</li><li>'turn whisper mode off'</li></ul>                                                                                                            |
| 62    | <ul><li>'what shall i do now that my battery is dead'</li><li>'how should i proceed if my car won t start and i think it s the battery'</li><li>'do i need jumper cables for my dead car battery'</li></ul>                                                            |
| 42    | <ul><li>'what time is my flight going to land'</li><li>'what landing time is scheduled for my flight'</li><li>'tell me when my flight is scheduled to start boarding'</li></ul>                                                                                        |
| 136   | <ul><li>'i need an uber to the movies for me and 5 other people'</li><li>'book uber from here to downtown'</li><li>'make an uber reservation to the ymca center city philadelphia please'</li></ul>                                                                    |
| 75    | <ul><li>'let s go to the next song please'</li><li>'start playing the next track'</li><li>'go passed the song now'</li></ul>                                                                                                                                           |
| 106   | <ul><li>'please do a dice roll'</li><li>'roll a 6 sided die and tell me the result'</li><li>'i want you to roll dice'</li></ul>                                                                                                                                        |
| 26    | <ul><li>'i need to make sure there is a reservation for george at connor oneil s'</li><li>'i wanna confirm my reservation for 2 20 at 8 pm'</li><li>'can you check my reservations for mortons under david winters'</li></ul>                                          |
| 121   | <ul><li>'thanks for your response'</li><li>'thanks'</li><li>'thanks '</li></ul>                                                                                                                                                                                        |
| 47    | <ul><li>'can i get to susan s house with my current tank'</li><li>'how much gas does my car currently have'</li><li>'does my car have enough gas to get to detroit'</li></ul>                                                                                          |
| 52    | <ul><li>'what s your birthday'</li><li>'let me know when you were born'</li><li>'what is the year that were you born'</li></ul>                                                                                                                                        |
| 5     | <ul><li>'are you a real life person'</li><li>'are you a real human being'</li><li>'could you be human'</li></ul>                                                                                                                                                       |
| 84    | <ul><li>'i need to make a bill payment'</li><li>'i need to pay my mortgage'</li><li>'please pay electric bill'</li></ul>                                                                                                                                               |
| 64    | <ul><li>'it appears that my luggage has vanished'</li><li>'my luggage was lost on the flight'</li><li>'it looks as though my luggage has been lost'</li></ul>                                                                                                          |
| 31    | <ul><li>'what is my current location that you see right now'</li><li>'where am i on gps'</li><li>'can you find the exact address for where i am currently'</li></ul>                                                                                                   |

## Uses

### Direct Use for Inference

First install the SetFit library:

```bash
pip install setfit
```

Then you can load this model and run inference.

```python
from setfit import SetFitModel

# Download from the 🤗 Hub
model = SetFitModel.from_pretrained("setfit_model_id")
# Run inference
preds = model("tell me today s date")
```

<!--
### Downstream Use

*List how someone could finetune this model on their own dataset.*
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set | Min | Median | Max |
|:-------------|:----|:-------|:----|
| Word count   | 1   | 8.4627 | 26  |

| Label | Training Sample Count |
|:------|:----------------------|
| 0     | 30                    |
| 1     | 40                    |
| 2     | 37                    |
| 3     | 41                    |
| 4     | 38                    |
| 5     | 36                    |
| 6     | 38                    |
| 7     | 35                    |
| 8     | 46                    |
| 9     | 37                    |
| 10    | 41                    |
| 11    | 44                    |
| 12    | 46                    |
| 13    | 46                    |
| 14    | 42                    |
| 15    | 33                    |
| 16    | 45                    |
| 17    | 40                    |
| 18    | 32                    |
| 19    | 33                    |
| 20    | 34                    |
| 21    | 47                    |
| 22    | 28                    |
| 23    | 36                    |
| 24    | 31                    |
| 25    | 39                    |
| 26    | 28                    |
| 27    | 37                    |
| 28    | 41                    |
| 29    | 40                    |
| 30    | 45                    |
| 31    | 33                    |
| 32    | 40                    |
| 33    | 40                    |
| 34    | 38                    |
| 35    | 34                    |
| 36    | 41                    |
| 37    | 45                    |
| 38    | 31                    |
| 39    | 45                    |
| 40    | 39                    |
| 41    | 38                    |
| 42    | 40                    |
| 43    | 43                    |
| 44    | 30                    |
| 45    | 43                    |
| 46    | 41                    |
| 47    | 36                    |
| 48    | 31                    |
| 49    | 35                    |
| 50    | 39                    |
| 51    | 38                    |
| 52    | 33                    |
| 53    | 41                    |
| 54    | 42                    |
| 55    | 41                    |
| 56    | 40                    |
| 57    | 48                    |
| 58    | 41                    |
| 59    | 35                    |
| 60    | 48                    |
| 61    | 36                    |
| 62    | 40                    |
| 63    | 32                    |
| 64    | 35                    |
| 65    | 51                    |
| 66    | 38                    |
| 67    | 31                    |
| 68    | 36                    |
| 69    | 42                    |
| 70    | 37                    |
| 71    | 30                    |
| 72    | 42                    |
| 73    | 37                    |
| 74    | 41                    |
| 75    | 37                    |
| 76    | 37                    |
| 77    | 42                    |
| 78    | 43                    |
| 79    | 31                    |
| 80    | 47                    |
| 81    | 33                    |
| 82    | 36                    |
| 83    | 329                   |
| 84    | 40                    |
| 85    | 33                    |
| 86    | 35                    |
| 87    | 36                    |
| 88    | 45                    |
| 89    | 35                    |
| 90    | 38                    |
| 91    | 44                    |
| 92    | 29                    |
| 93    | 32                    |
| 94    | 28                    |
| 95    | 39                    |
| 96    | 36                    |
| 97    | 41                    |
| 98    | 34                    |
| 99    | 33                    |
| 100   | 32                    |
| 101   | 29                    |
| 102   | 37                    |
| 103   | 41                    |
| 104   | 33                    |
| 105   | 34                    |
| 106   | 39                    |
| 107   | 40                    |
| 108   | 38                    |
| 109   | 33                    |
| 110   | 41                    |
| 111   | 31                    |
| 112   | 35                    |
| 113   | 34                    |
| 114   | 41                    |
| 115   | 35                    |
| 116   | 38                    |
| 117   | 42                    |
| 118   | 38                    |
| 119   | 42                    |
| 120   | 32                    |
| 121   | 36                    |
| 122   | 37                    |
| 123   | 42                    |
| 124   | 34                    |
| 125   | 33                    |
| 126   | 38                    |
| 127   | 40                    |
| 128   | 35                    |
| 129   | 38                    |
| 130   | 37                    |
| 131   | 30                    |
| 132   | 41                    |
| 133   | 45                    |
| 134   | 42                    |
| 135   | 40                    |
| 136   | 36                    |
| 137   | 34                    |
| 138   | 41                    |
| 139   | 39                    |
| 140   | 42                    |
| 141   | 46                    |
| 142   | 47                    |
| 143   | 37                    |
| 144   | 35                    |
| 145   | 36                    |
| 146   | 39                    |
| 147   | 38                    |
| 148   | 40                    |
| 149   | 31                    |
| 150   | 30                    |

### Training Hyperparameters
- batch_size: (32, 32)
- num_epochs: (1, 1)
- max_steps: -1
- sampling_strategy: oversampling
- num_iterations: 1
- body_learning_rate: (2e-05, 2e-05)
- head_learning_rate: 2e-05
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: False
- warmup_proportion: 0.1
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: False

### Training Results
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0027 | 1    | 0.3314        | -               |
| 0.1333 | 50   | 0.1509        | -               |
| 0.2667 | 100  | 0.1546        | -               |
| 0.4    | 150  | 0.0949        | -               |
| 0.5333 | 200  | 0.0923        | -               |
| 0.6667 | 250  | 0.0998        | -               |
| 0.8    | 300  | 0.1044        | -               |
| 0.9333 | 350  | 0.0658        | -               |

### Framework Versions
- Python: 3.12.13
- SetFit: 1.0.3
- Sentence Transformers: 3.0.1
- Transformers: 4.38.2
- PyTorch: 2.10.0+cu128
- Datasets: 2.19.1
- Tokenizers: 0.15.2

## Citation

### BibTeX
```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
    doi = {10.48550/ARXIV.2209.11055},
    url = {https://arxiv.org/abs/2209.11055},
    author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
    keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {Efficient Few-Shot Learning Without Prompts},
    publisher = {arXiv},
    year = {2022},
    copyright = {Creative Commons Attribution 4.0 International}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->