import React, { useState, useRef, useEffect } from "react";

const PhotoEditingComponent = () => {
  const [image, setImage] = useState(null);
  const [selectedFilter, setSelectedFilter] = useState('original');
  const canvasRef = useRef(null)

  const filters = [
    {
      name: 'original',
      label: "Orginal",
    },
    {
      name: "invert",
      label: "Invert",
    },
    { 
      name: "grayscale", 
      label: "Grayscale" 
    },
    { 
      name: "sepia", 
      label: "Sepia" 
    },
  ];

  //base64 encoding on uploading a file
  const handleFileChange = (e) => {
    const img = e.target.files[0];
    if (img) {
      const reader = new FileReader();
      reader.onload = () => {
        setImage(reader.result);
      };
      reader.readAsDataURL(img);
    }
  };
 useEffect(() => {
  const canvas = canvasRef.current
  if(!canvas || !image) return;

  const ctx = canvas.getContext('2d')
  const img = new Image()
  
  img.onload = () => {
    canvas.width = img.width
    canvas.height = img.height

    if (selectedFilter === "grayscale") {
      ctx.filter = "grayscale(100%)";
    } else if (selectedFilter === "invert") {
      ctx.filter = "invert(100%)";
    } else if (selectedFilter === "sepia") {
      ctx.filter = "sepia(100%)";
    } else {
      ctx.filter = "none";
    }
    ctx.drawImage(img , 0,0)

    ctx.filter = 'none' //ressetting the filter
  }
  img.src = image
 },[image , selectedFilter])
 

 const handleSave = () => {
  const canvas = canvasRef.current;

    const editedImage = canvas.toDataURL('image/png');

    const downloadLink = document.createElement('a')
    downloadLink.href = editedImage
    downloadLink.download = 'edited_image.png'

    document.body.appendChild(downloadLink)
    downloadLink.click()
    document.body.removeChild(downloadLink)
  }

  return (
    <div style={{ maxWidth: "900px", margin: "auto" }}>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {image && (
        <div>
          <label>Select Filter: </label>
          <select
            value={selectedFilter}
            onChange={(e) =>
              setSelectedFilter(e.target.value)
            }
          >
            {filters.map((filter) => (
              <option key={filter.name} value={filter.name}>
                {filter.label}
              </option>
            ))}
          </select>
          <div style={{ maxWidth: "600px", margin: "auto" }}>
            <canvas ref={canvasRef} style={{ maxWidth: "100%", height:'auto' }}/>
          </div>
          <button onClick={handleSave}>Save Image</button>
        </div>
      )}
    </div>
  );
};

export default PhotoEditingComponent;
