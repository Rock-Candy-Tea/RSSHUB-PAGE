
---
title: Re_ _PATCH 21_27_ treewide_ surround file paths in Kconfig files
 with double quotes
categories: 
    - 编程
    - Linux Patchwork - Patch Comments
author: Linux Patchwork - Patch Comments
comments: false
date: Tue, 11 Dec 2018 11:19:50 GMT
thumbnail: 
---

<div>   
On Tue, Dec 11, 2018 at 08:01:04PM +0900, Masahiro Yamada wrote:<br>&#x3E; The Kconfig lexer supports special characters such as &#x27;.&#x27; and &#x27;/&#x27; in<br>&#x3E; the parameter context. In my understanding, the reason is just to<br>&#x3E; support bare file paths in the source statement.<br>&#x3E; <br>&#x3E; I do not see a good reason to complicate Kconfig for the room of<br>&#x3E; ambiguity.<br>&#x3E; <br>&#x3E; The majority of code already surround file paths with double quotes,<br>&#x3E; and it makes sense since the included file paths are constant string<br>&#x3E; literals.<br>&#x3E; <br>&#x3E; Make it treewide consistent now.<br>&#x3E; <br>&#x3E; Signed-off-by: Masahiro Yamada &#x3C;yamada.masahiro@socionext.com&#x3E;<br><br>Acked-by: Wolfram Sang &#x3C;wsa@the-dreams.de&#x3E;  
</div>
            