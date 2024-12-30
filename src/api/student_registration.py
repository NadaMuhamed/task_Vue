import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_student(data):
    data = frappe.parse_json(data)

    # Validate input data
    required_fields = ['name', 'email', 'course', 'phone', 'start_date']
    for field in required_fields:
        if field not in data or not data[field]:
            return {"message": _(f"Field '{field}' is required."), "status": "error"}

    try:
        student = frappe.get_doc({
            "doctype": "Student Registration",
            "student_name": data['name'],
            "email": data['email'],
            "course_interest": data['course'],
            "phone_number": data['phone'],
            "expected_start_date": data['start_date']
        })
        student.insert()
        return {"message": _("Registration successful"), "status": "success"}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Student Registration Error")
        return {"message": _("An error occurred during registration. Please try again."), "status": "error"}

@frappe.whitelist(allow_guest=True)
def list_registrations():
    try:
        registrations = frappe.get_all('Student Registration', fields=['name', 'student_name', 'email'])
        return {"registrations": registrations, "status": "success"}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "List Registrations Error")
        return {"message": _("An error occurred while retrieving registrations."), "status": "error"}