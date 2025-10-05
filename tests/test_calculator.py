from src.calculator import Addition, TalkingUser, Subtract, Multiply, Divide
from src.calculator import Sqrt, Power, Factorial, UserInput, History
from contextlib import nullcontext as does_not_raise
import pytest


class TestComunication:

    @pytest.fixture
    def set_object(self):
        return TalkingUser()

    def test_comunication_hi(self, set_object, capsys):
        set_object.say_hi()
        captured = capsys.readouterr()
        assert captured.out.strip() == set_object._hi_words

    def test_comunication_bye(self, set_object, capsys):
        set_object.say_bye()
        captured = capsys.readouterr()
        assert captured.out.strip() == set_object._bye_words


class TestOperations:

    @pytest.mark.parametrize(
        "x, y, res, expactation",
        [
            (15, 5, 20, does_not_raise()),
            (25, 10, 35, does_not_raise()),
            (-5, 10, 5, does_not_raise()),
            (-5, "10", -15, pytest.raises(TypeError)),
        ]
    )
    def test_addition(self, x, y, res, expactation):
        with expactation:
            assert Addition().execute(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expactation",
        [
            (50, 5, 45, does_not_raise()),
            (25, 10, 15, does_not_raise()),
            (-5, 10, -15, does_not_raise()),
            (-5, "10", -15, pytest.raises(TypeError)),
        ]
    )
    def test_substract(self, x, y, res, expactation):
        with expactation:
            assert Subtract().execute(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expactation",
        [
            (5, 2, 10, does_not_raise()),
            (30, 3, 90, does_not_raise()),
            (-2, 10, -20, does_not_raise()),
        ]
    )
    def test_multiply(self, x, y, res, expactation):
        with expactation:
            assert Multiply().execute(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expactation",
        [
            (10, 2, 5, does_not_raise()),
            (100, 3, 33.3, does_not_raise()),
            (2, 0, None, pytest.raises(ZeroDivisionError)),
            (-5, "10", -15, pytest.raises(TypeError)),
        ]
    )
    def test_divide(self, x, y, res, expactation):
        with expactation:
            result = Divide().execute(x, y)
            if y != 0:
                assert result == pytest.approx(res, 0.05)
        with expactation:
            assert Divide().execute(x, y) == pytest.approx(res, 0.05)

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (10, 2, 100, does_not_raise()),
            (100, 3, 1_000_000, does_not_raise()),
            (-5, "10", None, pytest.raises(TypeError)),
            (-5, None, None, pytest.raises(TypeError)),
        ]
    )
    def test_power(self, x, y, res, expectation):
        with expectation:
            result = Power().execute(x, y)
            if res is not None:
                assert result == pytest.approx(res, 0.1)

    @pytest.mark.parametrize(
        "x, res, expectation",
        [
            (121, 11, does_not_raise()),
            (9, 3, does_not_raise()),
            (-5, None, pytest.raises(ValueError)),
        ]
    )
    def test_sqrt(self, x, res, expectation):
        with expectation:
            result = Sqrt().execute(x)
            if res is not None:
                assert result == pytest.approx(res, 0.1)

    @pytest.mark.parametrize(
        "x, res, expectation",
        [
            (5, 120, does_not_raise()),
            (3, 6, does_not_raise()),
            (-5, None, pytest.raises(ValueError)),
        ]
    )
    def test_factorial(self, x, res, expectation):
        with expectation:
            result = Factorial().execute(x)
            if res is not None:
                assert result == pytest.approx(res, 0.1)


class TestOtherStuff:
    @pytest.fixture
    def obj(self):
        return UserInput()

    def test_user_input(self, obj, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "15")
        result = obj.get_number("Enter the number")
        assert result == 15.0


class TestHistory:
    @pytest.fixture
    def obj_history(self):
        return History()

    def test_add_history(self, obj_history):
        obj_history.add_history("Addition: 2 + 2 = 4")
        assert "Addition: 2 + 2 = 4" in obj_history.history_of_inputs
        assert len(obj_history.history_of_inputs) == 1

    def test_show_history(self, obj_history, capsys):
        obj_history.add_history("Multiply: 3 * 3 = 9")
        obj_history.show_history()
        captured = capsys.readouterr()
        assert "Multiply: 3 * 3 = 9" in captured.out

    def test_show_empty_history(self, obj_history, capsys):
        obj_history.show_history()
        captured = capsys.readouterr()
        assert "The history is empty!" in captured.out

    def test_clear_history(self, obj_history, capsys):
        obj_history.add_history("Some operation")
        obj_history.clear_history()
        captured = capsys.readouterr()
        assert "History has been cleared!" in captured.out
        assert obj_history.history_of_inputs == []
