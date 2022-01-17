
---
title: '大公司为什么无法轻松使用更新的c++版本？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=3193'
author: 知乎
comments: false
date: Mon, 17 Jan 2022 03:34:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=3193'
---

<div>   
pansz的回答<br><br><p data-pid="3jexcOjg">如果只是改编译选项的标准，那当然简单。</p><p data-pid="GUX6u_ux">只要当前编译器支持，升高支持级别那根本就不叫事儿，我们这哪怕一个项目组员，自己偷偷改了编译器选项，比如从 -std=c++11 改成 -std=c++14，然后只要他自己编译过了，下回的测试不崩，以后不出事，基本就没人会来问责。</p><p data-pid="9MLdKoWW">问题就是，当前使用的编译器很可能就不支持你想要的新版本标准。那就得换编译器。</p><p data-pid="lmJZf5rZ">而换编译器，就是大事了。</p><p data-pid="GfpL1VVS">我们很多项目往往都是直接把编译器放进版本管理系统内的。也就是说项目跟编译器一起走，严格避免未来找不到能编译对应项目的编译器的问题。</p><p data-pid="fvz5BDCu">所以你要真想换编译器，那你就把整个编译器提供好，整理一个能直接提交进版本管理的工具链，你负责维护新的工具链，那你只管升。</p><hr><p data-pid="LuW51WSc">所以你问为什么有些公司无法轻松使用更新的C++版本？</p><p data-pid="fTg1ZKmC">答：因为他们无人维护编译器。</p><p><br></p><p data-pid="OW-_QJua">但凡有专人维护编译器，那么升级编译器对他来说就会是一项业绩，那么，自然就有人愿意升级了。</p><p></p><p></p>  
</div>
            