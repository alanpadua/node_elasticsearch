import express, { Request, Response } from "express";
import ActorController from "./client/ActorController";
import DBController from "./client/DBController";
import ElasticTesteController from "./client/ElasticTesteController";


const app = express();
app.get('/', (request: Request, response: Response) => response.json({"mensagem": 'Hello world'}));
app.get('/registro-teste', ElasticTesteController.create);
app.get('/db/create', DBController.create);
app.get('/db/findAllActor', DBController.findAllActor);
app.get('/actor/create', ActorController.create);
app.get('/actor/findAll', ActorController.findAll);
app.get('/actor/findById/:id', ActorController.findById);
app.get('/actor/createActor', ActorController.createActor)
app.get('/actor/findByQuery', ActorController.findByQuery)

app.listen(3333, () => console.log('Running...'));