import Std.Math.*;
import Std.Convert.*;
import Std.Core.*;
import Utils.*;

operation Generate(length : Int, no_symbols : Bool) : Unit {
    mutable password = ["", size = length];
    let chars = Alphanumeric() + (no_symbols ? [] | Symbols());
    let max = Length(chars) - 1;

    for i in 0..length - 1 {
        let n = RandomInt(max);
        password w/= i <- chars[n];
    }

    let result = Joined(password);
    Message(result);
}

