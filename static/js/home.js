/**
    Get Cookie (https://docs.djangoproject.com/en/3.2/ref/csrf/)
    @param {name} Name of the cookie example:- getCookie('csrftoken')
*/
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

/**
    Function for opening cards
    @param {string} evt - Event name
    @param {string} cardName - Identifier for the card
*/
function openCard(evt, cardName) {
  var i, cardContent, card;
  cardContent = document.getElementsByClassName("cardContent");
  for (i = 0; i < cardContent.length; i++) {
    cardContent[i].style.display = "none";
  }
  card = document.getElementsByClassName("card");
  for (i = 0; i < card.length; i++) {
    card[i].className = card[i].className.replace(" visible", "");
  }
  document.getElementById(cardName).style.display = "block";
  evt.currentTarget.className += " visible";
}

function SendData(endpoint) {
  const Http = new XMLHttpRequest();
  const url = endpoint;
  Http.open("POST", url);
  Http.setRequestHeader("X-CSRFToken", csrftoken);
  Http.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
  };
}

let searchBar = document.querySelector(".search");
searchBar.addEventListener("submit", (e) => {
  e.preventDefault();
  if (searchBar.classList.contains("animateup")) {
      SendData("http://127.0.0.1:8000/user/crawler")
  } else {
    searchBar.classList.add("animateup");
    document.querySelector("section.results").classList.remove("d-none");
    SendData("http://127.0.0.1:8000/user/crawler");
  }
});

const csrftoken = getCookie("csrftoken");
