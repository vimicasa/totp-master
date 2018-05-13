TOTP-MASTER
============

This is a POC Project to test TOTP in 2FA.  
`RFC 6238: TOTP: Time-Based One-Time Password Algorithm <https://tools.ietf.org/html/rfc6238>`

## NOTE: This app is a POC and it is not production ready.

Installation
------------
::

    pip install -r requirements


Functionalities
------------
* Login in the app ( email / password)  
   Once you login a QR is generated linked to the email provided. 
* Verify Token  
    Introduce your email and TOTP and check if it is valid


    