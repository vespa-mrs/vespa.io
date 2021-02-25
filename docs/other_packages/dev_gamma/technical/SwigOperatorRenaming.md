# Operator Renaming for Swig
From the Swig 1.3 documentation:
www.swig.org

See website for latest news on SWIG and any additions to this list.

```
    // name conversion for overloaded operators. 
    // replace "*::" with "YourObject::"

    %rename(__add__)              *::operator+;
    %rename(__pos__)              *::operator+();
    %rename(__pos__)              *::operator+() const;
    %rename(__sub__)              *::operator-;
    %rename(__neg__)              *::operator-() const;
    %rename(__neg__)              *::operator-();
    %rename(__mul__)              *::operator*;
    %rename(__deref__)            *::operator*();
    %rename(__deref__)            *::operator*() const;
    %rename(__div__)              *::operator/;
    %rename(__mod__)              *::operator%;
    %rename(__logxor__)           *::operator^;
    %rename(__logand__)           *::operator&;
    %rename(__logior__)           *::operator|;
    %rename(__lognot__)           *::operator~();
    %rename(__lognot__)           *::operator~() const;
    %rename(__not__)              *::operator!();
    %rename(__not__)              *::operator!() const;
    %rename(__assign__)           *::operator=;
    %rename(__add_assign__)       *::operator+=;
    %rename(__sub_assign__)       *::operator-=;
    %rename(__mul_assign__)       *::operator*=;
    %rename(__div_assign__)       *::operator/=;
    %rename(__mod_assign__)       *::operator%=;
    %rename(__logxor_assign__)    *::operator^=;
    %rename(__logand_assign__)    *::operator&=;
    %rename(__logior_assign__)    *::operator|=;
    %rename(__lshift__)           *::operator<<;
    %rename(__lshift_assign__)    *::operator<<=;
    %rename(__rshift__)           *::operator>>;
    %rename(__rshift_assign__)    *::operator>>=;
    %rename(__eq__)               *::operator==;
    %rename(__ne__)               *::operator!=;
    %rename(__lt__)               *::operator<;
    %rename(__gt__)               *::operator>;
    %rename(__lte__)              *::operator<=;
    %rename(__gte__)              *::operator>=;
    %rename(__and__)              *::operator&&;
    %rename(__or__)               *::operator||;
    %rename(__preincr__)          *::operator++();
    %rename(__postincr__)         *::operator++(int);
    %rename(__predecr__)          *::operator--();
    %rename(__postdecr__)         *::operator--(int);
    %rename(__comma__)            *::operator,();
    %rename(__comma__)            *::operator,() const;
    %rename(__member_ref__)       *::operator->;
    %rename(__member_func_ref__)  *::operator->*;
    %rename(__funcall__)          *::operator();
    %rename(__aref__)             *::operator[];
}}}