import React , {useState , useEffect} from 'react'
import ListItem from '../components/ListItem'
import CreateButton from '../components/CreateButton'
import { ReactComponent as NoteIcon } from '../assets/notes.svg' 

const NotesList = () => {

  let [notes , setNotes] = useState([  ])
  useEffect(() => {
    getNotes()
  },[])

  let getNotes = async () => {
    let response = await fetch('/api/notes')
    let data = await response.json()
    setNotes(data)
  }

  return (  
    <div className='notes'>
        <div className='notes-header app-header'>
          <h2 className='notes-title'><NoteIcon height="30px" width="30px"/> My Notes</h2>
          <p className='notes-count'>{notes.length}</p>
        </div>
        <div className='notes-list'>
            {notes.map((note, i)=> (
                <ListItem key={i} note={note}/>
            ))}
        </div>
        <CreateButton/>
    </div>
  )
}

export default NotesList