
---
title: 'ng-zorro-antd 14.0 发布，Ant Design 的 Angular 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5910'
author: 开源中国
comments: false
date: Sun, 28 Aug 2022 01:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5910'
---

<div>   
<div class="content">
                                                                                            <p>ng-zorro-antd 是 Ant Design 的 Angular 实现，主要用于研发企业级中后台产品。全部代码开源并遵循 MIT 协议，任何企业、组织及个人均可免费使用。</p> 
<p>ng-zorro-antd 14.0.0 正式发布，更新内容如下：</p> 
<h3>安装 ng-zorro-antd</h3> 
<pre><code>$ cd PROJECT-NAME
$ ng add ng-zorro-antd@14.0.0
</code></pre> 
<h3>Bug Fixes</h3> 
<ul> 
 <li><strong>steps:</strong> 移除顶层多余的 <code>div</code> 元素 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7582" target="_blank">#7582</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F60beabccd2459adcb973133fc139008b31abfca0" target="_blank">60beabc</a>)</li> 
</ul> 
<h3>Features</h3> 
<ul> 
 <li><strong>icon:</strong> <code>nz-icon</code> 使用方式从 <code>i</code> 元素变更为 <code>span</code> 元素 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7586" target="_blank">#7586</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F7242111c8bc2523df9d13e19521473502a4f6cf1" target="_blank">7242111</a>)</li> 
 <li><strong>popconfirm:</strong> 支持基于 <code>Promise</code> 的异步关闭 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7533" target="_blank">#7533</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F797b2617f08394b56fe0a7903dc69e2d75984219" target="_blank">797b261</a>)</li> 
</ul> 
<pre><code>- <i nz-icon nzType="search" nzTheme="outline"></i>
+ <span nz-icon nzType="search" nzTheme="outline"></span>
</code></pre> 
<h2>BREAKING CHANGES</h2> 
<ul> 
 <li><strong>pagination:</strong> <code>dom</code> 结构中添加 <code>ul</code> 标签 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7500" target="_blank">#7500</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fbecdd682514e36b188be93667a03ac74f224dcf7" target="_blank">becdd68</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Freleases%2Ftag%2F14.0.0" target="_blank">https://github.com/NG-ZORRO/ng-zorro-antd/releases/tag/14.0.0</a></p>
                                        </div>
                                      
</div>
            