
## event.preventDefault()
This method prevents default actions that browsers make when an event is triggered.

Here are some examples of default actions on webpages and how to override them with event.preventDefault().
````javascript
const form = document.getElementById('form')

form.addEventListener('submit', (event) => {
  event.preventDefault()

  // process data and submit a request manually
})
````

## event.stopPropagation()
Propagation is the act of spreading something, in this case, events. The stopPropagation method is used to prevent the spreading of events when an event is triggered on an element.

In JavaScript, when you trigger an event on an element, it bubbles up the tree to the parents and ancestors of that element. Basically, the element with the event is "inside" the parent's container, so the parent also receives the events.

````javascript
span.addEventListener('click', (event) => {
  event.stopPropagation()
  console.log("span was clicked")
})
````
