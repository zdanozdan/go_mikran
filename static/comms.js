(function($) {
    $.comms = function(data, klass) 
    {
    }
    
    /*
     * Public, $.facebox methods
     */
    
    $.extend($.comms, {
	settings: {
	    opacity      : 0,
	    overlay      : true,
	    redirect     : '',
	    loadingImage : '/static/loading.gif',
	    smallCloseImage   : '/images/close.png',
	    sent         : 0,
	    commsHtml    : '\
   <div id="comms" style="display:none;"> \
      <div class="close_top" title="Close"></div> \
        <table> \
          <tr> \
            <td class="body"> \
            <div class="comms_content"></div> \
          </tr> \
          </tbody> \
        </table> \
    </div>'
	},
	loading: function(clicked) {
	    progress = $(clicked).find('#progress')
	    progress.prepend('<div class="loading"><img src="'+$.comms.settings.loadingImage+'"/></div>')
	},
	reveal: function(element, data) {
	    element.replaceWith(data);
	},
	submit: function(form) {
	    $.comms.loading(form)

	    $.ajax({
		url: form.action,
		type: 'post',
		dataType: 'html',
		data: $(form).serialize(),

		success: function(response){
		    $('#cart_object').replaceWith(response);
		    $(document).trigger('rebind.comms');
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {
		    $('#cart_object').replaceWith(XMLHttpRequest.responseText);
		    $(document).trigger('rebind.comms');
		}
	    });
	}
    }),

    $.fn.formsubmit = function(index,element) {
	//init(settings)

	function submitHandler(event) {	
	    clicked = $(element);

	    $.comms.submit(this)
	    $(document).trigger('rebind.comms');
	    return false
	}

	return $(element).unbind('submit').bind('submit',submitHandler)
    }
    
    /*
     * Public, $.fn methods
     */
    $.fn.get = function(settings) {
	//init(settings)
	
	function clickHandler(event) {	
	    clicked = $(this);
	    inline = $('#'+this.rev)
	    
	    $.comms.loading(clicked)
	    $.ajax({
		url: this.href,
		type: 'get',
		dataType: 'html',
		success: function(response){
		    inline.replaceWith(response);
		    $(document).trigger('rebind.comms');
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {
		    inline.replaceWith(XMLHttpRequest.responseText);
		    $(document).trigger('rebind.comms');
		}
	    });
	    
	    $(document).trigger('rebind.comms');
	    return false
	}	

	return this.unbind('click').click(clickHandler)
    }
})(jQuery);

$(document).ready(function() {
    
    $(document).bind('rebind.comms', function() {
	$('[rel*=get]').get();
	
	$('[id*=inline_submit]').each(function(index,element) {
	    $.fn.formsubmit(index,element);
	})
	
	$('#inline_submit input[type=checkbox]').click( function() {
	    $.comms.submit(this.form)
	})

	$('#collapse').click(function() {
	    $('thead tr#collapse').hide()
	    $('tbody#collapse').hide()
	})
    })

    $(document).trigger('rebind.comms');
});