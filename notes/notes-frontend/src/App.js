import './App.css';
import NotesList from './pages/NotesList'
import EachNote from './pages/EachNote'
import { useState } from 'react'
import {
  BrowserRouter as Router, Route, Routes
} from "react-router-dom";
import { ReactComponent as Sun} from './assets/sun.svg'
import { ReactComponent as Moon} from './assets/moon.svg'


function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <Router>
      
      <div className={`container ${isDarkMode ? 'dark' : ''}`}>
      <button onClick={toggleDarkMode} className={`mode-switch ${isDarkMode ? 'dark' : 'light'}`}>
        {isDarkMode ? <Sun/> : <Moon/>}
      </button>
          <div className='app'>
            <Routes>
              <Route path='/' exact element={<NotesList />} />
              <Route path='/note/:id' element={<EachNote/>}/>
            </Routes>
          </div>
      </div>
    </Router>
  );
}

export default App;
