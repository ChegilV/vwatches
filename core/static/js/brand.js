let brandSubMenu = document.getElementById('brandSubMenu');
let manSubMenu = document.getElementById('manSubMenu');
let womenSubMenu = document.getElementById('womenSubMenu');
let shopOnSaleM = document.getElementById('shop-on-saleM');
let shopByColorM = document.getElementById('shop-by-colorM');
let shopOnSaleW = document.getElementById('shop-on-saleW');
let shopByColorW = document.getElementById('shop-by-colorW');
let newProd = document.getElementById('newProd');

let rotateBrands = document.getElementById('rotate-brands');
let rotateMan = document.getElementById('rotate-man');
let rotateWomen = document.getElementById('rotate-women');
let rotateNew = document.getElementById('rotate-new');

function toggleBrandUnderMenu() {

    brandSubMenu.classList.toggle('open-under');
    rotateBrands.classList.toggle("rotate");

}

function toggleManUnderMenu(){
     manSubMenu.classList.toggle('open-under');
     rotateMan.classList.toggle("rotate");
}

function manShopSale() {
    shopOnSaleM.classList.toggle('open-under');

}


function manShopColor() {
    shopByColorM.classList.toggle('open-under');
}


function toggleWomenUnderMenu() {
    womenSubMenu.classList.toggle('open-under');
     rotateWomen.classList.toggle("rotate");

}

function womenShopSale() {
    shopOnSaleW.classList.toggle('open-under');

}

function womenShopColor() {
    shopByColorW.classList.toggle('open-under');
}


function toggleNewUnderMenu() {
    newProd.classList.toggle('open-under');
     rotateNew.classList.toggle("rotate");
}



