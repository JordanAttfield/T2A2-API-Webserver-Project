Endpoint documentation should include
HTTP request verb
Required data where applicable
Expected response data
Authentication methods where applicable


# API Documentation

### Endpoint 1 ###

**URL Path:** auth/register

**Description:** Allows new users to be registered.

**HTTP Request Verb:** POST

**Required Data:** username, email and password - all fields are entered by user and saved in user_fields variable. Each of these fields are also set as not nullable and (required=True). Password must also be a minimum of 6 characters.

**Expected Response Data:** User is successfully registered with user data being stored in database. A JWT token is generated and associated with user. The JWT identity is also set as User ID. If the username or email is already stored in the database, a message is displayed indicating the username or email is already in use.

**Authentication Methods:** Bearer token is generated when user is registered.

### Endpoint 2 ###
**URL Path:** auth/login

**Description:** Allows previously registered users to login.

**HTTP Request Verb:** POST

**Required Data:** username, email and password. Each of these fields is also set to (required=True), so data must be entered.

**Expected Response Data:** If the user is already in the database, the user is successfully able to login, and their username and bearer token is given. If any data is not entered correctly, a message is given stating the data is not valid.

**Authentication Methods:** Bearer token is generated when user is registered. Password needs to match to password stored in database.

### Endpoint 3 ###
**URL Path:** auth/seller/login

**Description:** Allows sellers to login.

**HTTP Request Verb:** POST

**Required Data:** (Note that sellers can only be registered by contacting an administrator). To login an existing seller, username, email and password is required. Each of these fields are not nullable and required=True.

**Expected Response Data:** If the seller data already exists in the database, the seller will successfully login and their username and bearer token will be returned. If any of the data inputs are not valid a message will be returned indicating this.

**Authentication Methods:** Bearer token is generated when seller is logged in.

### Endpoint 4 ###
**URL Path:** /wine

**Description:** All wine stored in database is returned.

**HTTP Request Verb:** GET

**Required Data:** None.

**Expected Response Data:** All wine stored in the database should be returned. Each wine object has the following attributes: name, grape variety, vintage, description, price and vineyard.

**Authentication Methods:** Must be a registered user to view all wine in the database (bearer token must be entered to authenticate).

### Endpoint 5 ###
**URL Path:** /wine/id

**Description:** Data relating to a single wine is returned.

**HTTP Request Verb:** GET

**Required Data:** The wine id is required in the url.

**Expected Response Data:** Data relating to a single wine is returned based on the wine id. If an invalid wine id is entered, a message is returned indicating this.

**Authentication Methods:** User must have a JWT token associated with their account to view data.

### Endpoint 6 ###
**URL Path:** /wine

**Description:** Allows sellers to record a new wine in the database.

**HTTP Request Verb:** POST

**Required Data:** Name, grape variety, vintage, description, price vineyard should be entered. The only required=True fields are name, vintage, price and vineyard. All other fields are optional to enter.

**Expected Response Data:** If successfully posted, the new wine will be returned with all data fields showing.

**Authentication Methods:** User must have a JWT token and their identity must be "seller".

### Endpoint 7 ###
**URL Path:** /wine/id

**HTTP Request Verb:** PUT

**Description:** Allows sellers to update data relating to a specific wine already in the database.

**Required Data:** Wine ID is required for the url path. If an invalid wine id is entered, a message will be returned inidicating this. Fields required to update wine data is: name, grape variety, vintage, description and price.

**Expected Response Data:** If successfully posted, the updated wine data will be returned. If required data fields are missing, a message will be returned indicating where the missing data needs to be filled in.

**Authentication Methods:** User needs to have a JWT token and "seller" identity.

### Endpoint 8 ###
**URL Path:** /wine/id

**Description:** Allows sellers to delete individual wines from the database

**HTTP Request Verb:** DELETE

**Required Data:** No required data in the body. The wine id is required in the url.

**Expected Response Data:** If successful, a message will be returned stating the wine has been deleted from the database. If an incorrect wine id is provided, a message will indicate the wine cannot be found in the database.

**Authentication Methods:** User must have a JWT token and "seller" identity.

### Endpoint 9 ###
**URL Path:** /vineyards

**Description:** Route to get all vineyards from the database

**HTTP Request Verb:** GET

**Required Data:** None.

**Expected Response Data:** All vineyards stored in the database should be returned. Attributes for each vineyard include vineyard id, name, region, and a list of all wines the vineyard is selling.

**Authentication Methods:** User must have a JWT token to access.

### Endpoint 10 ###
**URL Path:** /vineyards/id

**Description:** Route to get a single vineyard back from the database based on vineyard id.

**HTTP Request Verb:** GET

**Required Data:** Vineyard id is required in the url.

**Expected Response Data:** If a correct vineyard id is entered, it will be returned from the database. If an incorrect id is entered, a message will indicate the vineyard cannot be found.

**Authentication Methods:** JWT token is required.

### Endpoint 11 ###
**URL Path:** /vineyards

**Description:** Route allows sellers to post a new vineyard to the database.

**HTTP Request Verb:** POST

**Required Data:** Vineyard name and region are both (required=True). An error will indicate this data needs to be entered if it is missing.

**Expected Response Data:** If the vineyard data is successfully entered, the data of the new vineyard will be returned.

**Authentication Methods:** User must have a JWT token and seller set as their identity.

### Endpoint 12 ###
**URL Path:** /vineyards/id

**Description:** Allows sellers to update individual vineyard data.

**HTTP Request Verb:** PUT

**Required Data:** Vineyard id is required in the url path. If the incorrect id is entered, a message will indicate the vineyard can't be found in the database. Both name and region are required=True. If data in these fields is missing, a message will be returned asking for data to be entered.

