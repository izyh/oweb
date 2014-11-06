$(function () {
	table_parse();
	img_parse();
	link_parse();
})

function table_parse () {
	$(".doc-content table").each(function () {
		$(this).addClass("table table-hover table-striped");
	});
}

function img_parse () {
	$(".doc-content img").each(function () {
		$(this).addClass("img-responsive");
	});
}

function link_parse () {
	$(".doc-content a").each(function () {
		if($(this).is("[target=_blank]")){
			$(this).append(' <span class="glyphicon glyphicon-new-window"></span>');
		}
		
	});
}