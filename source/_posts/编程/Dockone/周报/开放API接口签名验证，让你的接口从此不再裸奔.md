
---
title: '开放API接口签名验证，让你的接口从此不再裸奔'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/ef73e835980593ef3be144b820f5b29f.png'
author: Dockone
comments: false
date: 2021-04-30 00:14:00
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/ef73e835980593ef3be144b820f5b29f.png'
---

<div>   
<br><h3>接口安全问题</h3><ul><li>请求身份是否合法？</li><li>请求参数是否被篡改？</li><li>请求是否唯一？</li></ul><br>
<br><h3>AccessKey&SecretKey （开放平台）</h3><h4>请求身份</h4>为开发者分配AccessKey（开发者标识，确保唯一）和SecretKey（用于接口加密，确保不易被穷举，生成算法不易被猜测）。<br>
<h4>防止篡改</h4>参数签名：<br>
<ul><li>按照请求参数名的字母升序排列非空请求参数（包含AccessKey），使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串stringA；</li><li>在stringA最后拼接上Secretkey得到字符串stringSignTemp；</li><li>对stringSignTemp进行MD5运算，并将得到的字符串所有字符转换为大写，得到sign值。</li></ul><br>
<br>请求携带参数AccessKey和Sign，只有拥有合法的身份AccessKey和正确的签名Sign才能放行。这样就解决了身份验证和参数篡改问题，即使请求参数被劫持，由于获取不到SecretKey（仅作本地加密使用，不参与网络传输），无法伪造合法的请求。<br>
<h4>重放攻击</h4>虽然解决了请求参数被篡改的隐患，但是还存在着重复使用请求参数伪造二次请求的隐患。<br>
<br>timestamp+nonce方案：<br>
<br>nonce指唯一的随机字符串，用来标识每个被签名的请求。通过为每个请求提供一个唯一的标识符，服务器能够防止请求被多次使用（记录所有用过的nonce以阻止它们被二次使用）。<br>
<br>然而，对服务器来说永久存储所有接收到的nonce的代价是非常大的。可以使用timestamp来优化nonce的存储。<br>
<br>假设允许客户端和服务端最多能存在15分钟的时间差，同时追踪记录在服务端的nonce集合。当有新的请求进入时，首先检查携带的timestamp是否在15分钟内，如超出时间范围，则拒绝，然后查询携带的nonce，如存在已有集合，则拒绝。否则，记录该nonce，并删除集合内时间戳大于15分钟的nonce（可以使用redis的expire，新增nonce的同时设置它的超时失效时间为15分钟）。<br>
<h4>实现</h4>请求接口：<a href="http://api.test.com/test?name=hello&home=world&work=java" rel="nofollow" target="_blank">http://api.test.com/test%3Fnam ... Djava</a><br>
<br>客户端：<br>
<ul><li>生成当前时间戳timestamp=now和唯一随机字符串nonce=random</li><li>按照请求参数名的字母升序排列非空请求参数（包含AccessKey）：stringA="AccessKey=access&home=world&name=hello&work=java&timestamp=now&nonce=random";</li><li>拼接密钥SecretKey：stringSignTemp="AccessKey=access&home=world&name=hello&work=java&timestamp=now&nonce=random&SecretKey=secret";</li><li>MD5并转换为大写：sign=MD5(stringSignTemp).toUpperCase();</li><li>最终请求：<a href="http://api.test.com/test?name=hello&home=world&work=java&timestamp=now&nonce=nonce&sign=sign;" rel="nofollow" target="_blank">http://api.test.com/test%3Fnam ... gn%3B</a></li></ul><br>
<br>服务端：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/ef73e835980593ef3be144b820f5b29f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/ef73e835980593ef3be144b820f5b29f.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Token&AppKey（APP）</h3>在APP开放API接口的设计中，由于大多数接口涉及到用户的个人信息以及产品的敏感数据，所以要对这些接口进行身份验证，为了安全起见让用户暴露的明文密码次数越少越好，然而客户端与服务器的交互在请求之间是无状态的，也就是说，当涉及到用户状态时，每次请求都要带上身份验证信息。<br>
<h4>Token身份验证</h4><ul><li>用户登录向服务器提供认证信息（如账号和密码），服务器验证成功后返回Token给客户端；</li><li>客户端将Token保存在本地，后续发起请求时，携带此Token；</li><li>服务器检查Token的有效性，有效则放行，无效（Token错误或过期）则拒绝。</li></ul><br>
<br>安全隐患：Token被劫持，伪造请求和篡改参数。<br>
<h4>Token+AppKey签名验证</h4>与上面开发平台的验证方式类似，为客户端分配AppKey（密钥，用于接口加密，不参与传输），将AppKey和所有请求参数组合成源串，根据签名算法生成签名值，发送请求时将签名值一起发送给服务器验证。这样，即使Token被劫持，对方不知道AppKey和签名算法，就无法伪造请求和篡改参数。再结合上述的重发攻击解决方案，即使请求参数被劫持也无法伪造二次重复请求。<br>
<h4>实现</h4>登陆和退出请求：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/6bd1864799309d0f472768478fcf1964.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/6bd1864799309d0f472768478fcf1964.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
后续请求：<br>
<ul><li>客户端 ：和上述开放平台的客户端行为类似，把AccessKey改为token即可。</li><li>服务端 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/8cd0fa6c3520846c64b1817724c765f1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/8cd0fa6c3520846c64b1817724c765f1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br>源码：<a href="https://github.com/Joker-Coder/awesome-pay" rel="nofollow" target="_blank">https://github.com/Joker-Coder/awesome-pay</a><br>
<br>原文链接：<a href="https://blog.csdn.net/qq_18495465/article/details/79248608" rel="nofollow" target="_blank">https://blog.csdn.net/qq_18495 ... 48608</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            