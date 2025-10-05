import reflex as rx
from typing import Literal


class AuthState(rx.State):
    """The authentication state for the app."""

    is_authenticated: bool = False
    current_user_role: Literal["student", "teacher", "supervisor", ""] = ""
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
        self.is_authenticated = True
        self.current_user_role = self.login_role
        yield rx.toast.success(f"Login successful as {self.login_role.capitalize()}!")
        if self.login_role == "student":
            return rx.redirect("/student-dashboard")
        if self.login_role == "teacher":
            return rx.redirect("/teacher-dashboard")
        if self.login_role == "supervisor":
            return rx.redirect("/supervisor-dashboard")

    @rx.event
    def logout(self):
        """Log the user out."""
        self.is_authenticated = False
        self.current_user_role = ""
        return rx.redirect("/login")

    @rx.event
    def check_auth(self):
        """Check if the user is authenticated."""
        if not self.is_authenticated:
            return rx.redirect("/login")

    @rx.event
    def create_student_account(self, form_data: dict):
        """Handle student account creation."""
        if form_data["password"] != form_data["confirm_password"]:
            yield rx.toast.error("Passwords do not match.")
            return
        print(f"Creating student account with data: {form_data}")
        yield rx.toast.success("Student account created successfully!")
        return rx.redirect("/login")