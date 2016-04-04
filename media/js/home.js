$(".ing-event-select").change(function(){
    event_id = $(this).val();
    if(parseInt(event_id)>0){
        Dajaxice.home.getRank(getRank_callback, {"event_id": event_id});
    }
});

function getRank_callback(data){
    $('.score-rank-content').html(data['sumscore_rank_html']);
    $('.round-score-content').html(data['rounds_matchs_html']);
}
