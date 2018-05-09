from odoo import api,fields,models

class calc(models.Model):
    _name="percentage.calc"


    @api.multi
    def _get_total(self):
        total = 0.0
        print "\n\n\n\n COMPUTE METHOD CALLEDDDDDDDD"
        for rec in self:
            rec.total_marks += rec.java + rec.c + rec.python + rec.dbms + rec.ds
            print "\n\n\n\n TOTAL ISD",rec.total_marks

    java=fields.Float('java')
    c=fields.Float('c')
    python=fields.Float('python')
    dbms=fields.Float('dbms')
    ds=fields.Float('ds')
    perc=fields.Float(compute='per')
    total_marks =fields.Float(compute='_get_total')

    @api.one
    def per(self):
        total=self.java+self.c+self.python+self.dbms+self.ds
        self.perc=total/5.0
        print "Percentage",self.perc


