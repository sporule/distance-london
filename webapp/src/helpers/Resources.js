let instance = null;

export default class Resources{
    constructor() {
        if(!instance){  
            this.url = "https://distance-london.herokuapp.com/cameras";
            instance =this;
        }
        return instance;
      }
    
    getCameras(){
        return fetch(this.url).then(r=>r.json()).then(data=>{
            return data['body']
        })
    }
}