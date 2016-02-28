$(document).ready(function(){
    $(".score-record-btn").click(function(){
        match_id = $(this).attr("iid");
        Dajaxice.result.getMatch(getMatch_callback,{"matchId":match_id});
    });
});

$(document).on("click",".score-add-btn",function(){
    match_id = $(this).attr("mid");
    team_id = $(this).attr("iid");
    $("#id_match").val(match_id);
    $("#score-add-form").removeClass("hidden");
    $("#score-save").attr("iid",team_id);
});

$(document).on("click",".score-save",function(){
    $("#score-add-form").addClass("hidden");
    form = $("#score-add-form").serialize(true);
    match_id =$(".score-record-btn").attr("iid");
    which_team = $(this).attr("iid");
    Dajaxice.result.addScore(addScore_callback,{'form':form,'matchId':match_id,"which_team":which_team});
});

$(document).on("click",".score-modal-close",function(){
    location.reload();
});

score-modal-close

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
