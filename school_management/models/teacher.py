from odoo import models, api, fields

class School(models.Model):
    _name = 'school.school'

    name=fields.Char('Name')
    teacher=fields.Many2many('teacher.teacher','schoo_teacher_rel', 'teacher_id','school_id')

    _sql_constraints = [('name_uniq','unique(name)',"Name is already available please write different name.")]


    # @api.model
    # def create(self, vals):
    #     teacher_rec=self.env['teacher.teacher'].search([('name','=',vals.get('name'))])
    #     print 'teacher----------------rec----------------',teacher_rec
    #     res = super(School, self).create(vals)
    #     return res

    @api.multi
    def write(self, vals):
        #print '------------------vals--------------',vals
        res=super(School, self).write(vals)
        return res

        # @api.constrains('teacher')
        # def check_teacher(self):
        #     teacher = self.search([('teacher', '=', self.teacher)])
        #     print 'adffffffffffcvsvsfsfsfsdff', teacher


class Teacher_student(models.Model):
    _name = 'school.teacher.student'

    school_name=fields.Many2one('school.school',string = 'school name')
    teacher=fields.Many2many('teacher.teacher','teacher_school_rel', 'school_id','school_teacher_id')
    student=fields.Many2many('fy.details','teacher_student_rel','fy_id','teacher_student_id')
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ],
        default='draft')
    name = fields.Char('Name')

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirm'

    @api.multi
    def action_done(self):
        self.state = 'done'

    @api.model
    def create(self, vals):
        print "vvvvvvvvvvvvvvvvvvvvvv", vals
        school_rec = self.env['school.school'].search([('id','=',vals.get('school_name'))])
        #print "school idsssssssssssss", school_rec
        #print "------------------school_rec.teacher.ids----", school_rec.teacher.ids
        vals.update({'teacher': [(6, 0, school_rec.teacher.ids)]})

        rec = self.env['school.school'].search([('id', '=', vals.get('school_name'))])
        #print 'recorddddddddddddddddddddddddddddddddd', rec.teacher.ids
        stud_rec = self.env['fy.details'].search([('teacher_id', '=', rec.teacher.ids)])
        #print 'student recoccccccccccc', stud_rec.ids
        vals.update({'student': [(6, 0, stud_rec.ids)]})

        res = super(Teacher_student, self).create(vals)

        print 'resssssssssssssssssssssssss', res
        return res

    @api.multi
    def write(self, vals):
        print "----------------", vals
        vals.update({'name':'ABCCCCCCCCCCC'})
        res = super(Teacher_student, self).write(vals)
        print '',res
        return res


