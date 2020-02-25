__all__ = ['js_lib']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['base64_encode', 'encap'])
@Js
def PyJsHoisted_base64_encode_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'h', 'i', 'u', 'r', 't', 'f', 'o', 'a'])
    var.put('n', Js('LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'))
    var.put('r', Js('='))
    var.put('o', Js(False))
    var.put('f', Js(False))
    var.put('u', Js(''))
    var.put('a', var.get('t').get('length'))
    var.put('r', (var.get('r') or Js('=')))
    var.put('t', (var.get('e')(var.get('t')) if var.get('f') else var.get('t')))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('a')):
        try:
            var.put('h', (((var.get('t').callprop('charCodeAt', var.get('o'))<<Js(16.0))|((var.get('t').callprop('charCodeAt', (var.get('o')+Js(1.0)))<<Js(8.0)) if ((var.get('o')+Js(1.0))<var.get('a')) else Js(0.0)))|(var.get('t').callprop('charCodeAt', (var.get('o')+Js(2.0))) if ((var.get('o')+Js(2.0))<var.get('a')) else Js(0.0))))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(4.0)):
                try:
                    if (((var.get('o')*Js(8.0))+(var.get('i')*Js(6.0)))>(var.get('a')*Js(8.0))):
                        var.put('u', var.get('r'), '+')
                    else:
                        var.put('u', var.get('n').callprop('charAt', (PyJsBshift(var.get('h'),(Js(6.0)*(Js(3.0)-var.get('i'))))&Js(63.0))), '+')
                finally:
                        var.put('i', Js(1.0), '+')
        finally:
                var.put('o', Js(3.0), '+')
    return var.get('u')
PyJsHoisted_base64_encode_.func_name = 'base64_encode'
var.put('base64_encode', PyJsHoisted_base64_encode_)
@Js
def PyJsHoisted_encap_(str, key, this, arguments, var=var):
    var = Scope({'str':str, 'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 's', 'key', 'p', 'v', 'str', 'q', 'c', 'e', 'z', 'k', 'm', 'd', 'y', 'l'])
    @Js
    def PyJsHoisted_s_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['v', 'i', 'c', 'b', 'a'])
        var.put('c', var.get('a').get('length'))
        var.put('v', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('c')):
            try:
                var.get('v').put((var.get('i')>>Js(2.0)), (((var.get('a').callprop('charCodeAt', var.get('i'))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(1.0)))<<Js(8.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(2.0)))<<Js(16.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(3.0)))<<Js(24.0))))
            finally:
                    var.put('i', Js(4.0), '+')
        if var.get('b'):
            var.get('v').put(var.get('v').get('length'), var.get('c'))
        return var.get('v')
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    @Js
    def PyJsHoisted_l_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'c', 'd', 'm', 'a', 'b'])
        var.put('d', var.get('a').get('length'))
        var.put('c', ((var.get('d')-Js(1.0))<<Js(2.0)))
        if var.get('b'):
            var.put('m', var.get('a').get((var.get('d')-Js(1.0))))
            if ((var.get('m')<(var.get('c')-Js(3.0))) or (var.get('m')>var.get('c'))):
                return var.get(u"null")
            var.put('c', var.get('m'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('d')):
            try:
                var.get('a').put(var.get('i'), var.get('String').callprop('fromCharCode', (var.get('a').get(var.get('i'))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(8.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(16.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(24.0))&Js(255))))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if var.get('b'):
            return var.get('a').callprop('join', Js('')).callprop('substring', Js(0.0), var.get('c'))
        else:
            return var.get('a').callprop('join', Js(''))
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    if (var.get('str')==Js('')):
        return Js('')
    var.put('v', var.get('s')(var.get('str'), Js(True)))
    var.put('k', var.get('s')(var.get('key'), Js(False)))
    if (var.get('k').get('length')<Js(4.0)):
        var.get('k').put('length', Js(4.0))
    var.put('n', (var.get('v').get('length')-Js(1.0)))
    var.put('z', var.get('v').get(var.get('n')))
    var.put('y', var.get('v').get('0'))
    var.put('c', (Js(2248228889)|Js(406206880)))
    var.put('q', var.get('Math').callprop('floor', (Js(6.0)+(Js(52.0)/(var.get('n')+Js(1.0))))))
    var.put('d', Js(0.0))
    while (Js(0.0)<(var.put('q',Js(var.get('q').to_number())-Js(1))+Js(1))):
        var.put('d', ((var.get('d')+var.get('c'))&(Js(2363546047)|Js(1931421248))))
        var.put('e', (PyJsBshift(var.get('d'),Js(2.0))&Js(3.0)))
        #for JS loop
        var.put('p', Js(0.0))
        while (var.get('p')<var.get('n')):
            try:
                var.put('y', var.get('v').get((var.get('p')+Js(1.0))))
                var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
                var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
                var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
                var.put('z', var.get('v').put(var.get('p'), ((var.get('v').get(var.get('p'))+var.get('m'))&(Js(4021866800)|Js(273100495)))))
            finally:
                    (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        var.put('y', var.get('v').get('0'))
        var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
        var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
        var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
        var.put('z', var.get('v').put(var.get('n'), ((var.get('v').get(var.get('n'))+var.get('m'))&(Js(3141076802)|Js(1153890493)))))
    pass
    pass
    var.put('value', var.get('l')(var.get('v'), Js(False)))
    return var.get('value')
PyJsHoisted_encap_.func_name = 'encap'
var.put('encap', PyJsHoisted_encap_)
pass
pass
pass


# Add lib to the module scope
js_lib = var.to_python()