# Fasternet

[Go to Downloads](https://github.com/epicdragon44/fasternet/releases)

<img src="demo.png" width="360px">

---

### A HooHacks 2020 Winning Hack!

An open-source Python tool that optimizes your internet connection with one click by finding the most optimal local DNS servers, with help from Google's Open-source namebench utility, and then automatically applying that configuration to your computer.

[DevPost](https://devpost.com/software/fasternet-gtvhpu) | [GitHub](https://github.com/epicdragon44/fasternet/)

---

## About

### What it does

Fasternet is a single app which comes in two versions for your Windows PC: feather, and falcon, which is either a one-time executable or a program that installs to your hard drive and which you can regularly use, depending on your preference. The interface is extremely simple - a single click on the button "Start" will automatically optimize your internet for you, with no further interaction necessary.

### How we built it

The basic idea behind Fasternet is that DNS resolving - that is, turning a domain such as Google.com into an IP address which your computer can find on the web - is the bottleneck for much of internet loading times. Thus, our goal was to improve the DNS resolving process.

The foundation of our work is a (very old) open-source project called namebench, by Google, which uses a command line or GUI interface coded in Tlc and Tk to ping local DNS servers and determine the fastest ones. Our team built a Python and Windows shell script framework around namebench that automatically parses the HTML output from namebench and then changes your Windows PC's DNS configuration to use the best local DNS servers. 
