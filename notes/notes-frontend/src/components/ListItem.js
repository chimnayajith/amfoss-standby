import React from 'react'
import {Link} from 'react-router-dom'


let getTime = (date) => {
  const dateOptions = { day : '2-digit' , month:'2-digit' , year:'numeric'}
  return new Date(date).toLocaleDateString(undefined , dateOptions)

}

let currentTime = () => {
  const now = new Date()
  return now.toISOString()
} 
let getTitle = (note) => {
  let title = note.body.split('\n')[0]
  if (title.length > 45){
    return title.slice(0,45) + '...'
  } else {
  return title
  }
}

const ListItem = ({note}) => {
  return (
    <div>
        <Link to={`note/${note.id}`}>
            <div style={{
            borderRight: `6px solid ${
              note.deadline && (note.deadline < currentTime()) ? 'red' : 'green'
            }` }} className='notes-list-item'>
                <h3>{getTitle(note)}</h3>
                <p><span>{getTime(note.updatedAt)}</span> | Deadline :   {note.deadline ? getTime(note.deadline) : 'Not set'}</p>
            </div>
        </Link>
    </div>
  )
}

export default ListItem