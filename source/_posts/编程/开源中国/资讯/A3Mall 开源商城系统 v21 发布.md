
---
title: 'A3Mall 开源商城系统 v2.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 08:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left">A3Mall 介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">A3Mall 后端基于 ThinkPHP6 + Bootstrap 开发的开源商城系统，前端采用uniapp开发，支持微信公众号商城、H5商城、小程序商城、APP商城、PC商城，前后端源码100%开源，支持免费商用。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新介绍</h2> 
<ul> 
 <li>修复订单删除失败问题</li> 
 <li>修复移动端会员设置未更新问题</li> 
 <li>修复安装包检测环境无法下一步问题</li> 
 <li>修复注册页面发送短信失败也倒计时问题</li> 
 <li>修复找回密码调用错误验证类问题</li> 
 <li>修复资讯列表报错问题</li> 
 <li>修复搜索列表显示未上架商品问题</li> 
 <li>修复发送短信后验证错问题</li> 
 <li>优化会员标签设置</li> 
 <li>优化手机端设置</li> 
 <li>移除旧的API接口</li> 
 <li>其他优化</li> 
</ul> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云仓库： <a href="https://gitee.com/a3mall/A3Mall">https://gitee.com/a3mall/A3Mall</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开源中国： <a href="https://www.oschina.net/p/a3mall-">https://www.oschina.net/p/a3mall-</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方网站： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.a3-mall.com" target="_blank">https://www.a3-mall.com</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装A3Mall</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#032f62"><span style="color:#032f62">安装后端程序</span></span>
<span><span>1</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">下载好程序文件，解压上传到web根目录</span></span>
<span><span>2</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">需要绑定域名访问到public目录，确保其它目录不在WEB目录下面</span></span>
<span><span>3</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">Linux下需要给程序根目录下的runtime目录权限</span></span>
<span><span>4</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">访问：http://域名.com/install</span></span>
<span><span>5</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">按照提示安装</span></span>

<span style="color:#032f62"><span style="color:#032f62">使用uni-app发布H5端</span></span>
<span><span>1</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">打开HBuilderX</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">顶部菜单栏</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">发行</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">网站H5-手机版</span></span>
<span><span>2</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">打包后的文件路径：/unpackage/dist/build/h5</span></span>
<span><span>3</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">将打包完成的所有文件</span></span> <span style="color:#032f62"><span style="color:#032f62">复制到商城后端/pulic/wap目录下，全部替换</span></span>

<span style="color:#032f62"><span style="color:#032f62">使用uni-app发布APP端</span></span>
<span><span>1</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">打开HBuilderX</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">顶部菜单栏</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">发行</span></span> <span style="color:#032f62"><span style="color:#032f62">-></span></span> <span style="color:#032f62"><span style="color:#032f62">原生APP-云打包</span></span>
<span><span>2</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">打包后的文件路径：/unpackage/release/apk</span></span>
<span><span>3</span></span><span style="color:#032f62"><span style="color:#032f62">.</span></span> <span style="color:#032f62"><span style="color:#032f62">使用真机安装测试</span></span></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">页面展示</h3> 
<p><img src="https://oscimg.oschina.net/oscnet/up-cb8af821cead1beb795263cb109ac0d464d.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-883ef72abe75eb4e964ad633e6dfb3919dd.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-6949721f68709dd42968145b6c84e34bf15.png" referrerpolicy="no-referrer"></p> 
<p><img alt="输入图片说明" src="https://gitee.com/a3mall/A3Mall/raw/master/readme/images/2.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            