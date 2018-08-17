# Security Vulnerability Tracking Tool
 A tool that can scan and parse the upstream security advisories of Apache Tomcat and Apache HTTP Server along with their dependencies(example: OpenSSL, APR, libxml2, curl, mod_security). The tool should trace down any new public CVE on every JWS and JBCS related upstream project.

Note: This tool is intended to run as daemon task and notify through email or Redis channel subscribe. So it will not work as the best reliable tool when running manually as it will compare posted cves with your last run of the spider.

### Requirements


* Python 3.4+
* Works on Linux, Windows, Mac OSX, BS, 

##### Note: Requires the Python header files for completing the installation of requirements(eg, In Fedora OS the twisted package need to have python3-devel pkg installed). So check for  libxslt-devel,pyOpenSSL,python-lxml,python-twisted packages. These are dependencies of Scrapy framework and required to complete before installing Scrapy.



## The quick run Guide::

 Run following commands from inside project folder 
```
pip install -r requirements.txt
python main.py -D
```

<TR/DR>
## Tutorial : Preparing Tool for Running Environment 

You’ll need to have Python 3 available.

1. Setup a folder to store everything:

```
mkdir cve-tool
cd cve-tool
```
2. Get a copy of the C.A.J.S code by running a git clone:

```
git clone https://github.com/examin/C.A.J.S
```
3. We’ll need to create a virtual environment, and install our tool into it.

* For Linux, MacOS: 
```
 python3 -m venv venv
 . venv/bin/activate
 cd cve-tool
```
* For Windows:
```
py -3 -m venv venv
venv\Scripts\activate
cd cve-tool
```

* For Windows (with only conda installed):
```
    pip install virtualenvwrapper-win
    mkvirtualenv venv
    workon venv
    cd cve-tool

```
  You now have a working environment!

4. In addition, you need to install some packages:
```
pip install -r requirements.txt
```



5.  And Finally to test:
```
python3 main.py
```


# It’s alive!

#### Note: If you want to get/send new cve's added notification through email or Redis. Then Before running this tool

## For email:
You need to specify settings in the 'config.ini' file and 'contacts.txt' or pass arguments through commandline for eg: 
```
Python main.py -E -f {"sender email_Id"} -n {"sender name"} -s {"smtp_provider_address"} -p {"stmp_provider_port"} --user {"username"} --pass {"password"}
```
or you can also save setting in Add some names and their email-ids to send notification to by

Configuring "config.ini" file (path : C.A.J.S/Notify/)
*      Add your Gmail email-id
*      Add your Gmail password
Configuring "contacts.txt" file (path : C.A.J.S/Notify/)
*      Add all email ids and their name to send email to 

## For redis pubish:
You need to specify settings in the 'config.ini' file or pass arguments through commandline for eg:
```
Python main.py -R --redis_host { your redis server host } --redis_db {database num to perform action from} 
--redis_por { your redis server port}
```
