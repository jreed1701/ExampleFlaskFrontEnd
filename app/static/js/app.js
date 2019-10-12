$(document).ready(function() {
    $('ul').on('click li', function(event) {
        var $target = $(event.target).is('li') ? $(event.target) : $(event.target).closest('li')
        itemId = $target.data('id');
        handleButton(itemId)
    });
});


function handleButton(id){
    alert("Item id is: " + itemId);    
}