import {useState} from "react";

function App(){
    const [names, setNames] = useState(null)

    const onLoad = async () => {
        const names = (await import("./names")).default;

        const makeUpperCase = await import("./utilities").makeUpperCase;
        setNames(makeUpperCase(names));
    }

}
