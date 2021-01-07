# IBM Cloud Pak for Security Client

You can use this python package to interact with IBM Cloud Pak for Security.

![How does it work?](https://github.com/IBM/ibm-cp4s-client/blob/master/ibm-cp4s-client.png?raw=true)

# Getting started

## Prerequisites

* IBM Cloud Pak for Security 1.5.0 or later.
* Python 3.6 or later.
* (Optional) Jupyter Notebook, JupyterHub, or Jupyter Lab.

**Note:** Though this package was designed to run in a Jupyter Notebook environment, it should also work in any python programs.

## Installing

To install the package, use the following `pip` command in a Notebook cell.
```
!pip install git+git://github.com/ibm/ibm-cp4s-client.git
```

You can also build a compressed file from local repository, and install the package by running the following command.
```
!pip install /Documents/Github/ibm-cp4s-client/dist/ibm-cp4s-client-0.0.1.tar.gz
```

## Calling IBM Cloud Pak for Security APIs

Calling of IBM Cloud Pak for Security APIs are abstracted into client "objects" and "methods".
You must create an IBM Cloud Pak for Security object by supplying `url`, `username`, and `password`. The `username` and `password` are API keys that are obtained from the **Settings** page in IBM Cloud Pak for Security. For more information, see [API key](https://www.ibm.com/support/knowledgecenter/en/SSTDPP_latest/platform/docs/scp-core/apikey.html).

**Note:** `url` is the home page of CP4S plus `/api` path, for example:
```
from cp4s.client import CP4S
ac = CP4S(url='https://{{CP4S_homepage}}/api',
         username='0afa44ea210553628a9787399a5efffb',
         password='b4d8dce926e64df89c050680655076c1')
```

*CP4S* is the abbreviation of "Cloud Pak for Security". Therefore, a method of the IBM Cloud Pak for Security client hides the details of interacting with different IBM Cloud Pak for Security components to complete a particular job. You can focus on high-level objectives when using the methods. For instance, the method `search_df` retrieves results of STIX queries (by UDI component of IBM Cloud Pak for Security), and converts them into tables for analysis (by ATK component of IBM Cloud Pak for Security).
```
mdf = ac.search_df(
    query="[ipv4-addr:value = '127.0.0.1']",
    configs="all")
```

# Examples

* [Load Dataframe from CP4S](https://github.com/IBM/ibm-cp4s-client/blob/master/examples/cp4s-client.ipynb)

# References

[IBM Cloud Pak for Security](https://www.ibm.com/products/cloud-pak-for-security)
