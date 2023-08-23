# Introduction

I hope you can explore the functionality of Criminal IP's security OSINT tool for identifying internet-connected IoT devices and utilizing the CLI to search and access detailed information about specific IP addresses from the obtained data.


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
