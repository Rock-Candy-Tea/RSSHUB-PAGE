
---
title: 'Snowy v1.8 已发布，国内首个国密前后分离后台权限管理系统，让更多的人认识密码，使用密码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-76e6d4cdaa6bc8845fc906d6c17eb0b09a7.png'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 10:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-76e6d4cdaa6bc8845fc906d6c17eb0b09a7.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#40485b">随着密码技术的使用普及，软件安全越来越重要，让更多的人认识密码，使用密码，此版本采用了国产密码算法SM2、SM3、SM4及签名验签技术，软件层面完全符合等保测评要求。技术框架与密码结合，让前后分离“密”不可分！具体更新如下：</span></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>1、【登录】SM2前端加密，后端解密</strong></p> 
<p><img height="88" src="https://oscimg.oschina.net/oscnet/up-76e6d4cdaa6bc8845fc906d6c17eb0b09a7.png" width="783" referrerpolicy="no-referrer"></p> 
<p><br> <strong>2、【登录登出日志】SM2对登录登出日志做签名完整性保护存储</strong></p> 
<p><img height="193" src="https://oscimg.oschina.net/oscnet/up-ae6ed75713762b5db19112199f654a545fd.png" width="592" referrerpolicy="no-referrer"></p> 
<p><strong>3、【操作日志】SM2对操作日志做签名完整性保护存储</strong></p> 
<p><img height="220" src="https://oscimg.oschina.net/oscnet/up-896ab15396af232b3d1e7919cee1e16517f.png" width="596" referrerpolicy="no-referrer"></p> 
<p><strong>4、【Token】SM4（cbc模式）加密，Token不再曝光暴露</strong></p> 
<p><img height="352" src="https://oscimg.oschina.net/oscnet/up-c3bf0573025b06a5fc0921c53f18a4fffaf.png" width="1024" referrerpolicy="no-referrer"></p> 
<p><strong>5、【用户密码】SM3完整性保护存储，登录时做完整性校验</strong></p> 
<p><img height="114" src="https://oscimg.oschina.net/oscnet/up-dfbba5b38cb4f8559d01c3b7c1afe2237ce.png" width="787" referrerpolicy="no-referrer"></p> 
<p><strong>6、【用户手机号】SM4（cbc模式）加解密使用字段脱敏</strong></p> 
<p><img height="114" src="https://oscimg.oschina.net/oscnet/up-276a17b51de3d5b7aa6604e772ad06d8c1e.png" width="572" referrerpolicy="no-referrer"></p> 
<p><img height="333" src="https://oscimg.oschina.net/oscnet/up-f7e783a2c02c9f55ba6ffc1ff055f4a7baa.png" width="895" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">代码实现具体可看此次推送内容！</p>
                                        </div>
                                      
</div>
            