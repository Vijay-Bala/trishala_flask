const areas = document.querySelectorAll("area");
const bagalkot = document.getElementById("bagalkot");
const ballari = document.getElementById("ballari");
const distrcitText = document.getElementById("distrcit-text");
const detail = document.getElementById("detail");

var year = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
var bagalotOptionsArray = [
  "KAMATAGI",
  "SULEBAVI",
  "MADAPUR",
  "AMINAGAD",
  "AIHOLE",
  "DAMMUR",
  "GUDUR",
  "UPANAL",
  "BASARIKATTI",
  "KYADIGERI",
  "MURUDI",
  "BASANAL",
  "RAMATHAL",
  "SIDDANAKOLLA",
  "KELUR",
  "KALLIGUDDA",
  "RAKKASAGI",
  "SULEBHAVI TWO",
  "BENAL",
  "AMBLIKOPPA",
  "BENAKANAWARI",
  "UPNAL",
  "ADAGAL",
  "YARAGOPPA",
  "TALAWAR GALLI",
  "ANAND NAGAR",
  "Teradal PS Limits",
  "SHIRUR",
  "ANDAMURANAL",
  "ARAVIND LIMBAVALI HOUSE",
  "HARANASHIKARI KALANI",
  "VENKATAPET",
  "Tallikari",
  "Aski Asangi Village",
  "TOLAMATTI",
  "ANAGAWADI",
  "AMARAVTI",
  "TIMMAPUR",
  "TUMB",
  "HANAMANAL",
  "TARIWAL",
  "HERUR",
  "HIREKODAGALI",
  "HARINAPUR",
  "SIDDAPUR",
  "TULASIGERI",
  "ANKALAGI",
  "SIMIKERI",
  "SULIKERI",
  "ANAVAL",
  "SUBHAS NAGAR LAKSHANATTI",
  "ARALIKATTI",
  "TOWN BEAT",
  "Uttur",
  "WADDAR GALLI",
  "APMC YARD",
  "Vidyagiri",
  "TUNGAL",
  "TUBACHI",
  "TAMADADDI VILLAGE",
  "HANAGANDI VILLAGE",
  "TERDAL",
];

var ballariOptionsArray = [
  "Andral",
  "Torangal Village",
  "Yelubenchi village",
  "Hagari Village",
  "BELLARY RURAL",
  "APMC PS Limits",
  "CB PS",
  "GNPS",
  "Brucepet PS limts",
  "BASARAKODU VILLEGE",
  "Tekkalkote",
  "ANDRAL",
  "HALADAHALLI",
  "HALDALLI",
  "ANANTPUR ROAD",
  "STATION ROAD AREA",
  "HARISCHANDRA GHAT AREA",
  "Siddharthanagar",
  "HATCHOLLI",
  "SUGGENAHALLI",
  "HAMPADEVANAHALLI",
  "THIMMALAPURA",
  "VENIVEERAPURA",
  "SOMASAMUDRA",
  "H.VEERAPURA",
  "SHIVAPURA",
  "HALE YERRAGUDI",
  "HAGRI",
  "K.VEERAPURA",
  "ASUNDI",
  "LINGADEVANAHALLI",
  "SUSHILANAGARA",
  "YASAVANTHNAGARA",
  "ULURU VILLAGE",
  "SIRIGERI VILLAGE",
  "SIRUGUPPA TOWN",
  "HERKAL",
  "TEKKALKOTE Town",
  "TORANAGALLU R.S",
  "TUMUTI VILLAGE",
  "VADDU VILLAGE",
  "VITALAPURA VILLAGE",
  "U.RAJAPURA VILLAGE",
];
// areas.forEach(area => {
//     area.addEventListener('mouseover', function(event) {
//         const tooltip = document.getElementById('tooltip');
//         tooltip.textContent = event.target.title;
//         tooltip.style.top = event.clientY + 'px';
//         tooltip.style.left = event.clientX + 'px';
//         tooltip.style.display = 'block';
//       console.log('hi')
//     });

//     area.addEventListener('mouseout', function() {
//         const tooltip = document.getElementById('tooltip');
//         tooltip.style.display = 'none';
//     });
// });
function setOptions(options) {
  var selectElement = document.getElementById("village");

  // Clear existing options
  selectElement.innerHTML = "";

  // Create and append new options
  options.forEach(function (optionText) {
    var option = document.createElement("option");
    option.text = optionText;
    option.value = optionText.toLowerCase().replace(/\s+/g, ""); // Use a value without spaces
    selectElement.appendChild(option);
  });
  submitButton.classList.remove("hide"); 
}

function setYearOptions(options) {
  var selectElement = document.getElementById("year");

  // Clear existing options
  selectElement.innerHTML = "";

  // Create and append new options
  options.forEach(function (optionText) {
    var option = document.createElement("option");
    option.text = optionText;
    option.value = optionText.toLowerCase().replace(/\s+/g, ""); // Use a value without spaces
    selectElement.appendChild(option);
  });
  submitButton.classList.remove("hide"); 
}

bagalkot.addEventListener("click", function () {
  detail.classList.remove("hide");
  detail.classList.add("details");
  distrcitText.innerText = "Bagalkot";
  setOptions(bagalotOptionsArray);
  setYearOptions(year);
});

ballari.addEventListener("click", function () {
  detail.classList.remove("hide");
  detail.classList.add("details");
  distrcitText.innerText = "Ballari";
  setOptions(ballariOptionsArray);
  setYearOptions(year);
});