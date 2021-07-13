
---
title: 'ng-zorro-antd 12.0.0 发布，Ant Design 的 Angular 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6921'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6921'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ng-zorro-antd 是 Ant Design 的 Angular 实现，主要用于研发企业级中后台产品。全部代码开源并遵循 MIT 协议，任何企业、组织及个人均可免费使用。</p> 
<p>ng-zorro-antd 12.0.0 正式发布，更新内容如下：</p> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><strong>pagination:</strong> 修复总页数改变时没有触发变更检查的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6780" target="_blank">#6780</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F2f1f8dcb1c7eb4f89b1ff21bf8c64d7f8a75f344" target="_blank">2f1f8dc</a>)</li> 
 <li><strong>pagination:</strong> 修复错误的按钮类型导致在表单中触发提交的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6744" target="_blank">#6744</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Ff77ab28341489e9df7f757294a6a5ad6030700f4" target="_blank">f77ab28</a>)</li> 
 <li><strong>cascader:</strong> 修复 <code>nzClear</code> 不工作的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6761" target="_blank">#6761</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F3dd9534d8059985dba3389fc52ea463bbf3381c5" target="_blank">3dd9534</a>), closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6751" target="_blank">#6751</a></li> 
 <li><strong>select:</strong> 修复选择器被点击时没有聚焦的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6786" target="_blank">#6786</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F1c9331a4f8a32a91eaaf6128bdb335f26bd6fcab" target="_blank">1c9331a</a>)</li> 
 <li><strong>time-picker:</strong> 修复 Tab 切换焦点时弹出没有关闭的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6602" target="_blank">#6602</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F0e530538ee954ce6ccc5891c0556cfb338f00b56" target="_blank">0e53053</a>)</li> 
 <li><strong>tree:</strong> 修复 firefox 下拖拽的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6771" target="_blank">#6771</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fbe20114f6b83f326045dd98b5ad3aa9fab61af03" target="_blank">be20114</a>)</li> 
 <li><strong>typography:</strong> 修复单行省略的样式问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6776" target="_blank">#6776</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fe192a70aa034913d87b00f863e27e0f6acc280de" target="_blank">e192a70</a>)</li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li><strong>checkbox:</strong> 添加 <code>nzId</code> 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6813" target="_blank">#6813</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F52235c97aaf75802cca9e81c9071fa2bdfe0208e" target="_blank">52235c9</a>)</li> 
 <li><strong>date-picker:</strong> 添加 <code>nzId</code> 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6814" target="_blank">#6814</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F28074e1749a38a19cc64bd52aefc85d3e6f1a53b" target="_blank">28074e1</a>)</li> 
 <li><strong>experimental/image:</strong> 添加新的实验性组件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6590" target="_blank">#6590</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F7e2fba39354de78219be1237eea8edf19b5799e7" target="_blank">7e2fba3</a>)</li> 
 <li><strong>popconfirm:</strong> 添加 <code>nzAutoFocus</code> 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6256" target="_blank">#6256</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F91e5d49f83c8e833e70400c65b69a2e4787fc91d" target="_blank">91e5d49</a>), closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6249" target="_blank">#6249</a></li> 
 <li><strong>rate:</strong> 为定义字符模版添加 <code>index</code> 变量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6787" target="_blank">#6787</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F7163e360fc97d48cd718c65ffa301c0253801851" target="_blank">7163e36</a>)</li> 
 <li><strong>steps:</strong> 支持环形进度条 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6132" target="_blank">#6132</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F466a093d10da6d8996adc636447be3531c5d1d76" target="_blank">466a093</a>), closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F5684" target="_blank">#5684</a></li> 
 <li><strong>timeline:</strong> 添加 <code>nzLabel</code> 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6687" target="_blank">#6687</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F86c587d7be4b7b6e936cf50e2cafa4499d735407" target="_blank">86c587d</a>), closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6682" target="_blank">#6682</a></li> 
</ul> 
<h3><strong>重大变化</strong></h3> 
<p><strong>button</strong></p> 
<ul> 
 <li><code>[nz-button][nzType="danger"]</code> 已经不再支持，请使用 <code>[nz-button][nzDanger]</code> 代替。</li> 
</ul> 
<p><strong>modal</strong></p> 
<ul> 
 <li><code>ng-content</code> 的用法已经被移除，请使用 <code><ng-template nzModalContent></ng-template></code> 代替。</li> 
</ul> 
<p><strong>drawer</strong></p> 
<ul> 
 <li><code>ng-content</code> 的用法已经被移除，请使用 <code><ng-template nzDrawerContent></ng-template></code> 代替。</li> 
</ul> 
<p><strong>tree-view</strong></p> 
<ul> 
 <li><code>[nzNodeWidth]</code> 已经被移除， 请使用 <code>[nzItemSize]</code> 代替.</li> 
</ul> 
<p><strong>nz-space-item</strong></p> 
<ul> 
 <li><code>nz-space-item, [nz-space-item]</code> 已经被移除， 请使用 <code><ng-template nzSpaceItem></ng-template></code> 代替。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Freleases%2Ftag%2F12.0.0" target="_blank">https://github.com/NG-ZORRO/ng-zorro-antd/releases/tag/12.0.0</a></p>
                                        </div>
                                      
</div>
            