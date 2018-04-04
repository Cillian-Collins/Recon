# Recon
The Recon scanning tool scans websites for open files &amp; directories specified in the custom config file. Default server configuration files, open directories and other potentially harmful files can be found using this scanning tool. Use with permission of website administrator only.

## Requirements
* Python is required for this project. It will run on all Python versions, including 2.x and 3.x without any issues.
* Pip (or a similar alternative) is require to install necessary packages.
* Argparse is required in order to accept command-line arguments.
* Sys is required in order to accept command-line arguments and is also used for the loading icon.
* Requests is required for scanning the websites.
* Time is required for the loading icon.
* Threading is required for the loading icon.

## Installing
To get the project started, you will need to setup pip or an alternative package manager.
To install the necessary modules, listed above, please do the following commands:
```
$ pip install argparse
```
```
$ pip install sys
```
```
$ pip install requests
```
```
$ pip install time
```
```
$ pip install threading
```

## Customizing
You can fully customize which directories and files are scanned by the tool by simply editing the config file. Each line of the config file is a unique file/directory which will be scanned. You can name your config anything you'd like, the default config file can be found under scan.conf.

## Usage
To use the tool simply run the following command (or the equivalent, depending on whether you have renamed your scan.conf file or not):
```sh
$ scanner.py -f scan.conf
```
After which you will be prompted to enter the URL to be scanned. Please do not include any prefixes to the domain, such as "https", "http" or "www". You will see the following prompt:
```sh
$ URL: https://www.
```
If you were to scan GitHub, you would enter it in like so:

```sh
$ URL: https://www.github.com
```
Trailing slashes are completely unnecessary. They won't affect the scan whatsoever, so including one is optional.
