$(function () {
	table_parse();
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