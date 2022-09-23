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
**URL Path:**

**Description:**

**HTTP Request Verb:** 

**Required Data:** 

**Expected Response Data:** 

**Authentication Methods:** 

### Endpoint 10 ###
**URL Path:**

**Description:**

**HTTP Request Verb:** 

**Required Data:** 

**Expected Response Data:** 

**Authentication Methods:** 

### Endpoint 11 ###
**URL Path:**

**Description:**

**HTTP Request Verb:** 

**Required Data:** 

**Expected Response Data:** 

**Authentication Methods:** 