document.addEventListener("click", (e) => {
    if (e.target.tagName == "P" || e.target.tagName == "DIV" || e.target.tagName == "BUTTON"){
        console.log(e.target.firstChild)
    }
})