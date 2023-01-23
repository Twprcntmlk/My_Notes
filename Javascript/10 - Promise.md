## Promise
- An object used for asynchronous operations. These objects have a state of either `pending, fulfilled, or rejected`. A Promise is created with the `Promise()` constructor, which takes in a callback function, oftentimes called the <b>executor</b>. This callback function has two callback functions as parameters:
- resolve(value): Fulfills the Promise and sets its value.
- reject(error): Rejects the Promise and sets an error message.

### The Promise object has three primary functions:
- then(fulfilledFn rejectedFn): Calls fulfilledFn if the Promise is
    fulfilled and rejectedFn if it is rejected. Returns a new fulfilled Promise
    with the return value of the callback function.

- catch(rejectedFn): Calls rejectedFn if the Promise is rejected. returns a new
    fulfilled Promise with the return value of the callback function.

- finally(callback): Calls the callback function whenever the Promise is <b>settled</b> (fulfilled or rejected).

Since these functions all return a new Promise, they can be chained together, such as `promise.then(doX).then(doY).catch(handleError).finally(doZ)`

## Async/Await
[Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
[Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

````Typescript
interface SearchFn {
    (subString: string): Promise<boolean>;
}

type SearchFn = (subString: string) => Promise<boolean>;
````

````Typescript
type GetNumber = (num: number) => Promise<number>;

// ✅ Arrow function with Type
const getNumber: GetNumber = async (num) => {
  const result = await Promise.resolve(num);

  return result;
};

interface IGetNumber {
  (num: number): Promise<number>;
}

// ✅ Arrow function with Interface
const getNumber2: IGetNumber = async (num) => {
  const result = await Promise.resolve(num);

  return result;
};

// ✅ Arrow function inline
const getNumber3 = async (num: number): Promise<number> => {
  const result = await Promise.resolve(num);

  return result;
};

// ✅ Named function inline
async function getNumber4(num: number): Promise<number> {
  const result = await Promise.resolve(num);

  return result;
}
````
