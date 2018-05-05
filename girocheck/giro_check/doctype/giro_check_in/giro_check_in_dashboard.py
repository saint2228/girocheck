from frappe import _

def get_data():
	return {
		'fieldname': 'giro_check_in',
		'non_standard_fieldnames': {
			'Payment Entry': 'reference_no',

		},

		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Payment Entry']
			},

		]
	}
