
---
title: 'A3Mall 开源商城系统 v2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:left">2021 年 12 月 11 2.0 版本正式上线，经过 1.x 版本近两年的开源反馈磨合，对 1.x 的版本进行了重构和优化，更好的面向开发者进行二次开发。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新介绍</h2> 
<p>优化商品后端搜索功能<br> 优化上传功能<br> 优化我的推广提现记录分页功能<br> 优化资金明细分页功能<br> 优化提现记录分页功能</p> 
<p><br> 修复公共权限提示没有访问权限问题<br> 修复退款列表选项卡调用错误问题<br> 修复用户申请退款后，平台拒绝退款后不能发货问题</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">A3Mall 介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">A3Mall 后端基于 ThinkPHP6 + Bootstrap 开发的开源商城系统，前端采用uniapp开发，支持微信公众号商城、H5商城、小程序商城、APP商城、PC商城，前后端源码100%开源，支持免费商用。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云仓库： <a href="https://gitee.com/a3mall/A3Mall">https://gitee.com/a3mall/A3Mall</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开源中国： <a href="https://www.oschina.net/p/a3mall-">https://www.oschina.net/p/a3mall-</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方网站： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.a3-mall.com" target="_blank">https://www.a3-mall.com</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">开发计划</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1. 使用uniapp重构vue2 H5端所有页面 【 √ 】<br> 2. 适配H5端和支持微信公众号 【 √ 】<br> 3. 适配APP Android、IOS端功能 【 √ 】<br> 4. 移除现有wechat api使用微信 composer 开发包 【 √ 】<br> 5. 对后端进行重构和优化 【 √ 】<br> 6. 重新设计新的前端页面 【 x 】<br> 7. 使用uniapp vue3重构移动端 【 x 】<br> 8. 使用an design vue重构view层 【 x 】</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装A3Mall</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#032f62">安装后端程序</span>
<span>1</span><span style="color:#032f62">.</span> <span style="color:#032f62">下载好程序文件，解压上传到web根目录</span>
<span>2</span><span style="color:#032f62">.</span> <span style="color:#032f62">需要绑定域名访问到public目录，确保其它目录不在WEB目录下面</span>
<span>3</span><span style="color:#032f62">.</span> <span style="color:#032f62">Linux下需要给程序根目录下的runtime目录权限</span>
<span>4</span><span style="color:#032f62">.</span> <span style="color:#032f62">访问：http://域名.com/install</span>
<span>5</span><span style="color:#032f62">.</span> <span style="color:#032f62">按照提示安装</span>

<span style="color:#032f62">使用uni-app发布H5端</span>
<span>1</span><span style="color:#032f62">.</span> <span style="color:#032f62">打开HBuilderX</span> <span style="color:#032f62">-></span> <span style="color:#032f62">顶部菜单栏</span> <span style="color:#032f62">-></span> <span style="color:#032f62">发行</span> <span style="color:#032f62">-></span> <span style="color:#032f62">网站H5-手机版</span>
<span>2</span><span style="color:#032f62">.</span> <span style="color:#032f62">打包后的文件路径：/unpackage/dist/build/h5</span>
<span>3</span><span style="color:#032f62">.</span> <span style="color:#032f62">将打包完成的所有文件</span> <span style="color:#032f62">复制到商城后端/pulic/wap目录下，全部替换</span>

<span style="color:#032f62">使用uni-app发布APP端</span>
<span>1</span><span style="color:#032f62">.</span> <span style="color:#032f62">打开HBuilderX</span> <span style="color:#032f62">-></span> <span style="color:#032f62">顶部菜单栏</span> <span style="color:#032f62">-></span> <span style="color:#032f62">发行</span> <span style="color:#032f62">-></span> <span style="color:#032f62">原生APP-云打包</span>
<span>2</span><span style="color:#032f62">.</span> <span style="color:#032f62">打包后的文件路径：/unpackage/release/apk</span>
<span>3</span><span style="color:#032f62">.</span> <span style="color:#032f62">使用真机安装测试</span></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">页面展示</h3> 
<p><br> <img alt height="491" src="https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png" width="634" referrerpolicy="no-referrer"></p> 
<p><img alt height="491" src="https://oscimg.oschina.net/oscnet/up-883ef72abe75eb4e964ad633e6dfb3919dd.png" width="634" referrerpolicy="no-referrer"></p> 
<p><img alt height="491" src="https://oscimg.oschina.net/oscnet/up-6949721f68709dd42968145b6c84e34bf15.png" width="634" referrerpolicy="no-referrer"></p> 
<p><img alt height="908" src="https://oscimg.oschina.net/oscnet/up-c05b6f22055fb864f913e8305921da6f56a.png" width="634" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            