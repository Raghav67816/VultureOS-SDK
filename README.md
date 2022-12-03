# VultureOs SDK

Welcome to VultureOs SDK documentation. Please note that the SDK is currently under development

**Source Code: [GitHub](https://github.com)**

**Current Version: 1**

**Official Website: [Coming Soon](https://google.com)**

# About
VultureOs SDK is a software development kit for developing apps for VultureOs (Debian based) providing set of main features of the main app.

# Our current progress
- [ ] Complete System
     * [x] User Management System
     * [x] Cloud Database
     * [x] Device Registration
     * [x] JWT Token System
     * [x] Middlewares - Security
     * [x] Python Package - VultureOs
     * [ ] User Interface
     * [x] Sensor Interfacing
     * [x] Alexa Integration

## Key features of the SDK
* Lightweight and Fast
* Fewer dependencies
* Easy to change
* Proper error handling
* Scanned programs (using Bandit)

## Installation
Currently, SDK is only available on GitHub, but it will be soon available on [PyPi](https://pypi.org)

* Clone the GitHub repository
```commandline
git clone https://github.com/Raghav67816/VultureOS-SDK.git
cd vultureOs-sdk
```

* Install dependencies
```commandline
pip install -r requirements.txt
```

This SDK currently uses pymongo and python-dotenv as base dependencies. Install them using requirements.txt file the root folder.


## Setting up for UI development
In the root folder of the SDK the folder named **Widgets** contains pre-made widgets which are made according to the UI standard of the main app. These widgets are written in QML and designed through QT Creator.

* Installing QT Creator
    * Visit [QT Official Website](https://qt.io) and create a new account if not.
    * Go to [QT Open Source Community Version Download](https://www.qt.io/download-open-source?hsCtaTracking=e9c17691-91a0-4616-9bc2-1a6a6c318914%7C963686f8-2c68-442a-b17b-3d73ce95b819)
    * Download the Qt Installer and run it
    * Proceed to installation
    * Install the preferred version of Qt with MinGW x64 compiler
    * Wait for the installer to complete the process

All set!

!!! warning 

    BEFORE INSTALLING QT CREATOR PLEASE CHECK FOR THE VERSION BEING USED IN THE DEVELOPMENT OF MAIN APP IN DOCUMENTATION TO MATCH THE COMPATIBILITY OF THE MAIN APP AND CHILD APP.

If you encounter any problem during the installation, please reach us at **innovationinfinite8@gmail.com**


## Additional requirements
The SDK uses MongoDB for storing devices and error. This is a testing feature. Here you can use the local MongoDB database, or you can use the online MongoDB. For using MongoDB locally please visit [MongoDB Community Server Download](https://www.mongodb.com/try/download/community).

## Getting Started
Before getting started, please make sure to complete the steps above. If you have completed the setup then, proceed to Getting Started

##License
This project is Licensed under MIT License
