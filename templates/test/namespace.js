// 管理变量，防止污染全局，适用于模块化开发

var init = (function (){
    var name = 'lily';
    function getName() {
        console.log(name)
    }

    return function () {
        getName();
    }
}());

init();