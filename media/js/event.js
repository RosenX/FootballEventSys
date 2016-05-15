$(document).ready(function(){
    $("#event-save").click(function(){
        form = $("#event-add-form").serialize(true);
        Dajaxice.event.addEvent(addEvent_callback,{'form':form});
    });
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
    });
    $(".new-round").click(function(){
        event_id = $(this).attr("iid");
        Dajaxice.event.addNewRound(addNewRound_callback,{'event_id':event_id});
    });
    $(".new-match").click(function(){
        round_id = $(this).attr("iid");
        $("#id_round_belong").val(round_id);
    });
    $("#match-save").click(function(){
        form = $("#match-add-form").serialize(true);
        event_id = $(".new-round").attr("iid");
        Dajaxice.event.addNewMatch(addNewMatch_callback,{'form':form,"event_id":event_id});
    });

});


$(document).on("click",".check-cards-btn",function(){
    match_id = $(this).attr("iid");
    Dajaxice.result.getCards(getCards_callback,{'matchId':match_id});
});

function getCards_callback(data){
    $(".cards-record-table").html(data["html"]);
}

function addNewMatch_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".event-schedule-table").html(data["html"]);
    }
    location.reload()
}

function addNewRound_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".event-schedule-table").html(data["html"]);
    }
    location.reload()
}

function addEvent_callback(data){
    if(data["statu"]==0){
        alert("something wrong");
    }
    else{
        $(".event-table").html(data["html"]);
    }
}
