import Std.Math.*;
import Std.Core.*;
import Std.Arrays.*;
import Std.Measurement.*;

operation RandomNumber(max : Int) : Int {
    let n = BitSizeI(max);
    mutable result = 0;

    repeat {
        use qs = Qubit[n];
        ApplyToEach(H, qs);
        set result = MeasureInteger(qs);
    } until result <= max;

    return result;
}

operation GeneratePassword(length : Int, chars : String[]) : Unit {
    let max = Length(chars) - 1;
    mutable password = ["", size = length];

    for i in 0..length - 1 {
        let n = RandomNumber(max);
        password w/= i <- chars[n];
    }

    let result = Joined(password);
    Message(result);
}

function Joined(array : String[]) : String {
    return Fold((acc, s) -> acc + s, "", array);
}
