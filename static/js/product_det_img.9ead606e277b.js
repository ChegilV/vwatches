let main_photo = document.getElementById("main-img")
let smallImage = document.getElementsByClassName("image")
smallImage[0].onclick = ()=>{
    main_photo.src = smallImage[0].src
}
smallImage[1].onclick = ()=>{
    main_photo.src = smallImage[1].src
}

smallImage[2].onclick = ()=>{
    main_photo.src = smallImage[2].src
}

//smallImage[0].onclick = ()=>{
//    main_photo.src = smallImage[2].src
//}