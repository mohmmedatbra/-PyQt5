import reflex as rx
from typing import Literal


class AuthState(rx.State):
    """The authentication state for the app."""

    login_role: Literal["student", "teacher", "supervisor"] = "student"
    form_data: dict = {}

    @rx.event
    def handle_input(self, data: dict):
        self.form_data = data

    @rx.event
    def set_login_role(self, role: Literal["student", "teacher", "supervisor"]):
        """Set the role for the login form."""
        self.login_role = role

    @rx.event
    def login(self, form_data: dict):
        """Handle user login."""
        role = self.login_role
        print(f"Logging in as {role} with data: {form_data}")
        yield rx.toast.success(f"Login successful as {role.capitalize()}!")

    @rx.event
    def create_student_account(self, form_data: dict):
        """Handle student account creation."""
        if form_data["password"] != form_data["confirm_password"]:
            yield rx.toast.error("Passwords do not match.")
            return
        print(f"Creating student account with data: {form_data}")
        yield rx.toast.success("Student account created successfully!")
        return rx.redirect("/login")