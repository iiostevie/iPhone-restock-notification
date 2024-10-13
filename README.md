**Overview**

This Python script automates the process of checking for the availability of specific Apple products for pickup in nearby stores and sends notifications via LINE Bot. It regularly queries Apple's website for product availability, then sends a message to a specified LINE user if stock is available.

**Features**

1. LINE Bot Integration:
   
Receives incoming messages via the LINE Bot webhook, replies with the same message, and prints the message details. Notifies the user(s) about product availability through LINE messaging.

2. Product Pickup Availability Checker:

Automatically checks the availability of specific Apple products (e.g., iPhone Pro Max) for in-store pickup.
Sends a notification to a designated LINE user if the product is available for immediate pickup.

**Dependencies**

This script requires the following Python packages:

  a. requests: For sending HTTP requests to Apple's website and the LINE API.
   
  b. json: For handling JSON responses from the Apple and LINE APIs.
   
  c. datetime: For tracking the current time. 

  d. time: To add delay between requests to Apple's website. 


**How to run the script: **
The script will continuously check for product availability every 30 seconds and send a notification if stock is available.

**Example Output**

2023-10-06 03:25:56.538511

【台北 101】目前無白色Pro Max 256G 現貨

【信義 A13】目前無白色Pro Max 256G 現貨

