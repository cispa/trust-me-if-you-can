if (window.trustedTypes && trustedTypes.createPolicy) { // Only execute in browsers with TT support
    var escapePolicy = trustedTypes.createPolicy('default', {
        createHTML: function(string) {
            return string;
        },
        createScript: function(string) {
            return string;
        },
        createScriptURL: function(string) {
            return string; 
        }
    });
}
