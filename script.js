const songURL =
"https://href-yields-clinton-blades.trycloudflare.com/nowplaying.txt";


async function updateSong(){

    const songBox = document.getElementById("song");

    try {

        const response = await fetch(
            songURL + "?time=" + Date.now()
        );

        const song = await response.text();

        let parts = song.trim().split(" - ");

        if(parts.length >= 2){

            songBox.innerHTML =
            `
            <b>${parts[1]}</b><br>
            ${parts[0]}
            `;

        } else {

            songBox.innerHTML = song;

        }


    } catch(error){

        songBox.innerHTML =
        "WHBR Roanoke LIVE";

        console.log(error);

    }

}


updateSong();

setInterval(updateSong,10000);