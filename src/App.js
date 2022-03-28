import { useState } from 'react';
import './App.css';

function App() {
    const [formFields, setFormFields] = useState([
      {asset: '', allocation: ''}
    ])
  
    const handleFormChange = (index, event) => {
      let data = [...formFields];
      data[index][event.target.name] = event.target.value;
      setFormFields(data);
    }
  
    const addFields = () => {
      let object = {
        asset: '',
        allocation: ''
      }
  
      setFormFields([...formFields, object])
    }
  
    const removeFields = (index) => {
      let data = [...formFields];
      data.splice(index, 1)
      setFormFields(data)
    }
  
    const submit = (e) => {
      e.preventDefault();
      console.log(formFields)
    }
  
    return (
      <div className='index'>
      <head>
          <title>Portfolio Backtester</title>
      </head>
  
        <h1>Portfolio Backtester</h1>
        <p>Input a stock portfolio below with each stock's respective allocation and a start and end date to see how it performs.</p>
        <br/>
        <br/>
        
        <form>
            <label for="start"><b>Starting date </b></label>
            <input type="month" id="start" name="start"/>
            <br />
            <br />
            <label for="end"><b>Ending date </b></label>
            <input type="month" id="end" name="end"/>
            <br />
            <br />
            <label for="bench"><b>Benchmark </b></label>
            <input type="text" id="bench" name="bench"/>
            <br />
            <h2><b>Portfolio Holdings</b></h2>
            {formFields.map((input, index) => {
              return (
                <div key={index}>
                <input 
                  name="asset"
                  placeholder="Ticker"
                  value={input.name}
                  onChange={event => handleFormChange(index, event)}
                />
                <input
                  name="allocation"
                  placeholder="Percent Allocation"
                  value={input.name}
                  onChange={event => handleFormChange(index, event)}
                />
                <br />
                </div>
              )
            })}
            <br />
            <br />
            <br />
        </form>
        <br />
        <button onClick={addFields}>Add another asset</button>
        <br />
        <button onClick={submit}>Compare</button>
        </div>
    );
  }

  export default App;