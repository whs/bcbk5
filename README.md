# Barcamp Bangkhen 5

This is all source code used in organizing Barcamp Bangkhen 5.

All are licensed under MIT license. You may not use the Barcamp Bangkhen name, logo, graphics however.

## bcbk5

The bcbk5 folder contains the backend part (which used to resides in `api.2014.barcampbangkhen.org`).
It manages the session table data and registration data. It is powered by Django and Django REST framework.

## frontend

The frontend folder contains the same content as [bcbk5-front](https://github.com/whs/bcbk5-front) repository which
is mounted at [2014.barcampbangkhen.org](http://2014.barcampbangkhen.org).

## twstream

The twstream folder contains the Twitter timeline stream and video player used during the opening ceremony.

To run it, copy config.def.js to config.js and enter Twitter keys, install node.js dependencies
and run `node main.js`. Then, put the client folder in a web server and open it.

The client uses proprietary fonts which you must obtain them yourselves or redesign the interface.
If running in Linux (which was the case during the event) the infinality fontconfig patch is suggested.
