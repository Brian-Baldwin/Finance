import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function Asset(number) {
  return (
  <>
  <label for="asset1">Asset 1: </label>
  <input type="text" id="asset1" name="asset1"/>
  <label for="alloc1"> Percent Allocation: </label>
  <input type="text" id="alloc1" name="alloc1"/>
  </>
  );
}

const main = (
  <div>
  <head>
      <title>Portfolio Backtester</title>
  </head>

    <h1>Portfolio Backtester</h1>
    <p>Input a stock portfolio below with each stock's respective allocations and see how it performs.</p>
    <br/>
    <br/>
    <h2><b>Portfolio Holdings</b></h2>
    <form>
        <label for="start"><b>Starting date </b></label>
        <input type="month" id="start" name="start"/>
        <br/>
        <br/>
        <label for="end"><b>Ending date </b></label>
        <input type="month" id="end" name="end"/>
        <br/>
        <br/>
        <label for="bench"><b>Benchmark </b></label>
        <input type="text" id="bench" name="bench"/>

        <br/>
        <h2><b>Portfolio Holdings</b></h2>
        {/*
        <label for="asset1">Asset 1: </label>
        <input type="text" id="asset1" name="asset1"/>
        <label for="alloc1"> Percent Allocation: </label>
        <input type="text" id="alloc1" name="alloc1"/>
        <br/>
        <label for="asset2">Asset 2: </label>
        <input type="text" id="asset2" name="asset2"/>
        <br/>
        <label for="asset3">Asset 3: </label>
        <input type="text" id="asset3" name="asset3"/>
        <br/>
        <label for="asset4">Asset 4: </label>
        <input type="text" id="asset4" name="asset4"/>
        <br/>
        <label for="asset5">Asset 5: </label>
        <input type="text" id="asset5" name="asset5"/>
        <br/>
        <label for="asset6">Asset 6: </label>
        <input type="text" id="asset6" name="asset6"/>
        <br/>
        <label for="asset7">Asset 7: </label>
        <input type="text" id="asset7" name="asset7"/>
        <br/>
        <label for="asset8">Asset 8: </label>
        <input type="text" id="asset8" name="asset8"/>
        <br/>
        <label for="asset9">Asset 9: </label>
        <input type="text" id="asset9" name="asset9"/>
        <br/>
        <label for="asset10">Asset 10: </label>
        <input type="text" id="asset10" name="asset10"/> 
        */}
        <br/>
        <br/>
        <br/>
        <input type="submit" value="Compare"/>
    </form>
</div>
);

//export default App;
ReactDOM.render(main, document.getElementById('root'));

<body>
  <div id="root"></div>
</body>