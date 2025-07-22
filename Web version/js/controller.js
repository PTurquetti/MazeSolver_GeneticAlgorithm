function startAlgorithm(){

    //get parameters
    

    startLoading();

    const map = document.querySelector("#map_container");
    const cells = map.querySelectorAll("div");

    let matrix = []

    let maxRow = 0;
    let maxCol = 0;

    for(let x=0; x<=maxRow; x++){
        matrix[x] = [];
        for(let y=0; y<=maxCol; y++){
            matrix[x][y] = 0;
        }
    }

    cells.forEach(cell => {
        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);
        const status = parseInt(cell.dataset.status);
        matrix[row][col] = status;
    });

    console.log(matrix)
}