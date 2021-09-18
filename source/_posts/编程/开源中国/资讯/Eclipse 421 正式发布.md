
---
title: 'Eclipse 4.21 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-290c182604fcd736074820a595f6fea3c0e.png'
author: 开源中国
comments: false
date: Sat, 18 Sep 2021 07:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-290c182604fcd736074820a595f6fea3c0e.png'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse 4.21 正式版已发布。</p> 
<div> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>Eclipse 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fdownloads%2Fdrops4%2FR-4.21-202109060500%2F" target="_blank">https://download.eclipse.org/eclipse/downloads/drops4/R-4.21-202109060500/</a></li> 
  <li>更新内容：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.21%2F" target="_blank">https://www.eclipse.org/eclipse/news/4.21/</a></li> 
  <li>升级已有安装版本 (non-production)：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.21%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.21/</a></li> 
  <li>Specific repository good for building against：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.21%2FR-4.21-202109060500%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.21/R-4.21-202109060500/</a></li> 
  <li>Equinox 相关下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Fequinox%2Fdrops%2FR-4.21-202109060500%2F" target="_blank">https://download.eclipse.org/equinox/drops/R-4.21-202109060500/</a></li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.21%2F" target="_blank">Eclipse 4.21 更新亮点</a>：</strong></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Views, Dialogs and Toolbar  </p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>在类 PlainMessageDialog 中引入了一个新的 API，它使用一个构建器模式来创建一个不可变的 PlainMessageDialog 实例。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-290c182604fcd736074820a595f6fea3c0e.png" referrerpolicy="no-referrer"></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Java Editor</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>添加了一个新的清理，将代码转换为使用 StringBuilder（在 Java 1.5 中添加）而不是StringBuffer，后者有同步方法，比使用 StringBuilder 慢。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-0d4c244e6599506318717ca5e6d33edf935.png" referrerpolicy="no-referrer"></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>用户可以使用下面的快速修复方法（Ctrl+1）来声明一个密封的接口为其允许类型的超级接口。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-b806a442b452e7f4fcab8aed6e3b1f19967.png" referrerpolicy="no-referrer"></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>用户可以使用下面的快速修复方法（Ctrl+1），将一个子类型添加到一个密封的超级类型的允许类型中。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a55d9ae5049e630383f973fc7aac557e5b9.png" referrerpolicy="no-referrer"></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SWT 改动</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>StyledText 小组件现在有一个新的 setSelectionRanges(int[] ranges) API，允许传递任意数量的选择范围。当使用多个范围时，文本小组件将显示它们为不同的字符和选择范围，并允许在这些位置同时进行编辑。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">p2 改动</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>当要安装的组件设置了pgp.signatures属性时，除了负责验证签名对给定组件是否有效的完整性检查外，签名者的公钥现在将在与未知证书相同的信任对话框中向用户提示，用户必须声明签名者的密钥是受信任的才能完成安装。所有 PGP 签名的组件需要至少有一个受信任的签名者才能完成安装；没有受信任签名者的组件会阻止安装。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">API Tools</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>首选项中的所有微版本的用法以及错误、警告信息都已改为服务版本。</li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.21%2F" target="_blank">https://www.eclipse.org/eclipse/news/4.21/</a>。</p> 
</div>
                                        </div>
                                      
</div>
            