
---
title: '微信小程序 eslint 插件 eslint-plugin-wxml v0.4.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://funimg.pddpic.com/mobile_piggy/4d0f5a17-574b-4fbc-aee1-1b0cbb1c46dd.png.slim.c1.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 01:54:00 GMT
thumbnail: 'https://funimg.pddpic.com/mobile_piggy/4d0f5a17-574b-4fbc-aee1-1b0cbb1c46dd.png.slim.c1.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img alt height="150" src="https://funimg.pddpic.com/mobile_piggy/4d0f5a17-574b-4fbc-aee1-1b0cbb1c46dd.png.slim.c1.png" width="150" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><strong style="color:#333333"><em>eslint-plugin-wxml</em></strong></p> 
<p>微信小程序eslint插件 <strong style="color:#333333"><em>eslint-plugin-wxml </em></strong><span style="background-color:#ffffff; color:#333333">于2021年11月5日发布了新版v0.4.1</span></p> 
<p><span style="background-color:#ffffff; color:#333333">1. 新增了规则 </span><em><strong>wxml/no-wx-if-string</strong></em><span style="background-color:#ffffff; color:#333333">，用于校验警告在使用</span><span style="color:#c0392b"><span style="background-color:#ffffff">wx:if/wx:elif</span></span><span style="background-color:#ffffff">时必须使用有效的布尔值插值，否则会产生预期之外的结果</span></p> 
<blockquote> 
 <pre><code class="language-html"><view wx:if="&#123;&#123;user&#125;&#125;"> &#123;&#123;user.name&#125;&#125;</view></code></pre> 
 <p>If you use <strong>wx:if/wx:elif</strong> as control flow, make sure <strong>wx:if/wx:elif</strong>'s value is a <span style="color:#c0392b"><strong>boolean</strong></span>, not a string (or dynamic string), otherwise the value will always be true, your code logic will be broken.</p> 
 <p><br> wx:if="&#123;&#123;show&#125;&#125; "  => wx:if="true " => true<br> wx:if="&#123;&#123;show&#125;&#125; "  => wx:if="false " => true<br> wx:if="&#123;&#123;show&#125;&#125;-s"  => wx:if="true-s" => true<br> wx:if="&#123;&#123;show&#125;&#125;-s"  => wx:if="false-s" => true</p> 
</blockquote> 
<p><strong><em>eslint插件使用示例：</em></strong></p> 
<p><img alt height="352" src="https://funimg.pddpic.com/mobile_piggy/3c944e77-0792-4bee-a137-aa6922d94cfb.gif" width="1162" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">官方文档地址: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feslint-plugin-wxml.js.org" target="_blank">https://eslint-plugin-wxml.js.org</a></p> 
<p><span style="background-color:#ffffff; color:#333333">相关代码变更详见  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwxmlfile%2Feslint-plugin-wxml%2Fcompare%2Fv0.4.0...v0.4.1" target="_blank">https://github.com/wxmlfile/eslint-plugin-wxml/compare/v0.4.0...v0.4.1</a></p>
                                        </div>
                                      
</div>
            