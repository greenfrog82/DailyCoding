const assert = require('assert');

function mysolution(str) {
    if(!str) return [];
    
    const ret = [];
    let tmp = [1, str[0]];

    [...str].slice(1).forEach(element => {
        if (tmp[1] != element) {
            ret.push(tmp);
            tmp = [1, element];
        } else {
           tmp[0] += 1;
        }
    });

    ret.push(tmp);
    return ret;
}

function othersolution(str) {
    var arr = [],
        counter = 1;

    for(var i=0; i<str.length; i++) {
        if(str[i] === str[i+1]) {
            counter++;
        } else {
            arr.push([counter, str[i]]);
            counter = 1;
        }
    }
    return arr;
}

function othersolution2(str) {
    return (str.match(/(.)\1*/g) || []).reduce((r, s) => {
        return r.push([s.length, s[0]]), r;
    }, []);
}

const runLengthEncoding = othersolution2;

var randomString = function(n){
    var i, s = "";
    for(i = 0; i < n; ++i)
      s += (new Array((Math.random() * 5 + 1) | 0)).join(String.fromCharCode((Math.random() * 26 + "A".charCodeAt(0)) | 0));
    return s;
}
  
describe("runLengthEncoding",function(){
    it("should work for some examples",function(){
        assert.deepEqual(runLengthEncoding(""), []);      
        assert.deepEqual(runLengthEncoding("abc"), [[1,'a'],[1,'b'],[1,'c']]);
        assert.deepEqual(runLengthEncoding("aab"), [[2,'a'],[1,'b']]);      
        assert.deepEqual(runLengthEncoding("hello world!"),
            [[1,'h'],[1,'e'],[2,'l'],[1,'o'],[1,' '],[1,'w'],[1,'o'],[1,'r'],[1,'l'],[1,'d'],[1,'!']]);
        assert.deepEqual(runLengthEncoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"),
            [[34,'a'], [3,'b']]);
        assert.deepEqual(
        runLengthEncoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"),
            [[12,'W'],[1,'B'],[12,'W'],[3,'B'],[24,'W'],[1,'B'],[14,'W']]
        );
    });
});
describe("inverse operations",function(){
    it("should return the original string",function(){
        var i, inversRLE = function(arr) {
            return arr.reduce(function(p,e){ return p += (new Array(e[0] + 1).join(e[1])); }, "");
        }, s;
        for(i = 0;  i < 100; ++i){
            s = randomString(20);
            assert.equal(inversRLE(runLengthEncoding(s)), s);
        }     
    });
});