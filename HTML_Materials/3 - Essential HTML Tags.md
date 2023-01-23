## Essential HTML Tags

# &lt;p&gt; [link](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
````html
The paragraph tag, usually used for blocks of text (although they can
contain other elements that are part of the paragraph, such as images).

For example:
<p>Hello World!</p>:

````
# Heading Tags [link](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)
````html
HTML tags represented by <h1> through <h6>
````
# &lt;img&gt;
- <b>src:</b> The path to the image, either relative or absolute.

- <b>alt:</b> Alternative text to be used with screen readers or any time the image cannot be displayed.
````html
<img src="img/dog.png" alt="dog />
````
# &lt;ul&gt;
- The unordered list tag, used for a list where the order does not matter.By default, most browsers will show this as a bulleted list.
````html
<ul>
    <li>Chicken</li>
    <li>Horse</li>
    <li>Llama</li>
    <li>Cow</li>
</ul>
````

# &lt;ol&gt;
  - The ordered list tag, used for a list where the order matters.
  By default, most browsers will show this as a numbered list.
  ````html
  <ol>
      <li>List Item 1</li>
      <li>List Item 2</li>
      <li>List Item 3</li>
      <li>List Item 4</li>
  </ol>
  ````
# &lt;li&gt;
- The list item tag, used for individual elements in both unordered and ordered lists.
  ````html
  <ol>
      <li>Step 1: </li>
      <li>Step 2:
        <ol>
            <li> Substep 1: </li>
            <li> Substep 2: </li>
        </ol>
      </li>
      <li>Step 2:</li>
  </ol>
  ````
# &lt;pre&gt;
- The preformatted text tag. This tag preserves whitespace, which can be useful when indentation and newlines need to be preserved.
````html
<pre>
     *
    ***
   *****
  *******
    | |
</pre>
````
# &lt;br&gt;
- The line break tag. This is an empty tag used to create a line break in text, such as for the introduction of an email or new lines in a poem. However, this tag should not be used just for spacing out elements as that can be accomplished with CSS.
````html
<p>
    Dear User, <br/>
    We hope you are enjoying learning
</p>

````
# &lt;a&gt;
- The anchor tag, used for linking to other pages. This tag should include an  attribute with the path to the page being linked (absolute or relative).
````html
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a"> a </a>
````


# &lt;em&gt;
- The emphasis tag, usually rendered as italics by default in the browser.
````html
<p>I <em>need</em> to study! </p>
````

# &lt;strong&gt;
````html
<p>I <strong>Note:</strong> to study! </p>
````
