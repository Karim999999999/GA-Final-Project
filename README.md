#Introduction: 
Co-operate is a Full-Stack application with CRUD functionality built using Django, Express, React, Pipenv and Node. The tool supports the formation of Co-operatives to benefit from bulk purchasing, focusing on the use of food cooperatives to increase access of people from lower-income backgrounds to wider food and hygiene options.

N.B. The full build of this project was stalled by personal circumstances that resulted in the incompletion of all product features. With this said, many functionalities still work smoothly. 
The Brief
 
* **Build a full-stack application** by making your own backend and your own front-end
* **Use a Python Django API** using Django REST Framework to serve your data from a Postgres database
* **Consume your API with a separate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models
* **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut
* **Have an entity relationship diagram** showing your proposed database schema
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients & employers. **ALLOW** time for this.
* **Be deployed online** so it's publicly accessible.
 

# Technologies Used
## Back-End
Node.js
MongoDB
Mongoose
Express
Nodemon
Bcrypt
JSON Web Token

## Front-End
React
CSS
Axios
React-Router-Dom

## Development Tools
Adobe XD (wireframing)
Postman
Git & GitHub
Heroku (deployment)
VS Code
Netlify (Deployment)





# How do people co-operate?
The concept of this site is to facilitate the creation and operation of purchasing cooperatives while decreasing the financial risks and accessibility issues regularly associated with these organisations. 

# How did the site work?

## Creating Co-op and deciding on features:
Anyone can be a user. Once you are on the platform, you have the option to either join existing co-operatives or create your own. Creating your own co-operative gives you many options such as special tags in order to differentiate your co-op and make it easier for people to find it. 

## Inventory Research: 
The inventory tool allows the owner of the Co-op to make their own inventory, and list the products and their prices at different quantities. This gives the co-op members the transparency to review the costs of the items. Minimum quantities are set. 

## Creating Co-op Package:
Your Coop package is what items you will be selling in the next package. You can select items from your inventory to make up this list. 

## Order Package:
The package is then put out on the Co-op and members have the option to buy-in. This will order them the minimum quantity which they requested. Orders can be made on behalf of others. 

## Collection:
Upon collection, a barcode is scanned and the money is sent to the co-op manager.

## Power in Quantity: 
The more people you can attract to your Co-op the cheaper things get for your community. 

# Build Journal:
Day 1: Brainstorming and UI/UX of initial user journeys on Adobe XD
Day 2: More UI/UX of initial user journeys on Adobe XD and then commencing database design
Day 3: Database simplification, begin backend model building 
Day 4: Finish model building and start with the Django controllers
Day 5: Backend routing and testing + Commence FE
Day 6: Build home page, co-ops pages, and new coops user journey
Day 7: Debug and retest BE
Day 8: Build toggle screens, begin permission implementation, and build inventory functionality
Day 9: Build weeks orders FE construction. 
Day 10: Basic styling SASS
Did not have enough time as back end construction and testing were too long. 
# Database Design:
The database was built on Django, using the Django rest framework. The database involved 13 Models, divided between 5 Apps. Most models have controllers with full CRUD functionality, although some are only accessible through the Admin Django page. This was done with certain features to limit the creation of too many small components for the MVP. Functionality involved permission-based API access depending on multiple different user-specific properties. 

## App 1 - Coop Creator:
Fully contained within App 1 was everything needed to create a Coop. 
### Model 1 - Coop Tag:
A coop tag is an admin-only Db which has around 15 potential co-op tags to help members understand the primary function of the Co-op with more ease. 

### Model 2 - Purchase Frequency Option:
This is another admin-only DB that feeds down into a drop-down menu on the front end. This helps people understand how frequently the Co-op operates. 

### Model 3 - Operational City: 
This is another admin-only DB that feeds into a drop-down menu on the front end. It will be used to control the rollout of the product to different regions of the UK.

### Model 4 - Coop:
This is the only user-accessible DB, it displays the co-ops information, including tags to the other DB of Operational City, purchase frequency, and the coop tags. 

## App 2 - Coop Manager:
Fully contained is all the functions needed to manage coop inventory for any coop from app 1.
### Model 5 -  Item Type:
Item Type is an admin-only Db which has around 15 potential item tags. The idea behind this it to collect data on the different types of items purchased. It can also be used to implement subsidies across the system. 
 
### Model 6 - Quantity Unit:
Item Quantity Unit is an admin-only Db which has around 10 potential measures. This is to understand what type of unit of product the price stratification is divided into. 

### Model 7 - Coop Item:
This is a user-accessible DB, it displays the information for one item, including tags to the other DB of quantity unit and item type. A linked one too many fields for Price brackets exists in order to keep track of changes in a co-ops prices as more members join. 

### Model 8 - Price Bracket:
A user-accessible many to one field associated with a co-op item. Each price bracket features a number of units specified in the coop item section and the price per unit at that number of units. Multiple price brackets are added for each item in order 

## App 3 - Auth:
This app features a custom user model.

### Model 9 - CustomUser:
A custom user model with fields to link the user to the ownership and membership of certain Co-ops and orders, allows us to control permissions for different views.

## App 4 - Order Manager: 

### Model 10 -  Order Proposal Status:
An admin-only Db that has 5 potential proposal statuses. This is to help understand the status of the large order proposal made by the coop. 

### Model 11 - Order Status:
An admin-only Db that has 5 potential order statuses. This is to help understand the status of an individual coop members order. It will be used to understand the fulfilment status and pick up rate of the food co-op.

### Model 12 - Order Proposal:
An order proposal is a db that manages order options for a coop. When a new order proposal is drafted, it is tagged to co-op items, and to the co-op itself. Co-op members can then place an order of the order proposal. 

### Model 13 - Order:
Order is a db table that keeps track of requests of co-op members to buy into an order proposal. 

## Controllers:
All models were serialised and views were created for permission based CRUD functionality.
How does the site work?
Home Page, register, login: 
When you arrive at the web app you will get to the home page which is plain at the moment. If you navigate to the burger menu, then you can register or log in to the site. Once you have done that. I would recommend you use a fake email account.

## Discover Coops Page: 
On the discover Coop page you can see all of the co-ops. There is a tabs panel which uses the state to switch between different views. Due to shortages in time, the filters and my coops page were never developed at the time of this experiment. I will be getting back to them in my next version of the page. Here you also have the option to create a new Coop which is automatically tied to your account. Clicking on a Coop card takes you to the main page for the coop. 

## Coop Page:
The coop page has everything needed to create coop items, create order proposals and allow users to make orders. Unfortunately, this is incompletely built with only the ability to create new coop items. I will be working on adding the other functionalities in the next version of the product. The coop page should also contain a customer orders user journey which I have not had the opportunity to complete building yet. 


# Challenges:
This project was fun but complex to build. I grossly underestimated the complexity of the back end databases. While I initially cut off functionality like notifications and messages, I did not think of stripping down some of the avoidable DBS in the Coop creation Dbs. This led to an extended planning process. Although this was helpful, I didn't account for the construction time alone since I worked on my last project in a group of 3.

# Wins:
 Since the back end is fully functional, I think I did a good job in that phase of the production. The front end might not look ridiculously functional, however, I was able to get up all this functionality in under 48 hours by prioritizing the construction of components with props for use across the site. A minimalist white design with bright primary accents was a design choice to simplify the site for users. 

# Future:
In the future, I need to think of a more feasible plan. This would involve really stripping down additional DB features for the front end to simplify the MVP. I really enjoyed using the state in this project to manipulate the DOM. I will continue working on completing the features of this project which are still incomplete.

