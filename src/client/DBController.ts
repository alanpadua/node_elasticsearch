import { Request, Response } from "express";
import { Client } from "pg";


class DBController {
    async create(request: Request, response: Response) {

        const data_inicial = new Date().getTime();
        const client = new Client({
            host: 'localhost',
            port: 5432,
            database: 'dvdrental',
            password: 'mysecretpassword',
            user: 'postgres'
        });

        await client.connect();
        const { rows } = await client.query("SELECT * FROM ACTOR");
        const data_final = new Date().getTime();
        console.log('[Banco] O resultado foi...', (data_final - data_inicial));

        return response.json(rows);
    }

    async findAllActor(request: Request, response: Response) {

        const data_inicial = new Date().getTime();
        const client = new Client({
            host: 'localhost',
            port: 5432,
            database: 'dvdrental',
            password: 'mysecretpassword',
            user: 'postgres'
        });

        await client.connect();

        const { rows } = await client.query("SELECT * FROM ACTOR");

        const data_final = new Date().getTime();

        console.log('[Banco] O resultado foi...', (data_final - data_inicial));

        return response.json(rows);
    }
}

export default new DBController;