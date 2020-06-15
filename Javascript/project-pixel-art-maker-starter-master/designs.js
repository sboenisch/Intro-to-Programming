// Create a grid of cells depending on the width and height values
function makeGrid() {
    // Get Inputs
    const width = document.getElementById("inputWidth").value;
    const height = document.getElementById("inputHeight").value;
    const table = document.getElementById("pixelCanvas");
    table.innerHTML = '';
    // Create Rows
    for(let i = 0; i < height; i++){
        // let row = document.createElement('tr');
        let row = table.insertRow(i);
        // Create Columns
        for(let y = 0; y < width; y++){
            // let cell = document.createElement('td');
            let cell = row.insertCell(y);
            // Content of cell is empty
            // cell.append(document.createTextNode(''));
            // row.append(cell);
            cell.addEventListener('click',colorClick);
        };
        //grid.appendChild(row);
    };
};


// Change Backgroundcolor after click of cell
function colorClick(c){
    const color = document.getElementById("colorPicker").value;
    let clickedOn = c.target;
    clickedOn.style.backgroundColor =  color;
}


// Run makeGrid()-Function after submit Button
document.getElementById('sizePicker').onsubmit = function (){
    event.preventDefault();
    makeGrid();
};
