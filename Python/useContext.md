### Probably the most common use is for themes, ccs styling

- App() is parent of Profile()
- we can use <UserContext.Provider> to wrap a component

````Javascript
const UserContext = createContext({
    name: null,
  });

  function App() {
    return (
      <>
        <UserContext.Provider
          value={{
            name: 'Conner',
          }}>
          <Profile />
        </UserContext.Provider>
      </>
    );
  }
````

- Then in the child component we can use
- const user = useContext(UserContext) to access those values from above
-
````Javascript
  function Profile() {
    const user = useContext(UserContext);
    return <p>Hello {user.name}</p>;
  }
````

- Custom useContext
````Javascript
import { createContext } from 'react';

export const UserContext = createContext({
    toggleUser:null,
    user:{
        name:null,
        course: null
    }

});

const person1={
    name:"person1" ,
    course:"course123"
}

const person2={
    name:"person2",
    course: "course456"
}

export function UserContextProvider({children}){
    const [user, setUser] = useState(person1)

    const toggleUser = () =>{
        if (user === person1){
            setUser(person2)
        } else {
            setUser(person1)
        }
    }

    return (
        <UserContext.Provider value=({user, toggleUser})>
            {children}
        </UserContext.Provider>
    )
}
````
// But button does not have access to toggleUser from <UserContextProvider>
````Javascript
function App() {
    return (
      <>
        <UserContextProvider>
          <Profile />
        </UserContextProvider>
        <button onClick={toggleUser}>Toggle User</button>
      </>
    );
  }
````
// Helper function
````Javascript
function AppInternal (){
    const { toggleUser} = useContext(UserContext)
    return (
        <>
            <Profile/>
            <button onClick={toggleUser}>Toggle User</button>
        </>
    )
}
````
// now the app becomes
````Javascript
function App() {
    return (
      <>
        <UserContextProvider>
            <AppInternal/>
        </UserContextProvider>
      </>
    );
  }
````
