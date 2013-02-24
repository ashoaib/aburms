var contact = {
	defaults: {},
	
	init: function() {
		var name = $('#name');
		var email = $('#email');
		var message = $('#message');
		
		contact.defaults['name'] = name.val();
		contact.defaults['email'] = email.val();
		contact.defaults['message'] = message.val();
		
		name.on('focus', contact.onFocus).on('blur', contact.onBlur);
		email.on('focus', contact.onFocus).on('blur', contact.onBlur);
		message.on('focus', contact.onFocus).on('blur', contact.onBlur);		
	},
	
	onFocus: function() {
		var t = $(this);
		
		if (t.val() == contact.defaults[t.attr('id')]) {
			t.val('');
		}
	},
	
	onBlur: function() {
		var t = $(this);
		
		if (t.val() == '') {
			t.val(contact.defaults[t.attr('id')]);
		}
	}
};

$(function() {
	contact.init();
});
