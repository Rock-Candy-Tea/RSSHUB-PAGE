
---
title: 'Angular 12.0.0-rc.0 发布，Web 前端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1682'
author: 开源中国
comments: false
date: Sat, 24 Apr 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1682'
---

<div>   
<div class="content">
                                                                                            <p>Angular 12.0.0-rc.0 现已发布，具体更新内容如下：</p> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li><strong>animations：</strong>允许 shadow DOM 中的元素有动画（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F40134" target="_blank">＃40134</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fdad42c8cd669357f9c862023abc5f4695863040d" target="_blank">dad42c8</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F25672" target="_blank">＃25672</a></li> 
 <li><strong>common：</strong>viewport scroller 无法找到 shadow DOM 内的元素（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41644" target="_blank">＃41644</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fc0f5ba3d36b2509a71d09c436d247211a58ee80d" target="_blank">c0f5ba3</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41470" target="_blank">＃41470</a></li> 
 <li><strong>compiler：</strong>non-literal 的内联模板在部分编译中处理不正确（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41583" target="_blank">＃41583</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fab257b370127dce70bd3ee7ad6d64d3a9ad5ae95" target="_blank">ab257b3</a>）</li> 
 <li><strong>compiler：</strong>不为备用命名空间内的 ng-template 生成更新指令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41669" target="_blank">＃41669</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F2bcbbda78913be014534fde72318ab09795350f9" target="_blank">2bcbbda</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41308" target="_blank">＃41308</a></li> 
 <li><strong>compiler-cli：</strong>模板中的 autocomplete literal 类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41456" target="_blank">＃41456</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41645" target="_blank">＃41645</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F8b2b5ef903a21b599dfc4bfe8b0c64f7c136c3a9" target="_blank">8b2b5ef</a>）</li> 
 <li><strong>compiler-cli：</strong>如果组件没有内联样式，则在预置时不会出错（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41602" target="_blank">＃41602</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fa5fe8b95893798467c4eea2b3d38d49f6d0ce1b3" target="_blank">a5fe8b9</a>）</li> 
 <li><strong>router：</strong>只有当 reuse strategy 表明它应该重新连接时，才会检索存储的路由（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F30263" target="_blank">＃30263</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fa4ff071e3f08e3de6d4d3f97c747c2f42b827c49" target="_blank">a4ff071</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F23162" target="_blank">＃23162</a></li> 
 <li><strong>router：</strong>递归合并空路径匹配（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41584" target="_blank">＃41584</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F1179dc8cb32c9fc451d2af9215c4740af9d2e291" target="_blank">1179dc8</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F23162" target="_blank">#23162</a></li> 
</ul> 
<p><strong>性能改进</strong></p> 
<ul> 
 <li> <p><strong>compiler：</strong>减少生成的安全访问和无效合并的代码量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41563" target="_blank">＃41563</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F9a3b82f19d26819c95c340d702c1c32787f2931e" target="_blank">9a3b82f</a>），closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41437" target="_blank">＃41437 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41491" target="_blank">＃41491</a></p> </li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">https://github.com/angular/angular/blob/master/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            