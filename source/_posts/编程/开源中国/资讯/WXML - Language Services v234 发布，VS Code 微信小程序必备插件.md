
---
title: 'WXML - Language Services v2.3.4 发布，VS Code 微信小程序必备插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://funimg.pddpic.com/mobile_piggy/a3fe1277-f521-4bdc-bda8-e87eaddfd58e.png.slim.c1.png'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 11:51:00 GMT
thumbnail: 'https://funimg.pddpic.com/mobile_piggy/a3fe1277-f521-4bdc-bda8-e87eaddfd58e.png.slim.c1.png'
---

<div>   
<div class="content">
                                                                                            <h1>WXML - Language Services</h1> 
<p><img alt height="246" src="https://funimg.pddpic.com/mobile_piggy/a3fe1277-f521-4bdc-bda8-e87eaddfd58e.png.slim.c1.png" width="860" referrerpolicy="no-referrer"></p> 
<p>微软VSCode插件市场地址 -> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dqiu8310.minapp-vscode" target="_blank">https://marketplace.visualstudio.com/items?itemName=qiu8310.minapp-vscode</a></p> 
<p>VSCode微信小程序开发插件WXML - Language Services(原minapp)在停止迭代两年后，于近日开始发布迭代2.3.x版本。上一次发布版本还是在2019年8月1日，此次发布的版本优化了插件体积大小，更新了插件依赖以及微信小程序相关元数据。</p> 
<h1><strong>更新日志<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwx-minapp%2Fminapp-vscode%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">Changelog</a></strong></h1> 
<h2 style="text-align:start">2.3.4 / 2021-09-01</h2> 
<ul> 
 <li>添加钉钉用户交流群二维码</li> 
 <li>删除不再使用的travis-ci配置文件</li> 
</ul> 
<h2 style="text-align:start">2.3.3 / 2021-08-31</h2> 
<ul> 
 <li>参考vscode-eslint处理webpack打包时<code>require</code>语句失效的问题</li> 
</ul> 
<h2 style="text-align:start">2.3.2 / 2021-08-31</h2> 
<ul> 
 <li>将prettier打包进vsix文件，修复#103</li> 
</ul> 
<h2 style="text-align:start">2.3.1 / 2021-08-30</h2> 
<ul> 
 <li>插件更名</li> 
 <li>增加deploy状态badge</li> 
</ul> 
<h2 style="text-align:start">2.3.0 / 2021-08-30</h2> 
<ul> 
 <li>优化插件vsix文件体积(2.88mb -> 261kb)</li> 
 <li>插件更名&更换icon</li> 
 <li>更新代码提示中的微信官方文档链接/wepy文档链接</li> 
 <li>增加Github Actions CI</li> 
 <li>增加issue和PR模板</li> 
 <li>优化wxml语法高亮tmLanguage配置</li> 
</ul> 
<h1>让我们来看看插件有哪些功能！</h1> 
<h3 style="text-align:start">标签名与属性名自动补全</h3> 
<p><img alt="标签名与属性名自动补全" height="460" src="https://n1image.hjfile.cn/res7/2018/03/01/13631761451ae134c6eb3ea2ed1a6a12.gif" width="996" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">根据组件已有的属性，自动筛选出对应支持的属性集合</h3> 
<ul> 
 <li> <p>当 picker 的 mode="selector" 时，有 <code>range</code> 和 <code>range-key</code> 的属性</p> </li> 
 <li> <p>当 picker 的 mode="time" 时，有 <code>start</code> 和 <code>end</code> 的属性</p> </li> 
</ul> 
<p><img alt height="386" src="https://n1image.hjfile.cn/res7/2018/03/09/5c5704b51a37df84b5c6663d29a545f6.gif" width="948" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">属性值自动补全（有可选值的情况下才会触发补全）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/03/10/aaba780a36f1de1b87687295bc6fc922.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">点击模板文件中的函数或属性跳转到 js/ts 定义的地方（纯 wxml 或 pug 文件才支持，vue 文件不完全支持）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/11/20/c8d41ef5bce1b2128bb7a830d06338b9.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">样式名自动补全（纯 wxml 或 pug 文件才支持，vue 文件不完全支持）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/11/15/559184bb3ff7cc2fb76c204010f6f042.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">在 vue 模板文件中也能自动补全，同时支持 pug 语言</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/04/09/0b4573624091b04566232c38df08e323.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">支持 link（纯 wxml 或 pug 文件才支持，vue 文件不支持）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/04/27/dd7f301dc1e1593209d7f7ac169fd047.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">自定义组件自动补全（纯 wxml 文件才支持，vue 或 pug 文件不支持）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/03/09/fce0b3e9496cae95c1c81523725a1fef.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">模板文件中 js 变量高亮（纯 wxml 或 pug 文件才支持，vue 文件不支持）</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/05/07/c6dd2e8613fbb02417029fb3dbd302ce.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">内置 snippets</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/05/26/4a25927085e96e6bd9f05bf735621a8b.gif" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">支持 emmet 写法</h3> 
<p><img alt src="https://n1image.hjfile.cn/res7/2018/06/22/2f692e4cf499d712d34f593a3e813522.gif" referrerpolicy="no-referrer"></p> 
<p>你希望新增哪些功能？ 欢迎在评论区留言，谢谢</p>
                                        </div>
                                      
</div>
            