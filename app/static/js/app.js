$(document).ready(
function() {
    $('ul').on('click li', function(event) {
        var $target = $(event.target).is('li') ? $(event.target) : $(event.target).closest('li')
        itemId = $target.data('id');
        handleButton(itemId)
    });
});


function handleButton(id){
    
    /*alert("Item id is: " + itemId);  */  
    
    var url = '';
    
    switch(id) {
    
        case 'page-1-btn':
            url = '/page1';            
            break;
        case 'page-2-btn':
            url = '/page2';
            break;
        default:
            url = '/';
            break;
    }
    
    load(url)
}

function load (url) {
    fetch(url)
    .then((response) => response.text())
    .then((html) => {
        document.getElementById("displayArea").innerHTML = html;
    })
    .catch((error) => {
        console.warn(error);
    });
} 