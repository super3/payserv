# payserv

[![Build Status](https://travis-ci.org/Storj/payserv.svg?branch=master)](https://travis-ci.org/Storj/payserv)

# What is this?
A Flask application for testing the [Vennd](http://www.vennd.io/) batch send payment library. In Storj
we need to be able to pay users for their resources. This involves many small payments, most less
than a penny. We use payserv to keep track of all those small payments, and pay them out once they
reach a reasonable amount. 

tldr; We take lots of little payments, and make them into one big one.