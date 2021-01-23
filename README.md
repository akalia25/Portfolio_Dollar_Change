# Portfolio Dollar Change

### Abstract
The purpose of this script is to be able to quickly observe the dollar($) amount change on each of your individual stocks as well as your entire portfolio on a day, week, month, and holistic timeframe.

### Requirements
To run this script, please ensure you have the required libraries downloaded (yfinance, pandas, os) -- to download you can do "pip3 install"

This script requires one simple .csv to function. The .csv must be titled "stock_sheet.csv" and stored on your downloads folder (this can be altered by changing the directory on the script, if you so require). Within the .csv, three columns are required: [stock,	pricePaid,	qty]. Where "stock" holds the stocks ticker name, pricePaid the avg price you paid for that stock, and the qty refers to how many shares of this stock you hold. I have attached a screenshot below of what this template looks like below (dont worry this is not my actual holdings :P) -- You can also find this file in repo to download and edit.

![alt text](https://github.com/akalia25/Portfolio_Dollar_Change/blob/main/Screenshots/csv.png)

### Output
After the requirements are met, you can simply execute the file, and it will calculate each individual stocks dollar($) performance within the timeframes of day, week, month, total. After it is calculated for each of the stocks, the final portfolio's dollar($) change is shown for those timeframes.

![alt text](https://github.com/akalia25/Portfolio_Dollar_Change/blob/main/Screenshots/main_output.png)

### Conclusion
This makes it quick and easy to check how each of your stocks are doing, and the overall impact on your portfolio. May the gains be in your favor! :D 
