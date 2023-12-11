import React , {useState , useEffect} from 'react'
import { useParams , useNavigate } from 'react-router-dom' 
import { ReactComponent as Trash } from '../assets/trash.svg'

const EachNote = () => {
  let {id} = useParams()
  let history = useNavigate()

  let [note , setNote] = useState({body: '' , deadline: null})
  useEffect(() => {
    getNote()
  },[])

  let getNote = async () => {
    if( id === 'new') return;
    let response = await fetch(`/api/notes/${id}`)
    let data = await response.json()
    setNote(data)
  }

  let handleTextChange = (e) => {
    setNote(note => ({
      ...note,
      'body': e.target.value,
    }))
  };


  let handleDeadlineChange = (e) => {
    const deadline = new Date(e.target.value).toISOString().slice(0, 19) + 'Z'
    setNote(note => ({
      ...note,
      'deadline' : deadline
    }))
  };

  let createNote = async() => {
    fetch(`/api/notes/create/` , {
      method : "POST",
      headers:{
        'Content-Type' : 'application/json',
      },
      body : JSON.stringify(note)
    })
  }

  let updateNote = async() => {
    fetch(`/api/notes/${id}/update/` , {
      method : "PUT",
      headers:{
        'Content-Type' : 'application/json',
      },
      body :JSON.stringify(note)
    })
  }

  let deleteNote = async () => {
    fetch(`/api/notes/${id}/delete/`,{
      method:'DELETE',
      headers : {
        'Content-Type' : 'application/json'
      },
    })
    history('/')
  }


  let handleUpdate = () => {
    if(id !== 'new' && note.body === ''){
      deleteNote()
    } else if (id !== 'new'){
      updateNote()
    } else if (id === 'new' && note.body !== null && note.body !== ''){
      createNote()
    }
    history('/')
  }

  return (
    <div className={`note ${new Date(note.deadline) < new Date() && note.deadline ? 'deadline' : ''}`}>
        <div className='note-header'>
            <h3 onClick={handleUpdate}>
              &#8592; Go Back
            </h3>
            {id !== 'new' ? (
            <button onClick={deleteNote}><Trash width="35" height="35"/></button>
  
            ): (
            <button onClick={handleUpdate} className='done-button'>Done &#10004;</button>
              
            )}
        </div>
        <textarea onChange={(e) => {handleTextChange(e)}} value={note.body}></textarea>
        <div className="datetime-container">
          <label htmlFor="datetime">Deadline (Optional) : </label>
          <input onChange={(e) => {handleDeadlineChange(e)}} type="datetime-local" id="datetime" name="datetime" value={note.deadline? note.deadline.slice(0, 16) : null }/> 
      </div>
    </div>
  )
}

export default EachNote



