{
    'name' : 'student',
    'version' : '1.0',
    'summary' : 'student details',
    'category' : 'information',
    'depends':['sale'],
    'data' : [
        'views/student_views.xml',
        'views/calculate_views.xml',
        'views/wizard_views.xml',
        'views/teacher_view.xml',
        'views/sale_view.xml',
        'report/report_action.xml',
        'report/report_quotation.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}