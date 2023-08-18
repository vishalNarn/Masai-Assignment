function add(){
    a=parseInt(document.getElementById('1st').value)
    b=parseInt(document.getElementById('2nd').value)
    let c=a+b
    alert(c)
    // document.getElementById("res").innerText=c
}

function sub(){
    a=parseInt(document.getElementById('1st').value)
    b=parseInt(document.getElementById('2nd').value)
    let c=a-b
    alert(c)
}

function mul(){
    a=parseInt(document.getElementById('1st').value)
    b=parseInt(document.getElementById('2nd').value)
    let c=a*b
    alert(c)
}

function div(){
    a=parseInt(document.getElementById('1st').value)
    b=parseInt(document.getElementById('2nd').value)
    let c=a/b
    alert(c)
}