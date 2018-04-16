(function () {
    function addNofollowToLinks() {
        'use strict';
        if (typeof document.querySelectorAll !== 'function') {
            return;
        }
        var externalLinks = document.querySelectorAll('a.external');
        if (!externalLinks || !externalLinks.length) {
            return;
        }
        var externalLinksLength = externalLinks.length;
        for (var i = 0; i < externalLinksLength; i++) {
            if (typeof externalLinks[i].setAttribute === 'function') {
                externalLinks[i].setAttribute('rel', '_nofollow');
            }
        }
    }

    if ($ && typeof $.when === 'function') {
        $.when($.ready).then(addNofollowToLinks);
    } else {
        document.onload = addNofollowToLinks;
    }
})();
