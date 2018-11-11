#!/usr/bin/python3
##Written  by Saurav Gupta - 11th Nov 2018

#prerequisites
##Install Python 2.7 in windows- https://www.python.org/downloads/
##open cmd prompt and install these libraries
##>> cd C:\Python27\Scripts\
##>> pip.exe install nsetools
##>> pip.exe install nsepy
##>> pip.exe install lxml
##>> pip.exe install matplotlib
##edit enviroment variable path and add C:\Python27\ else python command will not be recognized. Don't forget to restart cmd prompt
##To Run type -> python PE.py


##Install python3 in linux - if already not installed
##>> sudo apt-get install python3.7
##>> sudo apt-get install pip3
##>> pip3 install lxml 
##>> pip3 install nsetools
##>> pip3 install nsepy
##>> pip3 install matplotlib
##To run type Run -> python3 PE.py

from nsetools import Nse;
from nsepy import get_history;
from nsepy import get_index_pe_history;
from datetime import date, timedelta;
from datetime import datetime as t;
from matplotlib import pyplot;
import os

def get_LATEST_MARKET_OPEN_DATE():
    if (date.today().weekday() == 6):
        return date.fromordinal(date.today().toordinal()-2);
    elif (date.today().weekday() == 5):
        return date.fromordinal(date.today().toordinal()-1);
    else:
        if (t.now().hour > 16):
            return date.today();
        elif (t.now().hour == 15 and t.now().minute > 30):
            return date.today();
        else:
            if (date.today().weekday() == 0):
                return date.fromordinal(date.today().toordinal()-3);
            else:
                return date.fromordinal(date.today().toordinal()-1);
        
def PE(i,date_latest,xdays):
    PE_of_xdays = get_index_pe_history(symbol=i,start=date.fromordinal(date_latest.toordinal()-xdays), end =date_latest);
    return PE_of_xdays['P/E'].tolist()[0],PE_of_xdays['P/B'].tolist()[0],PE_of_xdays['Div Yield'].tolist()[0];


def PE_list(i,date_latest,years):
    PE_of_years = get_index_pe_history(symbol=i,start=date.fromordinal(date_latest.toordinal()-years*365), end =date_latest);
    return PE_of_years.index.values,PE_of_years['P/E'].tolist(),PE_of_years['P/B'].tolist(),PE_of_years['Div Yield'].tolist();


#TODAY's PE PB DIVIDEND
print ("PE, PB and Dividend Yield ratio of NIFTY is ",PE('NIFTY',get_LATEST_MARKET_OPEN_DATE(),0));
print ("PE, PB and Dividend Yield ratio of NIFTY MIDCAP 50 is ",PE('NIFTY MIDCAP 50',get_LATEST_MARKET_OPEN_DATE(),0));
print ("PE, PB and Dividend Yield ratio of NIFTY SMALLCAP 100 is ",PE('NIFTY SMALLCAP 100',get_LATEST_MARKET_OPEN_DATE(),0));


# HISTORICAL PE, PB and DIV of INDEX1
index='NIFTY'
years=10
Date,PE,PB,Div = PE_list(index,get_LATEST_MARKET_OPEN_DATE(),years);

# HISTORICAL PE, PB and DIV of INDEX2
index2='NIFTY MIDCAP 50'
years2=10
Date2,PE_MID,PB2,DIV2 = PE_list(index2,get_LATEST_MARKET_OPEN_DATE(),years2);

# HISTORICAL PE, PB and DIV of INDEX3
index3='NIFTY SMALLCAP 100'
years3=10
Date3,PE_SMALL,PB3,DIV3 = PE_list(index3,get_LATEST_MARKET_OPEN_DATE(),years3);

#Plotting
f1 = pyplot.figure(1)
pyplot.subplot(3, 1, 1)
pyplot.plot(Date,PE);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PE');
pyplot.title('Last %i Year Chart of Price to Earnings of %s' %(years,index));
pyplot.text(Date[-1],PE[-1],PE[-1])

pyplot.subplot(3, 1, 2)
pyplot.plot(Date,PB);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PB');
pyplot.title('Last %i Year Chart of Price to Book Value Per Share of %s' %(years,index));
pyplot.text(Date[-1],PB[-1],PB[-1])

pyplot.subplot(3, 1, 3)
pyplot.plot(Date,Div);
pyplot.xlabel('YEAR');
pyplot.ylabel('Dividend Yield %');
pyplot.title('Last %i Year Chart of Dividend Yield of %s' %(years,index));
pyplot.text(Date[-1],Div[-1],Div[-1])
pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.52)
if os.path.exists("fig"):
	pyplot.savefig('fig/%s.png' %index)

f2 = pyplot.figure(2)
pyplot.subplot(3, 1, 1)
pyplot.plot(Date2,PE_MID);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PE');
pyplot.title('Last %i Year Chart of Price to Earnings of %s' %(years2,index2));
pyplot.text(Date2[-1],PE_MID[-1],PE_MID[-1])

pyplot.subplot(3, 1, 2)
pyplot.plot(Date2,PB2);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PB');
pyplot.title('Last %i Year Chart of Price to Book Value Per Share of %s' %(years2,index2));
pyplot.text(Date2[-1],PB2[-1],PB2[-1])

pyplot.subplot(3, 1, 3)
pyplot.plot(Date2,DIV2);
pyplot.xlabel('YEAR');
pyplot.ylabel('Dividend Yield %');
pyplot.title('Last %i Year Chart of Dividend Yield of %s' %(years2,index2));
pyplot.text(Date2[-1],DIV2[-1],DIV2[-1])
pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.52)
if os.path.exists("fig"):
	pyplot.savefig('fig/%s.png' %index2)

f3 = pyplot.figure(3);
pyplot.subplot(3, 1, 1)
pyplot.plot(Date3,PE_SMALL);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PE');
pyplot.title('Last %i Year Chart of Price to Earnings of %s' %(years3,index3));
pyplot.text(Date3[-1],PE_SMALL[-1],PE_SMALL[-1])

pyplot.subplot(3, 1, 2)
pyplot.plot(Date3,PB3);
#pyplot.xlabel('YEAR');
pyplot.ylabel('PB');
pyplot.title('Last %i Year Chart of Price to Book Value Per Share of %s' %(years3,index3));
pyplot.text(Date3[-1],PB3[-1],PB3[-1])

pyplot.subplot(3, 1, 3)
pyplot.plot(Date3,DIV3);
#pyplot.xlabel('YEAR');
pyplot.ylabel('Dividend Yield %');
pyplot.title('Last %i Year Chart of Dividend Yield of %s' %(years3,index3));
pyplot.text(Date3[-1],DIV3[-1],DIV3[-1])
pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.52);
if os.path.exists("fig"):
	pyplot.savefig('fig/%s.png' %index3)
pyplot.show();
