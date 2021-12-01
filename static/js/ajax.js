$('a').on('click',"li.ajax", function(event){
    console.log("REDIRECT");
    event.preventDefault();
    event.stopPropagation();
    var targetAttr = $(this).attr('target');
    var linkHref = $(this).attr('href');
    
    setTimeout(function(event){
      if ( targetAttr === undefined ){
        alert('redirect in same window');
        console.log("REDIRECT");
        window.location.href = linkHref;
    }
    })
})   

