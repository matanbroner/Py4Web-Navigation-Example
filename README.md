# Py4Web Navigation

A simple example of using nested Py4Web + Vue components to allow for navigation in a web application.

## Components

1.  Main App
    Has both a Python based component as well as a JS implementation. Holds the main data (ie. URL's and such) and is created by the main controllers file.

2.  About Page
    A simple example of a new page. Has a URL passed down to it from the parent Main App component which it uses to fetch content for the page.

```html
<about :url="about_url" />
<!-- Notice the :url, not url -->
```

3.  Sample Page
    Another simple page, no props passed, shows that a page can be simple with no API calls or difficult props.

```html
<samplepage />
```
