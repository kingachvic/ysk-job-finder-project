import './App.css';
import React from 'react';
import Hello from  './components';
import Jobs from './jobs';
import { BrowserRouter as Router, Route, Switch, Redirect, Link } from 'react-router-dom'

function App() {
  return(
    <div className = 'app'>
      <Router>
      	<Route exact path = '/' component = {Hello}/>
      	<Route path = '/jobs' component = {Jobs}/>
      </Router>
    </div>
  );
}

export default App;
