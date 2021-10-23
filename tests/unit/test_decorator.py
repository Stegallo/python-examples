from unittest.mock import call, patch

from python_examples.decorator import main


def test_main():
    with patch("python_examples.decorator.log") as mock_log:
        main()

    assert mock_log.call_args_list == [
        call("function name = log_hi"),
        call('docstring = Prints "hi".'),
        call("Something is happening before the function is called."),
        call("hi John"),
        call("Something is happening after the function is called."),
        call("function name = decorated_log_hello"),
        call('docstring = Prints "hello".'),
        call("Something is happening before the function is called."),
        call("hello Doe"),
        call("Something is happening after the function is called."),
    ]
