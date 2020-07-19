Persistent date-time stamp application 
======================================

An ansible playbook for deploying a simple lambda function for writing the 
current time and a uuid to a dynamodb table on a request. This is fronted 
by API gateway to only allow requsts to this lambda using POST on the /app 
endpoint.

Requirements
------------

This project has been tested using ansible 2.9.10 on python 3.6.9, the output `pip freeze`
has been provided for packages requried and versions 
```
asn1crypto==0.24.0
attrs==17.4.0
Automat==0.6.0
blinker==1.4
boto==2.49.0
boto3==1.14.21
botocore==1.17.21
certifi==2018.1.18
chardet==3.0.4
click==6.7
cloud-init==18.2
colorama==0.3.7
command-not-found==0.3
configobj==5.0.6
constantly==15.1.0
cryptography==2.1.4
decorator==4.1.2
distro-info==0.18
docutils==0.15.2
httplib2==0.9.2
hyperlink==17.3.1
idna==2.6
incremental==16.10.1
ipython==5.5.0
ipython-genutils==0.2.0
Jinja2==2.10
jmespath==0.10.0
jsonpatch==1.16
jsonpointer==1.10
jsonschema==2.6.0
keyring==10.6.0
keyrings.alt==3.0
language-selector==0.1
MarkupSafe==1.0
oauthlib==2.0.6
PAM==0.4.2
pexpect==4.2.1
pickleshare==0.7.4
prompt-toolkit==1.0.15
pyasn1==0.4.2
pyasn1-modules==0.2.1
pycrypto==2.6.1
Pygments==2.2.0
pygobject==3.26.1
PyJWT==1.5.3
pyOpenSSL==17.5.0
pyserial==3.4
python-apt==1.6.2
python-dateutil==2.8.1
python-debian==0.1.32
pyxdg==0.25
PyYAML==3.12
requests==2.18.4
requests-unixsocket==0.1.5
s3transfer==0.3.3
SecretStorage==2.3.1
service-identity==16.0.0
simplegeneric==0.8.1
six==1.11.0
ssh-import-id==5.7
systemd-python==234
traitlets==4.3.2
Twisted==17.9.0
ufw==0.35
unattended-upgrades==0.1
urllib3==1.22
wcwidth==0.1.7
zope.interface==4.3.2
```

RUNNING INSTRUCTIONS
====================

This ansible code assumes that you already own a domain within AWS and and have
a public route53 hosted zone. First edit the playbooks/provision.yaml and update
 `domain_suffix` to your owned domain.

You must create a vault file with your AWS credentials. Create 
the vault file first in plain text. 

```
touch inventory/group_vars/all/vault.yaml
```

Then encrypt the file with the following command, providing a unique memorable
password at the prompt
```
ansible-vault encrypt inventory/group_vars/all/vault.yaml
```

You can then edit the file using the edit command
```
ansible-vault edit inventory/group_vars/all/vault.yaml
```

Populate it with the following variables, substituting your own credentials
```
vault_AWS_ACCESS_KEY_ID: "MY ACCESS KEY"
vault_AWS_SECRET_ACCESS_KEY: "MY SECRET KEY"
```

The application can then be deployed by running the following, adding in your 
password as requested. 
```
ansible-playbook playbooks/provision.yaml
```


NOTES
=====

The playbook will pause at some point for you to add a variable to all.yaml. 
This is because ansible will create an api gateway resource but will be unable
to manage it going forth without the id returned by the module. 


There have been time when running this playbook has failed when AWS services
have not been updated quick enough for ansible to pick up new variables. 
Re-running the playbook will solve this. 

