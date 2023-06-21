function getData(data) {
    return new Promise(function(resolve,reject){
        if (typeof(data)!="number"){
            reject("error")
        }
        else if (data%2){
            setTimeout(function(){
                resolve("odd")
            },2000)
        }
        else{
            setTimeout(function(){
                resolve("even")
            },4000)
        }
    })
}
export default getData
