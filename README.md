<!--# Hostel_Room_Booking
## :heavy_exclamation_mark: This is still in the development phase!
* Coming Soon!!....
* This is a Hostel Room Booking system using Django and Python!-->
![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/Saketh-Chandra/Hostel_Room_Booking?include_prereleases)
[![GitHub license](https://img.shields.io/github/license/Saketh-Chandra/Hostel_Room_Booking)](https://github.com/Saketh-Chandra/Hostel_Room_Booking/blob/master/LICENSE)
![GitHub repo size](https://img.shields.io/github/repo-size/Saketh-Chandra/Hostel_Room_Booking)
![GitHub top language](https://img.shields.io/github/languages/top/Saketh-Chandra/Hostel_Room_Booking)
# This is a Centralized database to allot hostel rooms to the college students
This a web application where a user can login and create the tasks, this was built with the [Django](https://www.djangoproject.com/) web application framework

## Description:
The project “Hostel Room Allotment System” is a system based on accessing the internet to
allot the hostel rooms. Based on First Come First Serve, students will have an option to select
the available rooms based on their interest.

## Problem:
In the previous system for booking rooms there were many problems faced by students like
standing in the queues, waiting for longer hours because of manual entry. Therefore, the need
for automation is a necessity. 

## Solution:
The purpose of this project is to implement an online hostel room allotment system for
students replacing the manual method of room allotment. 

## :heavy_exclamation_mark: This is still in the development phase!

# :book: How to use the repository?
## :gear: Setup

#### **First we have to create virtual environments**

### On Windows: 
```cmd
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```

### On macOS and Linux:
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```
### Leaving the virtual environment
```bash
deactivate
```
### After setting up virtual environment do this!
``` bash
git clone https://github.com/Saketh-Chandra/Hostel_Room_Booking.git
cd Hostel_Room_Booking
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# :octocat: How to contribute?

All contributions are welcome! Code, documentation, graphics or even design suggestions are welcome; use GitHub to its fullest. Submit pull requests, contribute tutorials or other wiki content -- whatever you have to offer, it would be appreciated!

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on contributing.

## Know issues
```bash
System check identified some issues:

WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP
 Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this sett
ing True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it mo
re difficult for network traffic sniffers to steal the CSRF token.
?: (security.W018) You should not have DEBUG set to True in deployment.

System check identified 5 issues (0 silenced).

```


# 💡 Future implemention ideas! 
 * Online attendance system 
 * Gate pass system 
 * Raise an issue in hostel
 * Email verification
 * ReCaption V3 Implementation
 


# :scroll: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


See the full list of [contributors](https://github.com/Saketh-Chandra/Hostel_Room_Booking/graphs/contributors) who participated in this project and statistics.

# :heavy_exclamation_mark: Prerequisites aka requirements

Please read [Prerequisite](Prerequisite.md) file for details.

# :scroll: Changelog

Check the [changelog here](https://github.com/Saketh-Chandra/Hostel_Room_Booking/commits/master).

# :scroll: I found some bugs or issues. Where do I report?

Report [here](https://github.com/Saketh-Chandra/Hostel_Room_Booking/issues/new) in detail answering these questions:

* What steps did you take to make the bug appear?
* How can the bug be fixed? (In case you know)
* Which OS and which all packages / softwares / dependencies are you using?
* Have you tried any troubleshooting steps such as a reboot for example?
* Have you followed the prescribed prerequisites?

# :scroll: How do I contact the team?

Check [here](https://github.com/Saketh-Chandra/Hostel_Room_Booking/graphs/contributors) for the list of contributors. Contact one of them through their profiles.
