## Portal

- A built-in method for rendering React elements into a DOM node outside
of the parent React tree.

- A portal is created by using the `ReactDOM.createPortal`
function, which takes in a React element as the first parameter and the
DOM node as the second parameter. The element will be appended to that DOM
node, but it will still act the same as any other element in the original
React tree (it can still take props, read from context providers and have
events bubble up).

[label](https://reactjs.org/docs/portals.html)

````JSX
// Welcome to our Playground!

function App() {
  const [isHidden, setIsHidden] = useState(true);
  return (
    <>
      <div className="container">
        <button onClick={() => setIsHidden(!isHidden)}>
          {isHidden ? 'Show Modal' : 'Hide Modal'}
        </button>
        {isHidden || <Modal />}
      </div>

      <p className="other">Other Content</p>
    </>
  );
}

function Modal() {
  return createPortal(<p className="modal" style={{color:"black"}}>Modal</p>, document.getElementById('portal-root'));
}

````
