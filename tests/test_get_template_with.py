from .import client


def test_get_template_with():
    ret = client.get_template(
        "1005",
        "XXWJR"
    )
    print(ret.code, ret.msg)
    assert ret.code == "200"
