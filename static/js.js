const socket = io();
console.log("I am js")



socket.on("connect", ()=>{
    console.log("I am connected")
})

socket.on("message", (message) => {
    document.getElementById("infinite").innerText = message
    // console.log(message)
})

window.onload = ()=>{
    socket.emit("message", 10)
};

document.addEventListener("DOMContentLoaded", function(){

const btn = document.getElementById("btn");
btn.addEventListener("click", function(){
var input = document.getElementById("input").value;
socket.emit("inputtext", input)
})
});

socket.on("inputtext", (input) => {
    var tagg = document.createElement("li");
    const node = document.createTextNode(input);
    tagg.appendChild(node)

    document.getElementById("text-entered").appendChild(tagg)
    console.log(input);

});