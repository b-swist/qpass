import Std.Math.*;
import Std.Arrays.*;

function Lowercase() : String[] {
    [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    ]
}

function Uppercase() : String[] {
    [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
}

function Digits() : String[] {
    [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
}

function Alphanumeric() : String[] {
    Lowercase() + Uppercase() + Digits()
}

function Symbols() : String[] {
    [ "!", "@", "#", "$", "%", "^", "&", "*" ]
}

function Joined(array : String[]) : String {
    return Fold((acc, s) -> acc + s, "", array);
}

operation RandomInt(max : Int) : Int {
    let n = BitSizeI(max);
    mutable result = 0;

    repeat {
        use qs = Qubit[n];
        ApplyToEach(H, qs);
        set result = MeasureInteger(qs);
    } until result <= max;

    return result;
}
