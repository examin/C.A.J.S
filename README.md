# Security Vulnerability Tracking Tool
 A tool that can scan and parse the upstream security advisories of Apache Tomcat and Apache HTTP Server along with their dependencies(example: OpenSSL, APR, libxml2, curl, mod_security). The tool should trace down any new public CVE on every JWS and JBCS related upstream project.

### Requirements


* Python 3.4+
* Works on Linux, Windows, Mac OSX, BS


#### Note: Before starting the server, you need to specify its settings in the 'config.ini' file and 'contacts.txt'

 The quick way to running Steps::

1. Configure "config.ini" file (path : C.A.J.S/Notify/)
*      Add your Gmail email-id
*      Add your Gmail password
2. Configure "contacts.txt" file (path : C.A.J.S/Notify/)
*      Add some names and their email-ids to end notification to.

3. Run following commands
```
pip install -r requirements.txt
python main.py
```
<TR/DR>
## Tutorial: Preparing your Environment 
You’ll need to have Python 3 available. Instructions on how to set this up are on our Environment setup guide.

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
  You now have a working Batavia environment!

4. In addition, you need to install some pacakges;

Run this command:
```
pip install -r requirements.txt
```

5.  Configure "config.ini" file (path : C.A.J.S/Notify/)
*      Add your Gmail email-id
*      Add your Gmail password
6.   Configure "contacts.txt" file (path : C.A.J.S/Notify/)
*      Add some names and their email-ids to send notification to.

7.  Run following commands
```
    python3 main.py
```

# It’s alive!


