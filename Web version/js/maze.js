export class Maze{

    constructor(nRows, nCols, matrix, startPos, endPos){
        this.nRows = nRows;
        this.nCols = nCols;
        this.matrix = matrix;
        this.startPos = startPos;
        this.endPos = endPos;
    }


    printMaze(matrix = null) {
        const displayMatrix = matrix || this.cellMatrix;

        console.log("This is the maze:");
        for (let i = 0; i < this.nRows; i++) {
            console.log(displayMatrix[i].join(" "));
        }

        // Create a container div for the maze
        const container = document.createElement("div");
        container.style.display = "grid";
        container.style.gridTemplateRows = `repeat(${this.nRows}, 30px)`;
        container.style.gridTemplateColumns = `repeat(${this.nCols}, 30px)`;
        container.style.gap = "2px";
        container.style.margin = "10px";

        // Add cells to the grid
        for (let i = 0; i < this.nRows; i++) {
            for (let j = 0; j < this.nCols; j++) {
                const cell = document.createElement("div");
                cell.style.width = "30px";
                cell.style.height = "30px";
                cell.style.border = "1px solid #ccc";
                cell.style.boxSizing = "border-box";
                cell.style.backgroundColor = this.getCellColor(displayMatrix, i, j);

                container.appendChild(cell);
            }
        }

        // Append maze to body
        document.body.appendChild(container);
    }

    getCellColor(matrix, i, j) {
        if (matrix[i][j] === 0) return "white"; // free space
        if (matrix[i][j] === 1) return "black"; // wall
        if (matrix[i][j] === 2) return "green";   // solution path
        return "gray"; // fallback
    }

    printPath(movements) {
        const sequenceMoves = [];
        const visitedCells = [];
        const resultMatrix = this.cellMatrix.map(row => row.slice()); // Deep copy
        let currentPos = [...this.startPos];
        resultMatrix[currentPos[0]][currentPos[1]] = 2;
        visitedCells.push(currentPos);

        for (let i = 0; i < Math.floor(movements.length / 2); i++) {
            let [row, col] = currentPos;
            let moved = false;
            let newPos;

            if (movements[i * 2] === false) {
                // Vertical movement
                if (movements[i * 2 + 1] === false && row > 0 && resultMatrix[row - 1][col] !== 1) {
                    newPos = [row - 1, col];
                    sequenceMoves.push("Up");
                    moved = true;
                } else if (row < this.nRows - 1 && resultMatrix[row + 1][col] !== 1) {
                    newPos = [row + 1, col];
                    sequenceMoves.push("Down");
                    moved = true;
                }
            } else {
                // Horizontal movement
                if (movements[i * 2 + 1] === false && col < this.nCols - 1 && resultMatrix[row][col + 1] !== 1) {
                    newPos = [row, col + 1];
                    sequenceMoves.push("Right");
                    moved = true;
                } else if (col > 0 && resultMatrix[row][col - 1] !== 1) {
                    newPos = [row, col - 1];
                    sequenceMoves.push("Left");
                    moved = true;
                }
            }

            if (moved) {
                // Check for revisiting a cell
                if (visitedCells.some(([r, c]) => r === newPos[0] && c === newPos[1])) {
                    let index = visitedCells.findIndex(([r, c]) => r === newPos[0] && c === newPos[1]);
                    while (visitedCells.length > index) {
                        let last = visitedCells.pop();
                        resultMatrix[last[0]][last[1]] = 0;
                        sequenceMoves.pop();
                    }
                }

                currentPos = newPos;
                visitedCells.push(currentPos);
                resultMatrix[currentPos[0]][currentPos[1]] = 2;

                if (currentPos[0] === this.goalPos[0] && currentPos[1] === this.goalPos[1]) {
                    break;
                }
            } else {
                console.log("Movement out of bounds:", newPos);
                break;
            }
        }

        this.printMaze(resultMatrix);
        console.log(sequenceMoves);
    }


}