# CP4S Client

A python package for interacting with CP4S (CloudPak for Security).

![How does it work?](https://github.com/IBM/ibm-cp4s-client/blob/master/ibm-cp4s-client.png?raw=true)

# Getting started

## Prerequisites

1. CP4S version >= 1.5
1. Python 3
1. (Optional) Jupyter Notebook, JupyterHub, or Jupyter Lab

Note: This package was designed to be used within a Jupyter Notebook environment. However, it should also work in general python programs.

## Installing

To use the package, simply install it with `pip` in a notebook cell.
```
!pip install git+git://github.com/ibm/ibm-cp4s-client.git
```

One can also build a tar file from his/her local repository, and install it like the following.
```
!pip install /Documents/Github/ibm-cp4s-client/dist/ibm-cp4s-client-0.0.1.tar.gz
```

## Calling CP4S APIs

Calling of CP4S APIs are abstracted into client "objects" and "methods".
One need to properly create a CP4S object supplying `url`, `username` and `password` before using it. The `username` and `password` are API keys obtained from the "Settings" page in CP4S (see [here](https://www.ibm.com/support/knowledgecenter/SSTDPP_1.1.0/docs/scp-core/apikey.html) for details), while `url` is the homepage of CP4S plus `/api` path, like the following.
```
from cp4s.client import CP4S
ac = CP4S(url='https://{{CP4S_homepage}}/api',
         username='0afa44ea210553628a9787399a5efffb',
         password='b4d8dce926e64df89c050680655076c1')
```

Note that *CP4S* is the abbreviation of "Cloud Pak for Security". A method of the CP4S client (`ac`) hides the details of interacting with different CP4S components to complete a particular job, therefore users can focus on high-level objectives when invoking the methods. For instance, the method `search_df` will retrieve results of STIX queries (via UDI component of CP4S), and convert them into tables suitable for analyses (via ATK component of CP4S). The components are subject to change while CP4S is evolving, therefore their naming and functions are not discussed here.
```
mdf = ac.search_df(
    query="[ipv4-addr:value = '127.0.0.1']",
    configs="all")
```

# Examples

* [Load Dataframe from CP4S](https://github.com/IBM/ibm-cp4s-client/blob/master/examples/cp4s-client.ipynb)

# References

CP4S: https://www.ibm.com/products/cloud-pak-for-security
