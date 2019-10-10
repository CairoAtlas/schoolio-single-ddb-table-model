# Schoolio Single DDB Table Model
10/09 -- I've decided not to continue this POC. Yes, DyanmoDB has the ability to create relational database structure within a single table, but wrapping your head around how it is supposed to work, building a model/schema/object structure for your code to use, and building a separate interface to view the table as a real human being is not worth the time to use unless you have a team full of DynamoDB experts and [insert language here] experts to access the data and create an interface to abstract all the pk/sk/data relations away from the developer. 

It was worth the time testing it though

~A single DynamoDB table that "can handle the access patterns of a legitimate multi-table relational database without breaking a sweat" (Forrest Brazeal). The ERD for this model can be found here: <https://www.lucidchart.com/invitations/accept/4b397772-24b3-4548-bee8-2621f7c1091d>~
