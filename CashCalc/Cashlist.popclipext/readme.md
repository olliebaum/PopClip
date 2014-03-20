###Only supports prices in the following formats:
   - <s>£20
   - 4.17p
   - 4p </s>   
   - 109p
   - `£5.73p` (well, sort of – £5.73 shows up as £5 total) 
   - `£10.00`
   - Will recognise the whole number of pounds of any amount 		with 1 decimal place.
   - Can see how many whole pounds are in an amount of pennies –  
   For example – `109p` will return `£1 total`.
   

###Currently, this will not support:
- prices with pennies e.g. `10p`, `£3.49`  etc. 
- prices at 1 d.p. e.g. `£1.5` shows as `£1 total`
- abbreviated forms of million and thousand eg. `£13k`, `£23m`
- currencies other than GBP
- word forms of pound, pence etc. eg. 5 pounds, sixteen pence.