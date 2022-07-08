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

function findNumbers({request: {vector, end, start}}, callback){

    const localVector = vector.slice(start, end);
    const first = vector[0];

    const max = localVector.reduce((acc, cur) => 
        acc > cur? acc : cur
    );

    const min = localVector.reduce((acc, cur) => acc < cur? acc : cur, first);

    callback(null, {
        min: min,
        max: max    
    })
}

const server = new grpc.Server();

server.addService(CalculaDefinitions.CalculaService.service, {findNumbers: findNumbers});

server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
})

console.log('Listening')