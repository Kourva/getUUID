# getUUID
Get both version1 or version4 UUID from [uuidgenerator](https://www.uuidgenerator.net)
+ This tool helps you to get free UUID for your proxies like `vmess` and `vless`

#### What is a Version 1 UUID?
    A Version 1 UUID is a universally unique identifier that 
    is generated using a timestamp and the MAC address of 
    the computer on which it was generated.

#### What is a version 4 UUID?
    A Version 4 UUID is a universally unique identifier that 
    is generated using random numbers, using a secure random 
    number generator.


# Installatrion
+ clone 
```bash
https://github.com/kozyol/getUUID && cd getUUID
```
+ requirements
```bash
pip install beautifulsoup4, requests
```
+ usage
```bash
Help: python getUUID.py [[-h] [-v1] [-v4]]
    -h  : Show this message and exit.
    -v1 : get version 1 UUID
    -v4 : get version 4 UUID
```
+ example
```bash
python getUUID.py -v1 -v4

result:
Version1 UUID: 913860b6-a4f9-11ed-b9df-0242ac120003
Version4 UUID: 2060577b-49d1-49e3-97f0-d6ec9a5218fd
```
