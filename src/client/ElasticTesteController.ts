import getClient from "./elasticsearch";
import { Request, Response } from "express";

class ElasticTesteController {

    async create(request: Request, response: Response) {

        const client = getClient();

        // Criar um registro no Elasticsearch
        const result = await client.index({
            index: 'elastic_teste',
            type: 'type_elastic_teste',
            body: {
                user: 'Daniele',
                password: 'sd823udf',
                email: 'dani.leao89@gmail.com'
            }
        }).catch(e => { console.log(e) });

        return response.json(result);
    }

}

export default new ElasticTesteController;