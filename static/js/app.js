
// Look at
// http://stackoverflow.com/questions/9446318/bootstrap-tooltips-not-working

// active
$( function () {
	$("[data-toggle='tooltip']").tooltip();
	popover_start();
});

function popover_start () {
	// 
	$("[doc-pop], [doc-pop-target]").attr("data-toggle","popover");
	// 
	$("[doc-pop]").each(function(){
		$(this).attr("data-content",$(this).attr("doc-pop"));
	});
	$("[doc-pop-target]").each(function(){
		selector = $(this).attr("doc-pop-target");
		html     = $(selector).html();
		$(this).attr("data-content",html);
	})
	// 
	$("[data-toggle='popover']").popover({
		html      : true,
		placement : "top",
		trigger   : "hover",
	});
}

function dropdown_start () {
	$('.dropdown-toggle').dropdown();
}