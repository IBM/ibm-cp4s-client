# ibm-cp4s-client

 Use the Python package in this repository to develop federated searches on IBM Cloud Pak® for Security data sources. The following diagram illustrates how the package interacts with Cloud Pak for Security.

![How does it work?](https://github.com/IBM/ibm-cp4s-client/blob/master/ibm-cp4s-client.png?raw=true)

# Getting started

## Prerequisites

* Cloud Pak for Security 1.5.0 or later.
* Python 3.6 or later.
* (Optional) Jupyter Notebook, JupyterHub, or Jupyter Lab.

**Note:** Though the ibm-cp4s-client package is designed to run in a Jupyter Notebook environment, it can also be used in any Python program.

## Installing

To install the package, use the following `pip` command in a Notebook cell.
```
!pip install git+git://github.com/ibm/ibm-cp4s-client.git
```

You can also build a compressed file from [this GitHub repository](https://github.com/IBM/ibm-cp4s-client), and install the package by running the following command.
```
!pip install /Documents/Github/ibm-cp4s-client/dist/ibm-cp4s-client-0.0.1.tar.gz
```

## Calling Cloud Pak for Security APIs

Calls to IBM Cloud Pak for Security APIs are divided into client "objects" and "methods".
You must create an Cloud Pak for Security object by supplying `url`, `username`, and `password`. The `username` and `password` are API keys that are obtained from the **Settings** page in Cloud Pak for Security. For more information, see [API key](https://www.ibm.com/support/knowledgecenter/en/SSTDPP_latest/platform/docs/scp-core/apikey.html).

**Note:** The value  of `url` is the home page URL of Cloud Pak for Security CP4Shomepage plus the API path `/api`, for example:
```
from cp4s.client import CP4S
ac = CP4S(url='https://{{CP4S_homepage}}/api',
         username='0afa44ea210553628a9787399a5efffb',
         password='b4d8dce926e64df89c050680655076c1')
```

An ibm-cp4s-client method hides the details of interacting with different IBM Cloud Pak for Security components to complete a specific job. You can focus on high-level objectives by using the methods. For example, the method search_df retrieves the results of STIX queries from the Universal Data Insights component of Cloud Pak for Security, and converts them into tables for analysis by the analytics component of Cloud Pak for Security.
```
mdf = ac.search_df(
    query="[ipv4-addr:value = '127.0.0.1']",
    configs="all")
```

# Examples

[Load Dataframe from CP4S](https://github.com/IBM/ibm-cp4s-client/blob/master/examples/cp4s-client.ipynb)

# References

[IBM Cloud Pak for Security](https://www.ibm.com/products/cloud-pak-for-security)