**Expected Response Data:** If entered correctly, the updated vineyard data will be returned.

**Authentication Methods:** User must have a JWT token and seller set as their identity.

### Endpoint 13 ###
**URL Path:** /vineyards/id

**Description:** Allows users to delete a vineyard from the database.

**HTTP Request Verb:** DELETE

**Required Data:** The correct vineyard id needs to be entered in the url. A message will indicate if the vineyard id is not found in the system.

**Expected Response Data:** If entered correctly, a message will indicate the vineyard has been successfully deleted.

**Authentication Methods:** User must have a JWT token and seller set as their identity.

### Endpoint 14 ###
**URL Path:** /store

**Description:** Route for users to see all stores in database.

**HTTP Request Verb:** GET

**Required Data:** None.

**Expected Response Data:** All stores listed in database will be returned.

**Authentication Methods:** User must have a JWT token.

### Endpoint 15 ###
**URL Path:** store/id

**Description:** Route for users to return a single store from the database

**HTTP Request Verb:** GET

**Required Data:** Store id is required in the url.

**Expected Response Data:** If successful, a single store will be returned with all data fields. If no store id matches the url entered, a message will be returned indicating this.

**Authentication Methods:** JWT token is required.

### Endpoint 16 ###
**URL Path:** /store

**Description:** Route for sellers to create a new store

**HTTP Request Verb:** POST

**Required Data:** name, location and seller id are required fields.

**Expected Response Data:** If entered correctly, the newly added store will be returned with all data fields. All fields are required=True so a message will indicate if data is missing.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 17 ###
**URL Path:** /store/id

**Description:** Route for sellers to update store data

**HTTP Request Verb:** PUT

**Required Data:** Correct store id is required for the url, name, location and seller id are required for the body,

**Expected Response Data:** If entered correctly, the updated store data will be returned. If store id doesn't match the database, a message will be returned indicating this.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 18 ###
**URL Path:** store/id

**Description:** Route for sellers to delete a store from the database

**HTTP Request Verb:** DELETE

**Required Data:** Store id is required for the url

**Expected Response Data:** A message will be returned indicating the store has been successfully deleted. If store id entered doesn't match to the database, a message will alert to this.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 19 ###
**URL Path:** /store/wine_sold

**Description:** Route for sellers to see all sales data

**HTTP Request Verb:** GET

**Required Data:** None.

**Expected Response Data:** All sales data for wine sold from all stores will be returned.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 20 ###
**URL Path:** /store/wine_sold/id

**Description:** Route for seller to view data on a single wine sale.

**HTTP Request Verb:** GET

**Required Data:** wine_sold_id is required for the url.

**Expected Response Data:** Data on a single wine sale will be returned. If the wine sale id doesn't exist in the databse, a message will be returned indicating this.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 21 ###
**URL Path:** store/wine_id/wine_sale/store_id

**Description:** Route for sellers to record a new wine sale to their store

**HTTP Request Verb:** POST

**Required Data:** Correct wine id and store id is required for the url and data fields in the body.

**Expected Response Data:** If succesfully entered, the new sale transaction will be returned.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 22 ###
**URL Path:** /store/wine_sold/wine_sold_id

**Description:** Route for seller to update wine sale data

**HTTP Request Verb:** PUT

**Required Data:** Correct wine sold id is required for the url. Sale date, store id and wine id are required fields to succesfully update.

**Expected Response Data:** If successful, the updated data will be returned.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 23 ###
**URL Path:** /store/wine_sold/wine_sold_id

**Description:** Route for seller to delete wine sale data

**HTTP Request Verb:** DELETE

**Required Data:** wine sold id is required for the url.

**Expected Response Data:** A message will indicate the data has been successfully deleted. If the id doesn't match the database, a message will indicate this.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 24 ###
**URL Path:** /store/purchases

**Description:** Route to allow sellers to view all purchase data

**HTTP Request Verb:** GET

**Required Data:** None.

**Expected Response Data:** All purchase transaction data stored in the database is returned.

**Authentication Methods:**

### Endpoint 24 ###
**URL Path:** /store/purchase/id

**Description:** Route to sellers to view indidivual purchase data based on store purchase id.

**HTTP Request Verb:** GET

**Required Data:** Store purchase id is required for the url.

**Expected Response Data:** Individual purchase transaction data is returned from the database.

**Authentication Methods:** JWT bearer token and seller identity is required.


### Endpoint 25 ###
**URL Path:** /store/purchase

**Description:** Route for sellers to record a new store purchase transaction

**HTTP Request Verb:** POST

**Required Data:** Purchase date, user id, store id and wine id are all required data fields.

**Expected Response Data:** The new purchase data will be returned.

**Authentication Methods:** JWT bearer token and seller identity is required.

### Endpoint 26 ###
**URL Path:** store/purchase/store_purchase_id

**Description:** Route for sellers to update store purchase transaction data.

**HTTP Request Verb:** PUT

**Required Data:** store purchase id is required for the url. Purchase date, user id, store id and wine id are required in the body.

**Expected Response Data:** If entered correctly, the updated purchase transaction data will be returned.

**Authentication Methods:** JWT bearer token and seller identity required.

### Endpoint 27 ###
**URL Path:** /store/purchase/store_purchase_id
**Description:** Route for sellers to delete store purchase data.

**HTTP Request Verb:** DELETE

**Required Data:** Store purchase id is required for the url.

**Expected Response Data:** The store purchase transaction will be deleted from the database. If the id doesn't match the database, a message will indicate this.

**Authentication Methods:**JWT bearer token and seller identity required.

### Endpoint 28 ###
**URL Path:**

**Description:**

**HTTP Request Verb:**

**Required Data:**

**Expected Response Data:**

**Authentication Methods:**
