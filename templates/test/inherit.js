function inherit(Target, Origin) {
    function F() {};
    F.prototype = Origin.prototype;
    Target.prototype = new F();
    Target.prototype.constuctor = Target;
    Target.prototype.uber = Origin.prototype;
}

// 继承模式，YUI3
var inherit = (function () {
    var F = function () {};
    return function (Target, Origin) {
        F.prototype = Origin.prototype;
        Target.prototype = new F();
        Target.prototype.constructor = Target;
        Target.prototype.uber = Origin.prototype;
    }
}(Target, Origin));

// 闭包，属性私有化
function Person(name, wife) {

    var prepareWife = 'zora';

    this.name = name;
    this.wife = wife;
    this.divorce = function () {
        this.wife = prepareWife;
    }
    this.setPrepareWife = function (target) {
        prepareWife = target;
    }

    this.getPrapreWife = function () {
        console.log(prepareWife);
    }
}

var person = new Person('deng', 'lily');