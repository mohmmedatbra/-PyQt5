import reflex as rx
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def teacher_dashboard() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            _header(),
            rx.el.div(
                _upload_card(
                    title="رفع ملف محاضرة أو مرجع",
                    icon="file-text",
                    file_name_placeholder="مثال: قواعد البيانات 2 - المحاضرة 3",
                    button_text="رفع الملف",
                ),
                _upload_card(
                    title="رفع فروض منزلية (H.W)",
                    icon="edit-3",
                    file_name_placeholder="مثال: برمجة الويب - فرض منزلي 1",
                    button_text="رفع الفرض المنزلي",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-5xl",
            ),
            class_name="flex flex-col items-center w-full",
        ),
        class_name="font-['Inter'] bg-gradient-to-b from-blue-600 to-blue-500 min-h-screen p-8",
        dir="rtl",
    )


def _header() -> rx.Component:
    return rx.el.div(
        rx.el.h1("لوحة تحكم الأستاذ", class_name="text-2xl font-bold text-white"),
        rx.el.button(
            "رجوع",
            on_click=AuthState.logout,
            class_name="bg-white/20 text-white font-semibold py-2 px-4 rounded-lg hover:bg-white/30 transition-colors",
        ),
        class_name="flex items-center justify-between w-full max-w-5xl mx-auto mb-10",
    )


def _upload_card(
    title: str, icon: str, file_name_placeholder: str, button_text: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="text-blue-600"),
            rx.el.h2(title, class_name="font-bold text-lg text-gray-800"),
            class_name="flex items-center space-x-3 rtl:space-x-reverse mb-6",
        ),
        _form_input("اسم الملف", file_name_placeholder),
        _academic_year_select(),
        _file_upload_area(),
        rx.el.button(
            button_text,
            class_name="w-full bg-blue-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-blue-700 transition-colors mt-6",
        ),
        class_name="bg-white p-6 rounded-2xl shadow-lg",
    )


def _form_input(label: str, placeholder: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            placeholder=placeholder,
            class_name="w-full bg-gray-50 border border-gray-300 rounded-md py-2 px-3 text-sm",
        ),
        class_name="mb-4",
    )


def _academic_year_select() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "السنة الأكاديمية", class_name="text-sm font-medium text-gray-700 mb-1"
        ),
        rx.el.select(
            rx.foreach(
                DashboardState.academic_years,
                lambda year: rx.el.option(year, value=year),
            ),
            placeholder="اختر السنة الأكاديمية",
            class_name="w-full bg-gray-50 border border-gray-300 rounded-md py-2 px-3 text-sm",
        ),
        class_name="mb-4",
    )


def _file_upload_area() -> rx.Component:
    return rx.upload.root(
        rx.el.div(
            rx.icon("cloud_upload", class_name="text-blue-500 h-10 w-10"),
            rx.el.p("اختر ملف المحاضرة", class_name="font-semibold text-gray-700"),
            rx.el.p("أو اسحب الملف وأسقطه هنا", class_name="text-sm text-gray-500"),
            class_name="flex flex-col items-center justify-center p-6 bg-blue-50/50 border-2 border-dashed border-blue-200 rounded-lg text-center h-40",
        ),
        class_name="w-full cursor-pointer",
    )