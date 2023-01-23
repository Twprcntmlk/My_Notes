# Summary

|Order	|DOMContentLoaded|
|----------|:-------------:|
|async|Load-first order. Their document order doesn’t matter – which loads first runs first Irrelevant. May load and execute while the document has not yet been fully downloaded. That happens if scripts are small or cached, and the document is long enough.|
|defer	|Document order (as they go in the document).	Execute after the document is loaded and parsed (they wait if needed), right before DOMContentLoaded.|

### In practice, defer is used for scripts that need the whole DOM and/or their relative execution order is important.

### And async is used for independent scripts, like counters or ads. And their relative execution order does not matter.




## defer
- The defer attribute tells the browser not to wait for the script. Instead, the browser will continue to process the HTML, build DOM. The script loads “in the background”, and then runs when the DOM is fully built.

- Here’s the same example as above, but with defer:
````html
<p>...content before script...</p>

<script defer src="https://javascript.info/article/script-async-defer/long.js?speed=1"></script>

<!-- visible immediately -->
<p>...content after script...</p>
````

## async
- The async attribute is somewhat like defer. It also makes the script non-blocking. But it has important differences in the behavior.

- The async attribute means that a script is completely independent:

- The browser doesn’t block on async scripts (like defer).
Other scripts don’t wait for async scripts, and async scripts don’t wait for them.
DOMContentLoaded and async scripts don’t wait for each other:
DOMContentLoaded may happen both before an async script (if an async script finishes loading after the page is complete)
- …or after an async script (if an async script is short or was in HTTP-cache)
In other words, async scripts load in the background and run when ready. The DOM and other scripts don’t wait for them, and they don’t wait for anything. A fully independent script that runs when loaded. As simple, as it can get, right? */}
