$(document).ready(function(){
    $("#team-save").click(function(){
        form = $("#team-add-form").serialize(true);
        Dajaxice.team.addTeam(addTeam_callback,{'form':form})
    });
    $("#player-save").click(function(){
        form = $("#player-add-form").serialize(true);
        team_id = $(".player-add-btn").attr("iid");
        Dajaxice.team.addPlayer(addPlayer_callback,{'form':form,"teamId":team_id});
    });
    $(".player-add-btn").click(function(){
        team_id = $(this).attr("iid");
        $(".team").val(team_id);
    });
    $(".member-add-btn").click(function(){
        team_id = $(this).attr("iid");
        $(".team").val(team_id);
    });
    $("#member-save").click(function(){
        form = $("#member-add-form").serialize(true);
        team_id = $(".member-add-btn").attr("iid");
        Dajaxice.team.addMember(addMember_callback,{'form':form,'teamId':team_id});
    });
});

function addMember_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".member-list-table").html(data["html"]);
    }
}

function addTeam_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".team-table").html(data["html"]);
    }
}

function addPlayer_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".player-list-table").html(data["html"]);
    }
}