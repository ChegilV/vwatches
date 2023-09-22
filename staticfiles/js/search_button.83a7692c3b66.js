const trigger_search = document.querySelector('.trigger_search_btn');
const input = document.querySelector(".show-container");
const btn_search = document.querySelector("#trigger_search");
let div = document.getElementById("search-item");
let display = 0;

trigger_search.addEventListener("click", () =>{
    if(!input.classList.contains("input-open")){
        input.classList.add('input-open');
//        btn_search.style.display = "block";
         trigger_search.innerHTML = '<i class="fa-sharp fa-regular fa-circle-xmark fa-2xl"></i>';

    }
    else{
        input.classList.remove("input-open");

        trigger_search.innerHTML = "<i class='fas fa-search fa-2xl'></i>";
    }
})