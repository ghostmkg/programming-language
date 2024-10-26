const color = [
  "Red",
  "Orange",
  "Yellow",
  "Green",
  "Blue",
  "Purple",
  "Pink",
  "Brown",
  "Gray",
  "White",
  "Crimson",
  "Lime",
  "Teal",
  "Indigo",
  "Magenta",
  "Gold",
  "Silver",
  "Cyan",
  "Maroon",
  "Olive",
  "Navy",
  "Fuchsia",
  "Turquoise",
  "Violet",
  "Coral",
  "Lavender",
  "Slate",
  "Orchid",
  "Chocolate"
];

const txt = document.getElementById("color-text")
const btn = document.getElementById("button")
                                        
function flipper(){
   var num = Math.floor(Math.random() * color.length)
   txt.textContent = color[num]
   document.body.style.backgroundColor = color[num] 
}
