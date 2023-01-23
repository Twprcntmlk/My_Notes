# Meta Tags

&lt;meta&gt;:
    An HTML tag for providing extra metadata about a webpage. Most meta
    tags will use a `name` and `content` pair for type of metadata and its value.

````html
<!-- Sets the character encoding to utf-8 -->
<meta charset="utf-8" />

<!-- Allows for custom responsive CSS, rather than the default scaling behavior of small devices -->
<meta name="viewport" content="width=device-width, initial-scale=1" />

<!-- Sets the page author -->
<meta name="author" content="Stephen Choung" />
<!-- Sets the page description -->
<meta name="description" content="MetaTag Descriptions" />
````

&lt;Favicon&gt;
- The icon for a webpage. Browsers usually
  show these in a variety of places, such as next to the tab name.Favicons are created using the &lt;link&gt; tag.
````html
<link rel="icon" href="favicon.png" />
````
&lt;base&gt;
A tag for setting the document base URL, which will be used for all relative links on the page.
````html
<!-- This line goes in the <head> -->
<base href="https://algoexpert.io"/>

<!-- This would go to https://algoexpert.io/frontend -->
<a href="/frontend">FrontendExpert</a>
````

````html
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>My First Webpage</title>

    <meta name="author" content="FrontendExpert" />
    <base href="https://algoexpert.io" />
  </head>
  <body>
    <p>
      This link is relative to the base:
      <a href="/frontend" target="_blank">Frontend Expert</a>!
    </p>
  </body>
</html>
````
