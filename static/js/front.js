let name="ryo";
var btn = document.getElementById('text_btn');

// btn.addEventListener('click', (function(event){
//     btn.style.color = "red"; }
//     )
// );



// jQuery
$(function(){
    $("#text_btn").css("color","red");
    $("#text_btn").click(function(){
        $("#text_btn").css("color", "blue");
        $("#text_btn").children("h1").css("font-size","50px");
    });

    $("#text_btn").hover(
        function(){
            $("#text_btn").children("h2").html('<span class="bg=red">text</span>');
        },
        function(){
            $("#text_btn").children("h2").html("");
        }        
    )
});