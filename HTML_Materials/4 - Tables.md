## HTML
- &lt;tr&gt;: A single row in the table.
- &lt;th&gt;: A heading in the table. This should be used with:
  ````html
  <th scope="col">Category</th>
  <th scope="row">Food</th>
  ````
- &lt;td&gt;: A single piece of data in the table, also referred to as a cell.
- &lt;thead&gt;: A grouping tag for the heading of a table, usually containing a single
- &lt;tbody&gt;: A grouping tag for the body of the table, used for containing the primary rows of data.
- &lt;tfoot&gt;: A grouping tag for the footer of the table.
- &lt;caption&gt;: A caption or title for the table.

````html
<table>
  <caption>Budget</caption>

  <thead>
    <tr>
      <th scope="col">Category</th>
      <th scope="col">Budget</th>
      <th scope="col">Spending</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Food</th>
      <td>$200</td>
      <td>$100</td>
    </tr>

    <tr>
      <th scope="row">Entertainment</th>
      <td>$250</td>
      <td>$300</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <th>Total</th>
      <td>$450</td>
      <td>$400</td>
    </tr>
  </tfoot>
</table>
````
