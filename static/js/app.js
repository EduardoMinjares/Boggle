let submitBtn = document.getElementById("submit-Btn")
let input = document.getElementById("word")
score = 0

submitBtn.addEventListener("click", async function(e){
    e.preventDefault()

    let wordResponse = await axios.post("/process",{data:{word:input.value}})
    const result = wordResponse.data.result

    if(result == 'ok'){
        score += input.value.length
    }
})

setTimeout(async function(){
    submitBtn.setAttribute('disabled','disabled')
    let scoreResponse = await axios.post("/score",{data:{score:score}})
    console.log(scoreResponse)
}, 5000)