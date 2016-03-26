$(document).ready(function(){
    $(".score-record-btn").click(function(){
        match_id = $(this).attr("iid");
        Dajaxice.result.getMatch(getMatch_callback,{"matchId":match_id});
    });

});

$(document).on("click",".card-record-btn",function(){
    match_id = $(this).attr("iid");
    Dajaxice.result.getCards(getCards_callback,{'matchId':match_id});
});

function getCards_callback(data){
    $(".cards-record-table").html(data["html"]);
}

$(document).on("click",".score-add-btn",function(){
    match_id = $(this).attr("mid");
    team_id = $(this).attr("iid");
    $("#id_match").val(match_id);
    $("#score-add-form").removeClass("hidden");
    $("#score-save").attr("iid",team_id);
});

$(document).on("click",".red-add-btn",function(){
    match_id = $(this).attr("mid");
    $("#red-add-form #id_match").val(match_id);
    $("#red-add-form").removeClass("hidden");
});

$(document).on("click",".yellow-add-btn",function(){
    match_id = $(this).attr("mid");
    $("#yellow-add-form #id_match").val(match_id);
    $("#yellow-add-form").removeClass("hidden");
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

function addScore_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".score-record-table").html(data["html"]);
    }
}

function getMatch_callback(data){
    $(".score-record-table").html(data["html"]);
}

$(document).on("click","#red-add-save",function(){
    $("#red-add-form").addClass("hidden");
    form = $("#red-add-form").serialize(true);
    Dajaxice.result.addRedCard(addRedCard_callback,{'form':form});
});

function addRedCard_callback(data){
    if(data["statu"] == 0)alert("something wrong");
    else{
        $(".cards-record-table").html(data["html"]);
    }
}

$(document).on("click","#yellow-add-save",function(){
    $("#yellow-add-form").addClass("hidden");
    form = $("#yellow-add-form").serialize(true);
    Dajaxice.result.addYellowCard(addYellowCard_callback,{'form':form});
});

function addYellowCard_callback(data){
    if(data["statu"] == 0)alert("something wrong");
    else{
        $(".cards-record-table").html(data["html"]);
    }
}
