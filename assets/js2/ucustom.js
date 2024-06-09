
function logoutfunc()
{
    $.ajax({
        url: $("#logout_btn").attr("data-url"),
        type: 'POST',
        data:{
            'csrfmiddlewaretoken':jQuery('meta[name="csrf-token"]').attr('content')

            },
            success: function(response) {
                toastr.success("Logged Out!");
                
            },
            error: function(){
                toastr.error('Error Logging Out User!');
            }
    });
}

