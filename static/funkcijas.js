async function suutiitZinju(){
    let vieta = document.getElementById("chats");
    let zinja = document.getElementById("teksts").value;
    vieta.innerHTML = zinja;
    const atbilde = await fetch('/jschats/suutiit',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"saturs": zinja})
    }
    )
    vieta.innerHTML = await atbilde.json();
}