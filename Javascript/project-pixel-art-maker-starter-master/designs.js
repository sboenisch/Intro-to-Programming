// Create a grid of cells depending on the width and height values
function makeGrid() {
    // Get Inputs
    const width = document.getElementById("inputWidth").value;
    const height = document.getElementById("inputHeight").value;
    const grid = document.getElementById("pixelCanvas");
    grid.innerHTML = '';
    // Create Rows
    for(var i = 0; i < height; i++){
        var row = document.createElement('tr');
        // Create Columns
        for(var y = 0; y < width; y++){
            var cell = document.createElement('td');
            // Content of cell is empty
            cell.append(document.createTextNode(''));
            row.append(cell);
            cell.addEventListener('click',colorClick);
        };
        grid.appendChild(row);
    };
};


// Change Backgroundcolor after click of cell
function colorClick(c){
    const color = document.getElementById("colorPicker").value;
    var clickedOn = c.target;
    clickedOn.style.backgroundColor =  color;
}


// Run makeGrid()-Function after submit Button
document.getElementById('sizePicker').onsubmit = function (){
    event.preventDefault();
    makeGrid();
};
