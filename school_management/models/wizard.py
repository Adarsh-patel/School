from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'example.wizard'

    rno = fields.Char('Roll no', size=4, required=True)
    name = fields.Char('Name', translate=True)
    address=fields.Char('address')
    mobile_no=fields.Integer('Mobile_no')
    email=fields.Char('Email_id')

    @api.multi
    def create_rollno(self):
        r_no_obj = self.env['r.no']
        r_no_obj.create({'rno': self.rno, 'name': self.name,'address':self.address,'mobile_no':self.mobile_no,
                         'email':self.email})

        return True



class Teacher_Wizard(models.TransientModel):
    _name = 'create.teacher.wizard'

    name=fields.Char('Teacher Name')


    @api.one
    def create_tech(self):
        teacher_obj=self.env['teacher.teacher']
        teacher_obj.create({'name' : self.name})

        return True