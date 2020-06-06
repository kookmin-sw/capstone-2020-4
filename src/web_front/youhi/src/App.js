import React, { Component } from 'react';
import './App.css';
import Home from './Home';
import Skill from './Skill';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import styled from 'styled-components';
import Navbar from './component/navbar/Navbar';
import Footer from './component/footer/footer';

const StyledWrapper = styled.div`
  display: flex;
  justify-content: center;
  .innerDiv {
    width: 100%;
  }
`;
class App extends Component {
  render() {
    return (
      <Router>
      <Navbar />
        <StyledWrapper>
          <div className="innerDiv">
            <Route exact path ='/' component = { Home }/>
            <Route path = '/skill' component = { Skill }/>
          </div>
        </StyledWrapper>
      </Router>
    )
  }
}

export default App;
