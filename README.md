<h1>Portfolio Return Calculator</h1>

## Description
The program asks the user to create a hypothetical portfolio and then calculates the projected  market value of said portfolio over a specific period of time specified by the user. This program was originally made to give me better insight when planning my investments. Past returns don't guarantee future results, but they can still provide valuable information when no other data is present. It should be noted that this calculation (falsely) assumes no changes in dividend yield over time, and the stock's average annual return will remain constant over the years. Take these figures with a grain of salt.

## Languages and Utilities Used

- <b>Python</b> 
- <b>Pycharm 2023.2.1 Community</b>

## Packages used

- yfinance
- time

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

## Program walk-through:
<b>Launch Program:</b> 
 The program can be launched by simply downloading the code and running it through your cmd (assuming path variables are set correctly and you are in the correct directory) or any IDE.

<b>Step 1:</b>  
The program will ask you to input the number of assets you want in your portfolio, how many years you would like to invest, and how much money you plan to put toward your monthly investments.

<img src="https://i.imgur.com/8PaoVGL.png" height="80%" width="80%" />

<b>Step 2</b> 
Then, you will need to input the tickers you want in your portfolio. The program will output the annual dividend amount per share and the stock's current price. It will continue this until it reaches the amount of assets you specified earlier.

<img src="https://i.imgur.com/rIDMSXD.png" height="80%" width="80%" />

<b>Step 3:</b> 
Finally, the stock will output your expected account value after n years. It will also display your expected yearly dividend income. This is not a particularly complex program. Check the source code for a slightly more detailed explanation of the inner workings of this program.

<img src="https://i.imgur.com/x9vGk3R.png" height="80%" width="80%" />

## Documentation

[yfinance package](https://pypi.org/project/yfinance/)

[time package](https://docs.python.org/3/library/time.html)
