## SIMPLE BROWSER

![](https://www.researchgate.net/profile/Matija-Varga-2/publication/270904300/figure/fig1/AS:645020927410177@1530796381815/Web-browser-software-architecture.png)

## What is a browser ? 

A **web browser** (commonly referred to as a **browser**) is [application software](https://en.wikipedia.org/wiki/Application_software "Application software") for accessing the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web "World Wide Web"). When a [user](https://en.wikipedia.org/wiki/User_(computing) "User (computing)") requests a [web page](https://en.wikipedia.org/wiki/Web_page "Web page") from a particular [website](https://en.wikipedia.org/wiki/Website "Website"), the web browser retrieves the necessary content from a [web server](https://en.wikipedia.org/wiki/Web_server "Web server") and then displays the page on the user's device.

Web browsers commonly include an [address bar](https://en.wikipedia.org/wiki/Address_bar "Address bar") or [search bar](https://en.wikipedia.org/wiki/Search_box "Search box"), the ability to open multiple web pages in different [tabs](https://en.wikipedia.org/wiki/Tab_(interface) "Tab (interface)"), and other user interface features for navigating the web.

Although web browsers have a variety of functions, they also face a plethora of vulnerabilities that can be a critical threat to user privacy. With that, security plays a vital role in ensuring user safety

### Components of a Web Browser

#### 1\. User Interface

It is an environment allowing users to use certain features like search bar, refresh button, menu, bookmarks, etc.

#### 2\. Browser Engine

The bridge connects the interface and the engine. It monitors the rendition engine while manipulating the inputs coming from multiple user interfaces.

#### 3\. Networking

The protocol provides an URL and manages all sorts of safety, privacy and communication.\
In addition, the store network traffic gets saved in retrieved documents.

#### 4\. Data Storage

The cookies store information as the data store is an uniform layer that the browsers use. Storage processes like IndexedDB, WebSQL, localStorage, etc works well on browsers.

#### 5\. JavaScript Interpreter

It allows conversion of JavaScript code in a document and the executes it. Then the engine shows the translation on the screen to the users.

## CLI web browser

Our simple browser is a program which uses network protocoles to retrieve the page that we place as variable and let us navigate through it . 

## How it works

* Copy url adress from any source
* Paste url in the code at the required emplacements

        * mysock.connect(('https://mywebsitename', 80))
        * cmd = 'GET https://mywebsitename/page.html HTTP/1.0\r\n\r\n'.encode()

* save and run program in terminal