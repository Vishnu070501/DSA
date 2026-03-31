const perm = (arr)=>{
    if (arr.length==1){
        return [arr]
    }
    const roap = perm(arr.slice(1, arr.length))
    let result = []
    for (let ele of roap){
        for (let i=0; i<=ele.length; i++){
            ele.splice(i, 0, arr[0])
            result.push([...ele])
            ele.splice(i,1)
        }
        // result.push([...ele,arr[0]])
    }
    return result
}

console.log(perm([1,2,3]))