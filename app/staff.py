# staff handling

from flask import abort
from . import models 


def get_all():
    staff = models.Staff.query.all()
    staff_dicts = map(lambda staff: staff.to_dict(), staff)
    if staff is None:
        abort(404, f"Staff not found")
    return list(staff_dicts)

def get_one(id):
    staff = models.Staff.query.filter_by(id=id).first()
    if staff is None:
        abort(404, f"Staff with identifier {id} not found")
    return staff.to_dict()
