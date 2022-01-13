import axios from "axios";

export default class Api {
    constructor () {
        this.endpoint = "http://10.1.34.239:8000/call";
        this.client = axios;
    }

    //Get test:
    post(payload) {
        return this.client.post(this.endpoint, payload)
    }

}
