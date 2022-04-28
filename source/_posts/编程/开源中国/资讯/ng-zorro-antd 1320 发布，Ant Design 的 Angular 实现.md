
---
title: 'ng-zorro-antd 13.2.0 发布，Ant Design 的 Angular 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6793'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6793'
---

<div>   
<div class="content">
                                                                                            <p>ng-zorro-antd 是 Ant Design 的 Angular 实现，主要用于研发企业级中后台产品。全部代码开源并遵循 MIT 协议，任何企业、组织及个人均可免费使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ng-zorro-antd 13.2.0 现已发布，更新内容如下：</p> 
<h3>Bug Fixes</h3> 
<ul> 
 <li><strong>carousel:</strong><span> </span>修复<span> </span><code>nzAfterChange</code><span> </span>回调未正确触发问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7326" target="_blank">#7326</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fb517bd442fa36f4cfc5e4a37d587b4f26cfb940c" target="_blank">b517bd4</a>), closes<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7323" target="_blank">#7323</a></li> 
 <li><strong>cascader:</strong><span> </span>修复<span> </span><code>hover</code><span> </span>模式选项框无法错误隐藏问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7381" target="_blank">#7381</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F3d41ce08769bcbf337590169ded3559b092bc5cd" target="_blank">3d41ce0</a>)</li> 
 <li><strong>cascader:</strong><span> </span>修复选项框超出区域被遮挡问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7306" target="_blank">#7306</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F4c669a58f0bf02bc835e2d68402b5ea0c98511c5" target="_blank">4c669a5</a>)</li> 
 <li><strong>i18n:</strong><span> </span>修复部分翻译缺失问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7364" target="_blank">#7364</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F64e1c7cf2bd3b094a0124ed8ddb51edab284b927" target="_blank">64e1c7c</a>)</li> 
 <li><strong>list:</strong><span> </span>修复<span> </span><code>NgZone.onStable</code><span> </span>事件后未正确触发脏值检测问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7314" target="_blank">#7314</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F425f8dff39f29ba620cdeb6f4a6f45471845b819" target="_blank">425f8df</a>)</li> 
 <li><strong>modal:</strong><span> </span>关闭弹窗过程中忽略点击确认取消按钮行为 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7336" target="_blank">#7336</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fd16945249a28338ba480af46ff037d69b67b4af4" target="_blank">d169452</a>)</li> 
 <li><strong>popconfirm:</strong><span> </span>修复<span> </span><code>nzPopconfirmVisibleChange</code><span> </span>未触发问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7338" target="_blank">#7338</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F561041c3e7ce643cc57cfd2c18c22dd36da389c8" target="_blank">561041c</a>)</li> 
 <li><strong>upload:</strong><span> </span>修复在 Firefox 91/92 版本中拖拽文件会打开新页面问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7190" target="_blank">#7190</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F9b518742e3be8c85c0b2e2e66d4ffe108e43a2d0" target="_blank">9b51874</a>)</li> 
</ul> 
<h3>Features</h3> 
<ul> 
 <li><strong>code-editor:</strong><span> </span>支持设置自定义配置以支持 monaco editor 配置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7121" target="_blank">#7121</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F21ec517ba55cd20aa78298cd1050069308a9f98b" target="_blank">21ec517</a>)</li> 
 <li><strong>code-editor:</strong><span> </span>支持在<span> </span><code>NZ_CONFIG</code><span> </span>定义<span> </span><code>window.MonacoEnvironment</code><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7359" target="_blank">#7359</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F4dfd9cd21507fcf4382d5f28f03fd969d8fc425c" target="_blank">4dfd9cd</a>), closes<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6502" target="_blank">#6502</a></li> 
 <li><strong>image:</strong><span> </span>支持点击键盘左右方向键切换图片 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7321" target="_blank">#7321</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fb5f82b51eed45f9bc7f7418c90185693887b202a" target="_blank">b5f82b5</a>)</li> 
 <li><strong>input-number:</strong><span> </span>增加<span> </span><code>nzReadOnly</code><span> </span>属性支持只读方式 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7372" target="_blank">#7372</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F0da7496ba4dcc03be2827b6783a977382e487da1" target="_blank">0da7496</a>), closes<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7369" target="_blank">#7369</a></li> 
</ul> 
<h3>Performance Improvements</h3> 
<ul> 
 <li><strong>anchor:</strong><span> </span>使用<span> </span><code>passive</code><span> </span>改善的滚屏性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7330" target="_blank">#7330</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Faab060ffcebae479954355bf02804882935ef8d2" target="_blank">aab060f</a>)</li> 
 <li><strong>back-top:</strong><span> </span>使用<span> </span><code>passive</code><span> </span>改善的滚屏性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7329" target="_blank">#7329</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F7f3c4e1c5e8330597b5b0024c7b9075bccf93f44" target="_blank">7f3c4e1</a>)</li> 
 <li><strong>cascader:</strong><span> </span>减少触发不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7312" target="_blank">#7312</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fcb803f9a8c040157d83e095ce9ab0bd28a161b64" target="_blank">cb803f9</a>)</li> 
 <li><strong>image:</strong><span> </span>减少触发不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7309" target="_blank">#7309</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F752a5b6f3e76d467a839a39aa587deaed953ed72" target="_blank">752a5b6</a>)</li> 
 <li><strong>input-number:</strong><span> </span>减少触发不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7313" target="_blank">#7313</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F54386efaac97982675c8c1e1b3504cfed9671248" target="_blank">54386ef</a>)</li> 
 <li><strong>modal:</strong><span> </span>优化在不同设备上渲染帧率效果 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7293" target="_blank">#7293</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F106d346d72568f8256a942478d808d002f5421c7" target="_blank">106d346</a>)</li> 
 <li><strong>resizable:</strong><span> </span>使用<span> </span><code>passive</code><span> </span>改善性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7331" target="_blank">#7331</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F518997bcf193a59510a0dfc1db4ef306475eb990" target="_blank">518997b</a>)</li> 
 <li><strong>tree-view:</strong><span> </span>减少触发不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7307" target="_blank">#7307</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F1e0872b30873644032917f6242f585ba9bd1db30" target="_blank">1e0872b</a>)</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Freleases%2Ftag%2F13.2.0" target="_blank">https://github.com/NG-ZORRO/ng-zorro-antd/releases/tag/13.2.0</a></p>
                                        </div>
                                      
</div>
            