import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  render() {
    axios.get('http://localhost:5000/').then((Response)=>{
        console.log(Response);
    }).catch((Error)=>{
        console.log(Error);
    })

    return (
      <div>
        <h2>hello</h2>

      </div>
    );
  }
}

export default App;