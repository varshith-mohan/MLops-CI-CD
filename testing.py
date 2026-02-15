import pytest
from streamlit.testing.v1 import AppTest


def get_rendered_text(app):
    """Helper to extract visible text from Streamlit app"""
    return [t.value for t in app.text]


@pytest.fixture
def app():
    at = AppTest.from_file("web-app.py")
    at.run()
    return at


def test_addition(app):
    app.number_input(key="num1").set_value(5)
    app.number_input(key="num2").set_value(3)
    app.selectbox(key="operation").set_value("Addition")
    app.run()

    text = get_rendered_text(app)
    assert "Result: 5.0 + 3.0 = 8.0" in text
    assert "The square of 5.0 is: 25.0" in text
    assert "The square of 3.0 is: 9.0" in text


def test_subtraction(app):
    app.number_input(key="num1").set_value(10)
    app.number_input(key="num2").set_value(4)
    app.selectbox(key="operation").set_value("Subtraction")
    app.run()

    text = get_rendered_text(app)
    assert "Result: 10.0 - 4.0 = 6.0" in text


def test_multiplication(app):
    app.number_input(key="num1").set_value(6)
    app.number_input(key="num2").set_value(7)
    app.selectbox(key="operation").set_value("Multiplication")
    app.run()

    text = get_rendered_text(app)
    assert "Result: 6.0 × 7.0 = 42.0" in text


def test_division(app):
    app.number_input(key="num1").set_value(20)
    app.number_input(key="num2").set_value(5)
    app.selectbox(key="operation").set_value("Division")
    app.run()

    text = get_rendered_text(app)
    assert "Result: 20.0 ÷ 5.0 = 4.0" in text


def test_division_by_zero(app):
    app.number_input(key="num1").set_value(10)
    app.number_input(key="num2").set_value(0)
    app.selectbox(key="operation").set_value("Division")
    app.run()

    errors = [e.value for e in app.error]
    assert "Division by zero is not allowed." in errors


def test_square_calculation(app):
    app.number_input(key="num1").set_value(4)
    app.number_input(key="num2").set_value(2)
    app.run()

    text = get_rendered_text(app)
    assert "The square of 4.0 is: 16.0" in text
    assert "The square of 2.0 is: 4.0" in text
