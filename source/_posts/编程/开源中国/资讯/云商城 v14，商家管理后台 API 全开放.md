
---
title: '云商城 v1.4，商家管理后台 API 全开放'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5958'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 12:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5958'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><span style="background-color:#ffffff; color:#333333">wangmarket-shop是一款saas云商城系统，无需懂服务器、后端技能，在线开通商城账户、添加商品、快速上线发布，极大降低商城开发成本!</span><br> <span style="background-color:#ffffff; color:#333333">一台1核2G服务器，可做过千独立商城</span></p> 
<h2 style="text-align:start">升级说明</h2> 
<ol> 
 <li>增加访客自助开通店铺的插件</li> 
 <li>全面完善整理出商家管理后台的开放API （<a href="https://gitee.com/leimingyun/dashboard/wikis/leimingyun/889cb0c9-be33-4a47-aec6-20cd27ea52be/preview?doc_id=1525567&sort_id=4241705">https://gitee.com/leimingyun/dashboard/wikis/leimingyun/889cb0c9-be33-4a47-aec6-20cd27ea52be/preview?doc_id=1525567&sort_id=4241705</a>）</li> 
 <li>增加访客访问记录的插件，可以记录访客什么时间开始访问、停留了多久、记录访客手机号，以便后台能筛选意向用户</li> 
 <li>优化总管理后台的资源权限数据</li> 
 <li>修复商品分类上传图片异常的问题</li> 
 <li>全面调整商家管理后台的jsp显示页面。并调整数据列表为VUE赋值方式</li> 
 <li>清理一些无用jsp页面</li> 
 <li>轮播图的存储字符有100变为180字符</li> 
</ol> 
<h2 style="text-align:start">在线快速体验</h2> 
<h4 style="text-align:start">1. 在线开通一个商城</h4> 
<p style="text-align:start">开通url： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fapi.imall.net.cn%2Fplugin%2FphoneCreateStore%2Freg.do" target="_blank">http://api.imall.net.cn/plugin/phoneCreateStore/reg.do</a></p> 
<h4 style="text-align:start">2. 体验店铺管理后台</h4> 
<p style="text-align:start">记得添加个分类、添加个商品，试试功能，同时也能测试时看到效果</p> 
<h4 style="text-align:start">3. 体验效果</h4> 
<p style="text-align:start">这里我们开放了一个方便体验的h5页面（这个H5页面也是开源的），访问url：<br> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.imall.net.cn%2Findex.html%3Fstoreid%3D1%26host%3Dhttps%3A%2F%2Fapi.imall.net.cn%2F" target="_blank">http://demo.imall.net.cn/index.html?storeid=1&host=https://api.imall.net.cn/</a><br> 其中:<br> storeid： 便是你开通的店铺的id，刚开通店铺后跳转的页面里就有。<br> host： 商城的url，如果你是自己跑在本地，这里可以传入 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2F" target="_blank">http://localhost:8080/</a> ，如果你部署在服务器，可以传入 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--ip-fr5c86lx7z%2F" target="_blank">http://服务器ip/</a> ，格式一定是 http:// 或者 https:// 开头、 / 结尾</p> 
<p style="text-align:start">这里只是给出了一个H5的一个演示，因为全部接口开放,你可以任意用它来做H5商城、PC商城、小程序商城、APP商城。。</p>
                                        </div>
                                      
</div>
            