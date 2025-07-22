import { Bot } from './bot.js';
import { Maze } from './maze.js';

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function crossOver(A, B, x){
    const newA = [...A.slice(0, x), ...B.slice(x)];
    const newB = [...B.slice(0, x), ...A.slice(x)];
    return [newA, newB];
}

function mutation(movement, mutationRate){
    mutationRate = mutationRate / 100;
    for(let i=0; i<movement.length; i++){
        if(Math.random()<mutationRate){
            movement[i] = !movement[i]              // if boolean
        }
    }

    return movement;
}

function defineMovementLength(){
    return;
}


export async function runGeneticAlgorithm(nBots, nMovements, maxGenerations, mutationRate, nRows, nCols, mazeMatrix, startCell, endCell){
    let bots = [];
    let results = [];

    const startPos = [parseInt(startCell.dataset.row), parseInt(startCell.dataset.col)];
    const endPos = [parseInt(endCell.dataset.row), parseInt(endCell.dataset.col)];

    const maze = new Maze(nRows, nCols, mazeMatrix, startPos, endPos);

    for(let i=0; i<nBots; i++){
        let movements = Array.from({length: nMovements * 2}, () => Math.random() < 0.5);
        let bot = new Bot(movements);

        bots.push(bot);
    }

    let generation = 0;
    let solutionFound = false;

    while(generation < maxGenerations){

        for(let bot of bots){
            let [movements, performance] = bot.runMaze(maze, nMovements);
            results.push([movements, performance]);
        }
        console.log(results)
        results.sort((a, b) => a[1] - b[1]);
        console.log("sorting")
        console.log(results)

        console.log(`Generation ${generation + 1} - Best Result: ${results[0][1]}`);

        if(results[0][1]===0){
            //solution found
            solutionFound = true;
            //maze.printPath(results[0][0]);
            console.log("Solution found:" + results[0][0])
            break;
        }

        bots = []
        for(let i=0; i<Math.floor(nBots/2); i++){
            const [childMov1, childMov2] = crossOver(results[i][0], results[i+1][0], nMovements);

            const childBot1 = new Bot(mutation(childMov1, mutationRate));
            const childBot2 = new Bot(mutation(childMov2, mutationRate));

            bots.push(childBot1);
            bots.push(childBot2);
        }

        results = [];
        generation++;
        

        if (generation % 10 === 0) {
            await sleep(10); // pausa só a cada 10 gerações
        }
    }

    if (!solutionFound) {
        console.log("Solution not found");
    }

    


}