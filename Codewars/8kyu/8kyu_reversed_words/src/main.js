const assert = require('assert')

function mysolution(str) {
    return str.split(' ').reverse().join(' ')
}

const reverseWords = mysolution

describe("reverseWords",function(){
    it("should work for some examples", function(){
        assert.equal(reverseWords("hello world!"), "world! hello")
        assert.equal(reverseWords("yoda doesn't speak like this" ),  "this like speak doesn't yoda")
        assert.equal(reverseWords("foobar"                       ),  "foobar")
        assert.equal(reverseWords("kata editor"                  ),  "editor kata")
        assert.equal(reverseWords("row row row your boat"        ),  "boat your row row row")
    });
});