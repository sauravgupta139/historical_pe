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

def plot_figure(i,Date,years,index,PE,PB,Div):
	day=date.today().day
	mon=date.today().month
	year=date.today().year
	f1 = pyplot.figure(i)
	pyplot.subplot(3, 1, 1)
	pyplot.plot(Date,PE);
	#pyplot.xlabel('YEAR');
	pyplot.ylabel('PE');
	pyplot.title('Last %i Year Chart of Price to Earnings of %s on Date -%d/%d/%d' %(years,index,day,mon,year));
	pyplot.text(Date[-1],PE[-1],PE[-1])
	
	pyplot.subplot(3, 1, 2)
	pyplot.plot(Date,PB);
	#pyplot.xlabel('YEAR');
	pyplot.ylabel('PB');
	pyplot.title('Last %i Year Chart of PB of %s on Date -%d/%d/%d' %(years,index,day,mon,year));
	pyplot.text(Date[-1],PB[-1],PB[-1])
	
	pyplot.subplot(3, 1, 3)
	pyplot.plot(Date,Div);
	pyplot.xlabel('YEAR');
	pyplot.ylabel('Dividend Yield %');
	pyplot.title('Last %i Year Chart of Dividend Yield of %s on Date -%d/%d/%d' %(years,index,day,mon,year));
	pyplot.text(Date[-1],Div[-1],Div[-1])
	pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.52)
	if os.path.exists("fig"):
		pyplot.tight_layout()
		pyplot.savefig('fig/%s.png' %index)
	
#TODAY's PE PB DIVIDEND
print ("PE, PB and Dividend Yield ratio of NIFTY is ",PE('NIFTY',get_LATEST_MARKET_OPEN_DATE(),0));
print ("PE, PB and Dividend Yield ratio of NIFTY MIDCAP 50 is ",PE('NIFTY MIDCAP 50',get_LATEST_MARKET_OPEN_DATE(),0));
print ("PE, PB and Dividend Yield ratio of NIFTY SMALLCAP 100 is ",PE('NIFTY SMALLCAP 100',get_LATEST_MARKET_OPEN_DATE(),0));


# HISTORICAL PE, PB and DIV of INDEX1
index=['NIFTY','NIFTY MIDCAP 50','NIFTY SMALLCAP 100','NIFTY PHARMA','NIFTY BANK','NIFTY AUTO','NIFTY FMCG','NIFTY FINANCIAL SERVICES','NIFTY IT','NIFTY METAL','NIFTY REALTY','NIFTY MEDIA','NIFTY PRIVATE BANK','NIFTY PSU BANK','NIFTY ENERGY']
years=10
count=0
for i in index:
	count+=1
	print ("Fetching Data For %s" %i)
	DATE,PE,PB,DIV = PE_list(i,get_LATEST_MARKET_OPEN_DATE(),years);
	plot_figure(count,DATE,years,i,PE,PB,DIV)
print ("All Figures Stored in fig/ folder")	
#pyplot.show();
