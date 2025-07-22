let selectingStart = false;
let startCell = null;

let selectingEnd = false;
let endCell = null;

function create_maze(){
    const rows = document.querySelector("#nrows").value;
    const cols = document.querySelector("#ncols").value;
    const mapContainer = document.querySelector("#map_container");

    console.log(`Creating ${rows}x${cols} map`);

    mapContainer.innerHTML = "";
    mapContainer.style.gridTemplateColumns = `repeat(${cols}, 42px)`;

    for(let i=0; i<rows; i++){
        for(let j=0; j<cols; j++){

            const cell = document.createElement("div");
            cell.classList.add("mapCell");
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.dataset.status = 0;

            cell.addEventListener("click", () => switchCellStatus(cell));

            

            mapContainer.appendChild(cell);

        }
    }

    document.querySelector("#maze_creator").style.display="flex";
    document.querySelector("#btn_createMaze").innerHTML="Reset Maze"
}

function switchCellStatus(cell){

    if(selectingStart){

        if (startCell) {
            startCell.dataset.status = 0;
        }

        cell.dataset.status = 2;
        startCell = cell;
        
    }else if(selectingEnd){
        if (endCell) {
            endCell.dataset.status = 0;
        }

        cell.dataset.status = 3;
        endCell = cell;
    }

    if(cell.dataset.status === "0"){
        cell.dataset.status = 1;
    }else if(cell.dataset.status === "1"){
        cell.dataset.status = 0;
    }
    
}

function selectStart(btn){
    selectingStart = !selectingStart

    if(selectingStart){
        btn.style.border = "3px solid blue"
        selectingEnd = false;
        document.querySelector("#btn_selEnd").style.border="none";
        document.querySelector("#btn_selWall").style.border="none";
    }else{
        btn.style.border = "none";
    }
}

function selectEnd(btn){
    selectingEnd = !selectingEnd

    if(selectingEnd){
        btn.style.border = "3px solid red"
        selectingStart = false;
        document.querySelector("#btn_selStart").style.border="none";
        document.querySelector("#btn_selWall").style.border="none";
    }else{
        btn.style.border = "none";
    }

}

function selectWall(btn){
    selectingStart = false;
    selectingEnd = false;
    document.querySelector("#btn_selStart").style.border="none";
    document.querySelector("#btn_selEnd").style.border="none";
    btn.style.border = "3px solid black"
}

function startLoading(){
    document.querySelector("#loading").style.display="flex";
}

function stopLoading(){
    document.querySelector("#loading").style.display="none";
}

function toggleDropdown(header) {
    const content = header.nextElementSibling;
    const arrow = header.querySelector('.arrow');

    content.classList.toggle('open');
    arrow.classList.toggle('rotate');

    if (content.classList.contains('open')) {
        content.style.maxHeight = parseInt(content.scrollHeight + 100) + "px";
    } else {
        content.style.maxHeight = null;
    }
}

