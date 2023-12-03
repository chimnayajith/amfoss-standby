import React from 'react'
import { Link } from 'react-router-dom'
import { ReactComponent as CreateIcon } from '../assets/add.svg'

const CreateButton = () => {
  return (
    <Link to="/note/new" className='floating-button'>
        <CreateIcon />
    </Link>
  )
}

export default CreateButton
