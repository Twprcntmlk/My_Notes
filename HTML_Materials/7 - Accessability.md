
### Accessibility
- Building applications usable by as many people as possible.
  Oftentimes this means utilizing semantic HTML and ensuring the application works properly with various assistive technologies.
### Accessibility Tree
- A tree representation of the page focusing on information specific to accessibility. Each node in this tree contains information such as the: role, state, name, and descrption

### WAI-ARIA
- The "Web Accessibility Initiative - Accessible Rich Internet Applications" specification for accessible HTML created by the World Wide Web Consortium (W3C). Oftentimes referred to as just ARIA, this contains a set of HTML attributes that can be added to provide extra information to the accessibility tree


- ARIA attributes are usually grouped into three main categories:
#### Roles: What the element is doing, used to define the purpose of the element.
These can be broken down into a few main subgroups:

  - Landmarks: Major content areas, navigational landmarks.
  - Structure: Document structure information.
  - Widget: Interactive elements.
  - Window: Sub-windows in the browser.:
  - Live Region: Regions with dynamically changing content.
#### Properties: Extra meaning and characteristics of the element, such as labels.

#### States: Current state of the element, such as if it is disabled.




````html
<div role="dialog" aria-labelledby="title">
  <h1 id="title">Dialog Heading</h1>
  <p>
    The aria role and label don't change the output at all visually,
    but this dialog is more accessible now!
  </p>
</div>
````
