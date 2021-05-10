
---
title: 'Angular 12.0.0-rc.2 发布，Web 前端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7928'
author: 开源中国
comments: false
date: Sun, 09 May 2021 23:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7928'
---

<div>   
<div class="content">
                                                                                            <p>Angular 12.0.0-rc.0 现已发布，具体更新内容如下：</p> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li><strong>animations：</strong>确保过渡命名空间顺序一致（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F19854" target="_blank">＃19854</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F01cc99589bc449eaf3b1de2c94636de878843fba" target="_blank">01cc995</a>）</li> 
 <li><strong>common：</strong>为具有 HttpClient request body 的布尔值添加正确的 ContentType（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F38924" target="_blank">＃38924</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41885" target="_blank">＃41885</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F922a60283183c47a268fd084302b2bc87267a73e" target="_blank">922a602</a>）</li> 
 <li><strong>compiler-cli：</strong>将 linker 作为 Babel 插件公开（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41918" target="_blank">＃41918</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F8fdac8f4361fd4ac0f20c21c98289c19e8864347" target="_blank">8fdac8f</a>）</li> 
 <li><strong>compiler-cli：</strong>在 reference emitters 中更倾向于 non-aliased exports（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41866" target="_blank">＃41866</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F75bb931889b946c243161a6ce0503bc7d08a6565" target="_blank">75bb931</a>），closes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41443" target="_blank">＃41443 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41277" target="_blank">＃41277</a></li> 
 <li><strong>core：</strong> AsyncPipe 现在与 RxJS 7 兼容（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41590" target="_blank">＃41590</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F9759bca339b44ed78ec6aafab0336d531d285f90" target="_blank">9759bca</a>）</li> 
 <li><strong>core：</strong>使用表达式绑定处理多个 i18n 属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41882" target="_blank">＃41882</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F73c6c64f82d45c34203d4d18d759ad0c33a6b221" target="_blank">73c6c64</a>），closes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41869" target="_blank">＃41869</a></li> 
 <li><strong>localize</strong><strong>：</strong>将丢失目标的错误放宽为警告（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41944" target="_blank">＃41944</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F35ceed2061a890a70576dc7afa0b779f3779ae7b" target="_blank">35ceed2</a>），closes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F21690" target="_blank">＃21690</a></li> 
</ul> 
<p><strong>性能改进</strong></p> 
<ul> 
 <li> <p><strong>core：</strong>对监听器指令的较小改进（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41807" target="_blank">＃41807</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F9346d61d92c722175ca7673efe475e838546fef7" target="_blank">9346d61</a>）</p> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">https://github.com/angular/angular/blob/master/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            