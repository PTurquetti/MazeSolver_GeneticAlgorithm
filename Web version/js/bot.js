export class Bot{
    constructor(movements){
        this.movements = movements;
        this.currentPos = [];
        this.reachedGoal = false;
    }

    calculatePerformance(goal){ //manhattan distance
        return Math.abs(goal[0] - this.currentPos[0]) + Math.abs(goal[1] - this.currentPos[1]);
    }

    move(maze, direction) {
        let row = this.currentPos[0];
        let col = this.currentPos[1];

        if (direction === "up") {
            if (row > 0 && maze.cellMatrix[row - 1][col] === 0) {
                this.currentPos = [row - 1, col];
            }
        } else if (direction === "down") {
            if (row < maze.nRows - 1 && maze.cellMatrix[row + 1][col] === 0) {
                this.currentPos = [row + 1, col];
            }
        } else if (direction === "left") {
            if (col > 0 && maze.cellMatrix[row][col - 1] === 0) {
                this.currentPos = [row, col - 1];
            }
        } else if (direction === "right") {
            if (col < maze.nCols - 1 && maze.cellMatrix[row][col + 1] === 0) {
                this.currentPos = [row, col + 1];
            }
        } else {
            console.log("Unknown movement direction");
        }

        if (this.currentPos[0] === maze.goalPos[0] && this.currentPos[1] === maze.goalPos[1]) {
            this.reachedGoal = true;
        }
    }

    runMaze(maze, nMovements){
        this.currentPos = [...maze.startPos]; 
        let currentMove = 0;

        while (!this.reachedGoal && currentMove <= nMovements) {
            if (this.movements[currentMove * 2] === false) {
                // vertical movement
                if (this.movements[currentMove * 2 + 1] === false) {
                    this.move(maze, "up");
                } else {
                    this.move(maze, "down");
                }
            } else {
                // horizontal movement
                if (this.movements[currentMove * 2 + 1] === false) {
                    this.move(maze, "right");
                } else {
                    this.move(maze, "left");
                }
            }
            currentMove++;
        }

        // Analyze performance
        const performance = this.calculatePerformance(maze.endPos);

        return [this.movements, performance];
    }
}