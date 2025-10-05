import reflex as rx
from app.states.auth_state import AuthState


def student_dashboard() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "لوحة تحكم الطالب", class_name="text-3xl font-bold text-gray-800"
                ),
                rx.el.button(
                    "تسجيل الخروج",
                    on_click=AuthState.logout,
                    class_name="bg-red-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-red-600 transition-colors",
                ),
                class_name="flex justify-between items-center w-full mb-8",
            ),
            rx.el.p("مرحباً بك في لوحة تحكم الطالب.", class_name="text-gray-600"),
            class_name="w-full max-w-4xl mx-auto flex flex-col items-center",
        ),
        class_name="font-['Inter'] bg-sky-100 flex items-start justify-center min-h-screen p-8",
        dir="rtl",
    )