from odoo import api, fields, models

class first(models.Model):
    _name = "fy.details"
    _description = "student information"

    roll_no_id=fields.Many2one('r.no', string="Roll no",require=True,store=True)
    name=fields.Char(string="Name",require=True,translate=True,related='roll_no_id.name',store=True)
    img=fields.Binary("image",attachment=True,store=True)
    address=fields.Char(string="Address",require=True,translate=True,related='roll_no_id.address',store=True)
    email_id=fields.Char(string="Email_id",require=True,translate=True,related='roll_no_id.email_id',store=True)
    mobile_no=fields.Char(string="Mobile no",size=10,require=True,translate=True,related='roll_no_id.mobile_no',store=True)
    state=fields.Char(string="State",translate=True,related='roll_no_id.state',store=True)
    active_fy = fields.Boolean('Active')
    marks=fields.Float(string="Marks",size=2,require=True,translate=True,related='roll_no_id.marks',store=True)
    max=fields.Float(string="max",default=100,store=True)
    date_today=fields.Datetime(string="start_date",default=fields.Datetime.now,
    index=True, copy=False)
    color = fields.Integer(string='Color Index')
    date_action = fields.Date('Next Activity Date', index=True)
    div=fields.Selection([('a','A'),('b','B'),('c','C')])
    #aref = fields.Reference([('model_name', 'String'),('model_no','5'),('model_price','19000')])
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher Name')
    sequence=fields.Integer("Sequence" , default=1)

    #
    # @api.onchange('roll_no_id')
    # def roll_onchange(self):
    #     print "********ONCHANGE CALLED****************", self.roll_no_id.name
    #     self.name = self.roll_no_id.name
    #     self.address=self.roll_no_id.address
    #     self.email_id = self.roll_no_id.email_id
    #     self.mobile_no = self.roll_no_id.mobile_no
    #     self.state = self.roll_no_id.state
    #     self.marks = self.roll_no_id.marks

    @api.constrains('roll_no_id')
    def check_rollno(self):
        # print "*******self.roll_no_id*******",self.roll_no_id.id, self.roll_no_id.rno, self.roll_no_id.name, self.roll_no_id.address
        rollno_rec = self.env['sy.details'].search([('roll_no_ids', '=', self.roll_no_id.id)])
        # print "********sy rno****", rollno_rec.roll_no_ids.rno
        # print "********fy rno****", self.roll_no_id.rno
        if rollno_rec.roll_no_ids.rno == self.roll_no_id.rno:
            if self.roll_no_id.rno == self.roll_no_id.rno:
                raise ValueError("please write different roll_no. Roll Number is already Used.")

    @api.constrains('mobile_no')
    def mobile_no_checked(self):
        mobile=self.search([('mobile_no','=',self.mobile_no)])
        print "self===============1mobile-------------",self.mobile_no,mobile
        if len(mobile) > 1 :
            raise ValueError("Mobile Number is already exist.")



class second(models.Model):
    _name = "sy.details"
    _description = "student information"

    roll_no_ids=fields.Many2one('r.no',string="Roll no",size=4)
    name=fields.Char(string="Name",require=True,translate=True)
    address=fields.Char(string="Address",equire=True,translate=True)
    email_id=fields.Char(string="Email_id",require=True,translate=True)
    mobile_no=fields.Char(string="Mobile no",size=10,require=True,translate=True)
    state=fields.Char(string="State",require=True,translate=True)
    active_sy = fields.Boolean('Active')
    date_action = fields.Date('Next Activity Date', index=True)
    marks = fields.Float(string="Marks", size=2, require=True, translate=True)

    teacher_id=fields.Many2one('teacher.teacher', string='Teacher Name')


    @api.onchange('roll_no_ids')
    def roll_Change(self):
        # print "********ONCHANGE CALLED****************", self.roll_no_ids.name
        self.name=self.roll_no_ids.name
        self.address = self.roll_no_ids.address
        self.email_id = self.roll_no_ids.email_id
        self.mobile_no = self.roll_no_ids.mobile_no
        self.state = self.roll_no_ids.state
        self.marks = self.roll_no_ids.marks

    @api.constrains('email_id')
    def check_email(self):
        email = self.search([('email_id','=',self.email_id)])
        # print "----------------sy rec-------", email
        # print "len-----------", len(email)
        if len(email) > 1:
            raise ValueError("Email is already exist.")


class Teacher(models.Model):

    _name = 'teacher.teacher'

    name = fields.Char('Teacher name')
    student_ids=fields.One2many('fy.details','teacher_id',string="Student Id")
    arel_ids = fields.Many2many('fy.details','fy_det_teacher_rel','fy_id','teacher_id')

    # @api.model
    # def create(self, vals):
    #     print "----------------------VAls----------------------",vals
    #     stud_rec=self.env['fy.details'].search([('id','=',vals.get('sequence'))])
    #     print "sequence                   ",stud_rec
    #
    #     res = super(Teacher, self).create(vals)
    #     return res

class CustomerNew(models.Model):
    _name="customer.cust"

    select=fields.Selection([('mr','Mr.'),('miss','Miss'),('mrs','Mrs.')])
    name=fields.Many2one('res.partner',string="Customer Name")
    name1=fields.Many2one('res.users',string="vendor Name")
    history=fields.One2many('customer.history1','cust_id',string="History")
    service=fields.Many2many('customer.history1','cust_hobby1','customer_id','cust_id')

class History(models.Model):
    _name="customer.history1"

    date_time=fields.Datetime(string="start_date",default=fields.Datetime.now,
                              index=True, copy=False)
    problem=fields.Char(string="problem",require=True)
    next_date=fields.Date(string="next_date")
    prec=fields.Char('prescription')
    cust_id=fields.Many2one('customer.new1',string='Customer Name')


class Rno(models.Model):
    _name="r.no"
    _rec_name = 'rno'

    rno=fields.Char('Roll no',size=4,required=True)
    name=fields.Char('Name',translate=True)
    address = fields.Char(string="Address", require=True, translate=True)
    email_id = fields.Char(string="Email_id", require=True, translate=True)
    mobile_no = fields.Char(string="Mobile no", size=10, require=True, translate=True)
    state = fields.Char(string="State", require=True, translate=True)
    marks = fields.Float(string="Marks", size=2, require=True, translate=True)
    is_student=fields.Boolean('Is_Student')
    is_teacher=fields.Boolean('Is_Teacher')
    img = fields.Binary("image", attachment=True, store=True)

    _sql_constraints = [('rno_uniq', 'unique(rno)', "The Roll No must be unique.")]


