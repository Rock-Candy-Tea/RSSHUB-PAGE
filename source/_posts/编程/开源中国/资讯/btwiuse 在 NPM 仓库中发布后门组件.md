
---
title: 'btwiuse 在 NPM 仓库中发布后门组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/a2f93fa5e0fbf216a83fe49de37884a1.jpeg'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 12:26:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/a2f93fa5e0fbf216a83fe49de37884a1.jpeg'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>报告来源：OSCS开源安全社区</p> 
 <p>更新日期：2022-07-04</p> 
</blockquote> 
<h2>事件简述</h2> 
<p>NPM 是 Node.js 包管理工具，提供了对第三方 Node.js 包的查找、下载、安装、卸载等功能。</p> 
<p>2022 年 07 月 04 日，OSCS 监测发现 NPM 官方仓库被 btwiuse 上传了 btwiuse、k0s 恶意组件包，使用恶意组件包后会在用户电脑上加载名为 k0s 的远控木马，危害较为<code>严重</code>，OSCS 提醒广大开发者关注。</p> 
<h2>详细分析</h2> 
<p>以 k0s 组件为例，其目录结构如下：</p> 
<pre><code>index.js
package.json
</code></pre> 
<p>引入该组件后会执行远控木马程序，危险代码存在于 package.json 与 index.js 文件中。</p> 
<p>恶意代码如下：</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/a2f93fa5e0fbf216a83fe49de37884a1.jpeg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/1a4f158fd73e5b9bf42bf09d8b22c9e7.png" referrerpolicy="no-referrer"></p> 
<p>进行代码溯源可发现会安装如下地址的远程控制服务</p> 
<pre><code>https://github.com/btwiuse/k0s.git/
</code></pre> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/2a6fcd0a76fa322090ddd8859bcd377d.png" referrerpolicy="no-referrer"></p> 
<p>其远控服务端地址如下</p> 
<pre><code>https://k0s.io/
</code></pre> 
<p>OSCS 开源安全社区建议广大用户做好资产自查以及预防工作，以免遭受黑客攻击。</p> 
<h2>处置建议</h2> 
<p>OSCS 开源安全社区建议用户通过以下方式排查：</p> 
<p>1、使用npm ls或npm ls -g命令查看是否安装恶意组件</p> 
<p>2、排查项目 package.json 是否引用恶意组件</p> 
<p>具体可参考：</p> 
<pre><code>https://www.oscs1024.com/hd/MPS-2022-41934/
</code></pre> 
<h2>时间线</h2> 
<p>7月1日，攻击者上传了 k0s 的恶意包</p> 
<p>7月3日，攻击者上传了 btwiuse 的恶意包</p> 
<p>7月4日，OSCS 监测到本次恶意 NPM 包投毒行为，已有服务器被攻击者控制</p>
                                        </div>
                                      
</div>
            