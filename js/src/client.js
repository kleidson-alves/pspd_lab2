const grpc = require('@grpc/grpc-js') ;
const { loadSync } = require('@grpc/proto-loader');
const path = require('path'); 

const protoObject = loadSync(path.resolve(__dirname, "../../protos/calcula.proto"), 
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
   });

const CalculaDefinitions = grpc.loadPackageDefinition(protoObject).calcula;

const client = new CalculaDefinitions.CalculaService('localhost:50051', grpc.credentials.createInsecure())

function generateArray(){
    const array = [];

    for(let i =0; i< 500000; i++){      
        array.push((Math.floor(Math.random() * 500000)));
    }

    return array;
}

function main() {
    const array = generateArray();

    client.FindNumbers({vector: array, start: 1, end: array.length}, (err, response) => {
        console.log(response);
    } )
}

main();