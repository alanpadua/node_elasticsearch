import { Response, Request } from "express";
import { Client, types } from "pg";
import getClient from "./elasticsearch";


class ActorController {

    async create(request: Request, response: Response) {
        const client = new Client({
            host: 'localhost',
            port: 5432,
            database: 'dvdrental',
            password: 'mysecretpassword',
            user: 'postgres'
        });

        await client.connect();

        const { rows } = await client.query("SELECT * FROM ACTOR");

        for await (let row of rows) {
            getClient().index({
                index: 'actor',
                type: 'type_actor',
                body: row
            }, (erro) => {
                if (erro) {
                    return response.status(400).json({ error: erro })
                }
            });
        }

        // return response.status(200).json({ message: 'Index ok' })
        return response.status(200).json({ rows })
    }

    async findAll(request: Request, response: Response) {
        const data_inicial = new Date().getTime();
        const data = await getClient().search({
            index: 'actor',
            size: 6000
        });
        const data_final = new Date().getTime();

        console.log('[Elastic Search] O resultado foi...', (data_final - data_inicial));

        return response.json(data);
    }

    async findById(request: Request, response: Response) {

        const { id } = request.params;
        // console.log("ID: ")
        // console.log(id);

        const data = await getClient().search({
            index: 'actor',
            q: `actor_id:${id}`
        });

        return response.json(data.hits.hits);

    }

    async createActor(request: Request, response: Response) {
        const actor = {
            "actor_id": 99999,
            "first_name": "Teste",
            "last_name": "Last Test",
            "last_update": "2013-05-26T17:47:57.620Z"
        }

        const data = await getClient().index({
            index: 'actor',
            type: 'type_actor',
            body: actor
        });

        return response.json(data);
    }

    async findByQuery(request: Request, response: Response) {

        const data = await getClient().search({
            index: 'actor',
            body: {
                query: {
                    term: {
                        "first_name.keyword": 'Teste'
                        // "first_name": 'Teste'
                    }
                }
            },
        })

        return response.json(data);
    }

}

export default new ActorController;