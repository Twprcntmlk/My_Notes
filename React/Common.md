### Notes

## Starting React
[React Typescript] https://create-react-app.dev/docs/adding-typescript/
````Typescript
npx create-react-app my-app --template typescript
````

## SyntheticEvent
- The object type passed to React event handler functions. Synthetic events
  generally work the same as native events, but with more consistency across
  browsers.

## Component LifeCycle
- The different stages that an instance of a component goes through. There are three primary stages to the React lifecycle:
1. Mounting : The component renders for the first time.
2. Updating : The component re-renders whenever state changes or the
    props are updated by the parent component. A component can update many
    times without ever mounting again.
3. Unmounting : The component is removed from the DOM. This is the final
    stage of the lifecycle, and a component cannot update again once it has
    been unmounted. However, a new instance of the component can still be mounted.

## Hook
- A JavaScript function used to "hook" into React features such as state and
  the larger component lifecycle. The names of hooks always begin with `use`,
  and they cannot be called conditionally.

## useReducer
- An alternative React hook for creating stateful components, oftentimes used
  for more complex state. The `useReducer` function takes in a
  reducer function and the initial state. It returns an array with two
  elements: the current state value and a dispatch function.
- The reducer function takes in the previous state and an action object
  as parameters, then it returns the new state. Usually the action object will
  have a `type` property, which will be used in a switch statement.
  For example:
````javascript
function reducer(state, action){
    swtich (action.type) {
        case 'increment':
            return {count: state.count + action.num};
        case 'decrement':
            return {count: state.count - action.num};
        default:
            throw new Error ('Unknown action type')
    }
}
````

  The dispatch function will then take in an object, which will be passed as
  the action to the reducer function. For example:
````javascript
const [state, dispatch] = useReducer(reducer, {count:0})

return (
    <button onClick={()=> dispatch({
        type:'increment',
        num: 1
    })}>
        Increment
       </button>
)
````
[Learn-More]https://reactjs.org/docs/hooks-reference.html#usereducer

### Lifting State Up
- A common React pattern of moving shared state up to the lowest common
  ancestor component in the tree. This allows for a single component to keep
  track of the state and pass the current value and setter function down
  through props.

### Controlled Component
-
  A pattern of using React state to control the current state of an input,
  rather than allowing the native elements to control their own state (known as
  an `uncontrolled component`). For example, an input can be controlled via
  the `value` and `onChange` props (note that in React, `onChange`  works the same as
`onInput`). For example:
```` javascript
const [value, setValue] = useState('')
return <input value={value} onChange={e=>setValue(e.target.value)} />
````

### useRef
- useRef is mostly used to get reference to a hmtl property in a component so it can be modified.
-[youtube]https://www.youtube.com/watch?v=t2ypzz6gJm0
- like State but in that it:
  - - persists between renders
- BUT:
  - - Doesn't not cause component to re-update
```
const renderCount = useRef()

// renderCount is below
// renderCount: {current:0}

useEffect(()=>{
    renderCount.current+=1
})
```

### useImperativeHandle
- useImperativeHandle customizes the instance value that is exposed to parent components when using ref. As always, imperative code using refs should be avoided in most cases. useImperativeHandle should be used with forwardRef:
- custom components do not have ref so we need to forward to the custom input.

#### takes 3 inputs
- useImperativeHandle(ref, function(), [array of dependencies like useEffect] )

[youtube]https://www.youtube.com/watch?v=zpEyAOkytkU
````javascript
function FancyInput(props, ref) {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => {
      inputRef.current.focus();
    }
  }));
  return <input ref={inputRef} ... />;
}
FancyInput = forwardRef(FancyInput);

````
