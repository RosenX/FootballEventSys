$(document).ready(function(){
    $(".score-record-btn").click(function(){
        match_id = $(this).attr("iid");
        Dajaxice.result.getMatch(getMatch_callback,{"matchId":match_id});
    });
});

$(document).on("click",".score-add-btn",function(){
    match_id = $(this).attr("mid");
    $("#id_match").val(match_id);
    $("#score-add-form").removeClass("hidden");
});

$(document).on("click",".score-save",function(){
    $("#score-add-form").addClass("hidden");
    form = $("#score-add-form").serialize(true);
    alert(form);
    match_id =$(".score-record-btn").attr("iid");
    Dajaxice.result.addScore(addScore_callback,{'form':form,'matchId':match_id});
});

function addScore_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".match-record-table").html(data["html"]);
    }
}

function getMatch_callback(data){
    $(".match-record-table").html(data["html"]);
}
