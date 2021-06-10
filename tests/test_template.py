from hutoolpy.template import render_template


def test_render_template():
    assert render_template("Hello {{ name }}!", name="World") == "Hello World!"
