# Introduction

Use security OSINT tool Criminal IP (criminalip.io) to identify IoT equipment connected to the internet. You can use CLI to search for IoT equipment and view details of specific IP addresses from the retrieved data



# Prerequisites

* [criminalip.io](https://www.criminalip.io) API Key

You need to create an account and receive an API key at https://www.criminalip.io in order to use sherlocksigth.

Even if you have just a free account, you can access an API key. You can find and use the API key that is assigned to your account at https://www.criminalip.io/mypage/information.



# Installation

Clone repository:

```
$ git clone https://github.com/Aidennnn33/sherlocksight.git
```

```
$ cd sherlocksight
```

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

```
$ pip3 install -r requirements.txt
```



# Getting started

```
$ chmod +x sherlocksight
```

```
$ ./sherlocksight --auth [your-criminalip-api-key]
```



# Optional Arguments

| Flag          | MetaVar       | Usage                                                        |
| ------------- | ------------- | ------------------------------------------------------------ |
| `-A/--auth`   | **API key**   | api authentication with a valid [criminalip.io](http://criminalip.io/) api key |
| `-I/--ip`     | **IP**        | return information of a target IP                            |
| `-Q/--query`  | **Query**     | text search query                                            |
| `-F/--full`   | **Y/N**       | return full(Y) or short information(N) of a target IP        |
| `-O/--output` | **File Path** | write output to a file                                       |
| `-S/--start`  | **Number**    | start number for search query                                |
| `-L/--list`   | **Y/N**       | return IoT search query                                      |
| `-R/--read`   | **File Path** | read file and pretty print the information                   |
