import React, { useState , useRef } from "react";
import ImageFilter from "react-image-filter";

const PhotoEditingComponent = () => {
  // matrix for the orginal filter
  const orginal_filter = [
    1, 0, 0, 0, 0, 
    0, 1, 0, 0, 0, 
    0, 0, 1, 0, 0, 
    0, 0, 0, 1, 0,
  ]

  const [image, setImage] = useState(null);
  const [selectedFilter, setSelectedFilter] = useState(orginal_filter);
  const canvasRef = useRef(null)
  // List of available filters
  const filters = [
    {
      name: orginal_filter,
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

  const handleSave = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    const img = new Image()
    img.onload = () => {
      ctx.clearRect(0,0,canvas.width , canvas.height);
      ctx.drawImage(img , 0 , 0 , canvas.width , canvas.height);

      const editedImage = canvas.toDataURL('image/png');

      const downloadLink = document.createElement('a')
      downloadLink.href = editedImage
      downloadLink.download = 'edited_image.png'

      document.body.appendChild(downloadLink)
      downloadLink.click()
      document.body.removeChild(downloadLink)
    }
    img.src = image
  }
  return (
    <div>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {image && (
        <div>
          <label>Select Filter: </label>
          <select
            value={JSON.stringify(selectedFilter)}
            onChange={(e) => setSelectedFilter(JSON.parse(e.target.value))}
          >
            {filters.map((filter) => (
              <option key={filter.name} value={JSON.stringify(filter.name)}>
                {filter.label}
              </option>
            ))}
          </select>
          <div>
          <canvas ref={canvasRef} width={500} height={500} />
            <ImageFilter image={image} filter={selectedFilter} ref={canvasRef} />
          </div>
          <button onClick={handleSave}>Save Image</button>
        </div>
      )}
    </div>
  );
};

export default PhotoEditingComponent;
